#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python imports
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from builtins import range
from future import standard_library
standard_library.install_aliases()
import configparser
import pickle
import cProfile
import copy
import datetime
import math
import logging
import operator
import os
import shutil
import sys
import time
import traceback
import numpy

import ADT
import alixe_library as al
import SELSLIB2

# Get a copy of the space group dictionary
dictio_space_groups = al.get_spacegroup_dictionary()

# Functions to help in optimization
def timing(f):
    """

    :param f:
    :type f:
    :return:
    :rtype:
    """

    def wrap(*args, **kwds):
        time1 = time.time()
        ret = f(*args, **kwds)
        time2 = time.time()
        print ('%s function took %0.3f s' % (f.__name__, (time2 - time1)))
        return ret

    return wrap


def profileit(func):
    """

    :param func:
    :type func:
    :return:
    :rtype:
    """

    def wrapper(*args, **kwargs):
        datafn = func.__name__ + ".profile"  # Name the data file sensibly
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.dump_stats(datafn)
        return retval

    return wrapper

def fishing_round_by_prio_list(dict_first_round_by_rotclu, reference_hkl, sg_symbol,phstat_version, path_phstat,
                               ncores, clust_fold, path_ins, path_best, cell, resolution, cycles, tolerance, orisub,
                               weight, oricheck=True, mapcc=False,ent_path=None,folder_mode=False,shelxe_line=None,
                               shelxe_path=None):


    # NOTE CM: I should possibly deprecate the use of the python version, but meanwhile this will make it work
    f_fom=(True if weight == 'f' else False)


    list_prio = []
    list_to_remove = []
    sg_number = al.get_space_group_number_from_symbol(sg_symbol)
    seed = 0  # We give the input sorted so in the fortran phstat we want it to use the first one as ref

    if not folder_mode:
        for rotclu in dict_first_round_by_rotclu.keys():
            topllg = 0
            name_clust_topllg = ''
            topzscore = 0
            name_clust_topzscore = ''
            for cluster in dict_first_round_by_rotclu[rotclu].keys():
                if dict_first_round_by_rotclu[rotclu][cluster]['dict_FOMs']['llg'] > topllg:
                    topllg = dict_first_round_by_rotclu[rotclu][cluster]['dict_FOMs']['llg']
                    name_clust_topllg = cluster
                if dict_first_round_by_rotclu[rotclu][cluster]['dict_FOMs']['zscore'] > topzscore:
                    topzscore = dict_first_round_by_rotclu[rotclu][cluster]['dict_FOMs']['zscore']
                    name_clust_topzscore = cluster
            if name_clust_topllg not in list_prio:
                list_prio.append(name_clust_topllg)
            if name_clust_topzscore not in list_prio:
                list_prio.append(name_clust_topzscore)
        list_rest = []
        for rotclu in dict_first_round_by_rotclu.keys():
            for cluster in dict_first_round_by_rotclu[rotclu]:
                if cluster not in list_prio:
                    list_rest.append((cluster, dict_first_round_by_rotclu[rotclu][cluster]['dict_FOMs']['llg']))
        sorted_list_rest = sorted(list_rest, key=lambda x: x[1])
        for i in range(len(sorted_list_rest)):
            sorted_list_rest[i] = sorted_list_rest[i][0]
        list_prio.extend(sorted_list_rest)
    else:
        list_prio = [ele for ele in dict_first_round_by_rotclu["0"].keys()]



    number_of_trials = int(ncores)
    max_number_of_trials = len(list_prio)
    dict_result_by_trial = {}
    raw_clust_second_round = open(os.path.join(clust_fold, "info_clust_second_round_raw"), 'w')
    del raw_clust_second_round
    table_clust_second_round = open(os.path.join(clust_fold, "info_clust_second_round_table"), 'w')
    if ent_path != None:
        table_clust_second_round.write('%-40s %-5s %-10s %-10s %-10s %-10s\n' % ('Cluster', 'n_phs', 'wmpd_max', 'wmpd_min','phi_cc','phi_wmpe'))
    else:
        table_clust_second_round.write(
            '%-40s %-5s %-10s %-10s %-10s \n' % ('Cluster', 'n_phs', 'wmpd_max', 'wmpd_min', 'phi_cc'))
    del table_clust_second_round
    for i in range(number_of_trials):
        if i >= max_number_of_trials:
            break  # We can't use more references, we finished the list!
        reference = list_prio[i]
        if (os.path.split(reference))[1] in list_to_remove:
            print("This reference, ", reference, " was already fished with another reference. Skipping this cycle")
            continue  # We go to the next iteration, because this reference has been fished already
        name_ref = os.path.split(reference)[1]
        name_phi = reference[:-4] + "_ref.phi"
        if phstat_version == 'python':
            dict_phs = {}
            dict_phs[reference] = True
            for j in range(len(list_prio)):
                name_file = (os.path.split(list_prio[j]))[1]
                if (list_prio[j] not in dict_phs.keys()) and (name_file not in list_to_remove):
                    dict_phs[list_prio[j]] = False
            dict_result_by_trial[list_prio[i]] = startALIXEasPHSTAT(clust_fold, reference_hkl, dict_phs, cell,
                                                                    sg_number, tolerance=tolerance,
                                                                    resolution=resolution, cycles=cycles, f_fom=f_fom)
        elif phstat_version == 'fortran':
            path = os.path.normpath(clust_fold)  # relative path because fortran does not accept such long paths
            list_path = path.split(os.sep)
            relative_path_clust_fold = './' + list_path[-1]
            # 1) Write an ls file with the list of phs, putting first the reference
            path_ls = os.path.join(clust_fold, reference[:-4] + "_ref.ls")
            relative_ref = os.path.join(relative_path_clust_fold, name_ref)
            lsrotfile = open(path_ls, 'w')
            lsrotfile.write(relative_ref + '\n')
            for j in range(len(list_prio)):
                phs_namefile = (os.path.split(list_prio[j]))[1]
                phs_relative_path = os.path.join(relative_path_clust_fold, phs_namefile)
                if phs_relative_path != relative_ref and (phs_namefile not in list_to_remove):
                    lsrotfile.write(phs_relative_path + '\n')
            lsrotfile.close()
            # 2.1) Link the ins file
            os.link(path_ins, os.path.join(clust_fold, path_ls[:-3] + ".ins"))
            # 2.1) Link a pda file
            os.link(path_best, os.path.join(clust_fold, path_ls[:-3] + ".pda"))
            # 3) Launch the function in alixe_library
            complete_output,errors = al.call_phstat_print_for_clustering(path_ls[:-3], relative_path_clust_fold,
                                                                         path_phstat,resolution, seed, tolerance,
                                                                         cycles, orisub, weight,oricheck,mapcc)
            print(complete_output)
            #print errors

            ls = open(path_ls, "r")
            lineas_fichero_ls = ls.readlines()
            numero_phs = len(lineas_fichero_ls)
            del ls

            dict_result_by_trial[reference] = {name_phi: None}

            # NOTE CM: Change to make it compatible with our newest phstat
            #dict_result_by_trial[reference][name_phi] = al.read_phstat_print_clusterization_output(ls_content,
            #                                                                                      complete_output,
            #                                                                                       cycles)
            dict_result_by_trial[reference][name_phi],runtime = al.read_phstat_isa_clusterization_output(complete_output=complete_output,
                                                                                                 cycles=cycles, n_files=numero_phs)

        # NOTE: Because of the relative paths, in the fortran case I need to modify the dictionary now to contain the full paths
        raw_clust_second_round = open(os.path.join(clust_fold, "info_clust_second_round_raw"), 'a')
        raw_clust_second_round.write(
            "*********************************************************************************************************************************************\n")
        n_phs = len(dict_result_by_trial[list_prio[i]][name_phi].keys())
        raw_clust_second_round.write("CLUSTER fishing with reference " + name_ref + ' , found in file ' + name_ref[
                                                                                                          :-4] + '_ref.phi, containing ' + str(
            n_phs) + ' phase files' + '\n')
        for key1 in dict_result_by_trial[list_prio[i]].keys():
            wmpe_max = 0.0
            wmpe_min = 90.0
            for key2 in dict_result_by_trial[list_prio[i]][key1].keys():
                if phstat_version == 'fortran':
                    new_key2 = os.path.join(clust_fold, os.path.split(key2)[1])
                    dict_result_by_trial[list_prio[i]][key1][new_key2] = copy.deepcopy(
                        dict_result_by_trial[list_prio[i]][key1][key2])
                    del dict_result_by_trial[list_prio[i]][key1][key2]
                    raw_clust_second_round.write(
                        new_key2 + "\t" + str(dict_result_by_trial[list_prio[i]][key1][new_key2]) + '\n')
                    wmpe = dict_result_by_trial[list_prio[i]][key1][new_key2]['wMPE_first']
                else:
                    raw_clust_second_round.write(
                        key2 + "\t" + str(dict_result_by_trial[list_prio[i]][key1][key2]) + '\n')
                    wmpe = dict_result_by_trial[list_prio[i]][key1][key2]['wMPE']
                list_to_remove.append(os.path.split(key2)[1])
                if wmpe > wmpe_max:
                    wmpe_max = wmpe
                if wmpe < wmpe_min and wmpe != 0.0:  # Because 0.0 is to itself, the reference
                    wmpe_min = wmpe

            name_cluster = (os.path.split(key1))[1]

            if wmpe_max == 0.0 and wmpe_min == 90.0:  # Then we have not clustered them
                wmpe_max = 0.0
                wmpe_min = 0.0
            # TODO: I should also include the generation of some sum file like in the first round

            # TODO: Here, if I do have an ent, perform a postmortem of the phi (CAREFUL, THIS IS COPIED FROM ELSEWHERE)
            if ent_path != None:
                table_clust_second_round = open(os.path.join(clust_fold, "info_clust_second_round_table"), 'a')
                name_shelxe = name_cluster[:-4]
                path_name_shelxe = os.path.join(clust_fold, name_shelxe)
                os.link(ent_path, path_name_shelxe + ".ent")
                os.link(reference_hkl, path_name_shelxe + ".hkl")
                #os.link(path_ins, path_name_shelxe + ".ins")
                output = al.phase_with_shelxe_from_phi(shelxe_line, name_shelxe, clust_fold, shelxe_path)
                lst_file = open(path_name_shelxe + '.lst', 'r')
                lst_content = lst_file.read()
                list_fom = al.extract_EFOM_and_pseudoCC_shelxe(lst_content)
                list_mpe = al.extract_wMPE_shelxe(clust_fold + name_shelxe + '.lst')
                wmpe_phi=list_mpe[2]
                # Soon I will have a version of SHELXE that also computes initCC
                # initcc = al.extract_INITCC_shelxe(lst_content)
                initcc=-1.0


            table_clust_second_round = open(os.path.join(clust_fold, "info_clust_second_round_table"), 'a')
            if ent_path != None:
                table_clust_second_round.write('%-40s %-5s %-10f %-10f %-10f %-10f\n' % (name_cluster, n_phs, wmpe_max,
                                                                                         wmpe_min,initcc,wmpe_phi))
            else:
                table_clust_second_round.write(
                    '%-40s %-5s %-10s %-10f %-10f \n' % (name_cluster, n_phs, wmpe_max, wmpe_min))
            del table_clust_second_round

        del raw_clust_second_round

    return dict_result_by_trial


def startALIXEasPHSTAT(clust_fold, reference_hkl, dict_phs, cell, sg_number, tolerance=75.0, resolution=2.0, cycles=3,
                       f_fom=True):
    """ Minimal version of the ALIXE program.

    :param clust_fold: directory to perform the clustering
    :type clust_fold: str
    :param reference_hkl: the path for the hkl given for shelxe, to filter by evalues the phs in case there is extrapolated data
    :type reference_hkl: str
    :param dict_phs: phs dictionary with values that are the phs and keys set to True if they have to be tested as references and False otherwhise
    :type dict_phs: dict
    :param cell: the unit cell parameters, in the form of a list of floats
    :type cell: list
    :param sg_number: space group number
    :type sg_number: int
    :param tolerance: tolerance for the MPE value between the phase sets
    :type tolerance: float
    :param resolution: resolution to filter the phase sets for combination
    :type resolution: float
    :param cycles: number of macrocycles of combination
    :type cycles: int
    :param f_fom: If true, mpe are weighted by Fvalues, otherwhise, by E values
    :type f_fom: bool
    :return: dictio_clusters
    :rtype: dict
    """

    print('\n ALIXE started at: ', time.strftime("%c"))
    start = datetime.datetime.now()
    dictio_clusters = {}  # Dictionary to return the results

    # Get the symmetry information thanks to the sg_number
    symops = al.get_symops_from_sg_dictionary(sg_number)
    polar, origins = al.get_origins_from_sg_dictionary(sg_number)

    # Compute the coefficients needed for other calculations
    unit = cell[0] * cell[1] * cell[2]  # Sides of the cell (abc)
    coef1 = []
    coef2 = []
    coef3 = []
    list_cos = []
    list_sin = []
    for n in range(0, 3):
        angle_rad = 1.74533 * math.pow(10, -2) * (cell[n + 3])  # Convert to radian units the angles
        cos_angle = numpy.cos(angle_rad)
        list_cos.append(cos_angle)
        sin_angle = numpy.sin(angle_rad)
        list_sin.append(sin_angle)
        exp1 = 2.0 * unit * (cos_angle / cell[n])  # 2.0 * abc * (cos_angle/side)
        coef1.append(exp1)
    volume = unit * math.sqrt(1 - (list_cos[0]) ** 2 - (list_cos[1]) ** 2 - (list_cos[2]) ** 2 + (
    2 * list_cos[0] * list_cos[1] * list_cos[2]))  # V = abc * (1-cos²α-cos²β-cos²γ+2cosαcosβcosγ)^(-1/2)
    unit = unit / volume # abc / volume
    for n in range(0, 3):
        exp2 = 0.25 * unit * ((list_sin[n] / cell[n]) ** 2)
        coef2.append(exp2)
    unit = unit / volume # (abc / V) / V , so abc/V²
    coef3.append(unit * cell[0] * (list_cos[1] * list_cos[2] - list_cos[0]))  # (abc/V²) * a *(cosβ*cosγ-cosα)
    coef3.append(unit * cell[1] * (list_cos[0] * list_cos[2] - list_cos[1]))  # (abc/V²) * b *(cosα*cosγ-cosβ)
    coef3.append(unit * cell[2] * (list_cos[0] * list_cos[1] - list_cos[2]))  # (abc/V²) * c *(cosα*cosβ-cosγ)


    # TODO: Add a filtering for the extrapolated phases in the phs if they exists

    # Generate a list with the phs from the dictionary that are references
    list_references = [phs for _, phs in enumerate(dict_phs.keys()) if dict_phs[phs]]

    # Use the first phs file to compute the evalues and epsilon factors
    ref_for_evalues = list_references[0]
    # Process the array
    array_ref = al.read_phs_file(ref_for_evalues)
    #print 'Resolution check set to ',resolution
    array_ref, max_resolution = al.check_resolution_limit(array_ref, resolution, coef2,
                                          coef3)  # We will use the coefficients saved in coef2 and coef3
    #if max_resolution!=resolution:
    #     print 'Warning: the resolution cut set for phase clustering is of ',resolution
    #     print 'while your data has a maximum resolution of ',max_resolution
         #print 'Automatically adjusting resolution to ',max_resolution
         #resolution=max_resolution
    array_ref = al.change_to_standard_equivalent_reflections(array_ref, sg_number)
    array_ref = al.sort_reflections_phs(array_ref)
    # Get the number of reflections that we expect in all the phs files
    nreflections = len(array_ref)
    # Find epsilon factor and 1/dsquared
    epsilon, onedsquared, res_max = al.get_epsilon_1overdsquared_and_resmax(array_ref, symops, coef2, coef3)
    # Estimate E-values (whats changes in phs is phases, not structure factors)
    array_evalues, array_aux = al.get_evalues_and_array_aux(epsilon, onedsquared, res_max,
                                                            array_ref)  # e-values only in the array_evalues

    # Save the information that is common to all phs 
    # # # Before
    # array_miller_indices = []
    # array_f_sigf = []
    # for i, _ in enumerate(array_ref):
    #     array_miller_indices.append([array_ref[i][0], array_ref[i][1], array_ref[i][2]])
    #     array_f_sigf.append([array_ref[i][3], array_ref[i][6]])
    # # # After
    array_miller_indices = [ [array_ref[i][0], array_ref[i][1], array_ref[i][2]] for i, _ in enumerate(array_ref)]
    array_f_sigf = [ [array_ref[i][3], array_ref[i][6]] for i, _ in enumerate(array_ref) ]
    array_ref = None

    n_phs = len(dict_phs.keys())
    print("\n Processing ", str(n_phs), " phase files")
    # Prepare the arrays to save
    list_arrays_va_to_modify = [None for x in range(n_phs)]
    list_arrays_vb_to_modify = [None for x in range(n_phs)]
    list_arrays_to_modify = [None for x in range(n_phs)]
    list_names_phs = [None for x in range(n_phs)]

    for iphs, phs in enumerate(dict_phs.keys()):
        try:
            if phs[-4:] == ".phi":  # NOTE: My phi files are the same as phs files NOW
                array_phs = al.read_phs_file(phs)
            elif phs[-4:] == ".phs":
                array_phs = al.read_phs_file(phs)
            else:
                print("ALIXE only supports clustering of SHELXE phi or phs files")
                sys.exit(0)
            # Save the name so that we have the correct order
            list_names_phs[iphs] = phs  # phs is the full path of the phs
            # Check resolution limit
            filter_res_array, max_resolution = al.check_resolution_limit(array_phs, resolution, coef2,coef3)
            # Find equivalent reflections with standard indices and transform phases
            array_merged = al.change_to_standard_equivalent_reflections(filter_res_array, sg_number)
            # Sort reflections in order of higher h,k and l indexes
            sorted_array = al.sort_reflections_phs(array_merged)
            new_sorted_array = []
            for r in range(len(sorted_array)):
                if not ((sorted_array[r][0] == array_miller_indices[r][0]) and
                        (sorted_array[r][1] == array_miller_indices[r][1]) and
                        (sorted_array[r][2] == array_miller_indices[r][2])):
                    #print 'sorted_array h,k,l',sorted_array[r][0],sorted_array[r][1],sorted_array[r][2]
                    #print 'array_miller_indices h,k,l',array_miller_indices[r][0],array_miller_indices[r][1],array_miller_indices[r][2]
                    #print 'type(sorted_array[r][0])',type(sorted_array[r][0])
                    #print 'type(array_miller_indices[r][0])',type(array_miller_indices[r][0])
                    # NOTE CM: Temporary to see how many reflections have this problem and whether it affects a lot or not
                    continue
                    #sys.exit(0)
                else:
                    new_sorted_array.append(sorted_array[r])

            if len(sorted_array)!=len(new_sorted_array):
                print('phs with the problem is ',phs)
                sys.exit(0)
            # Reduce the array to the phi and FOM values
            reduced_array = al.reduce_array_phs_to_PHI_and_FOM(sorted_array)  # [FOM,PHI]
            list_arrays_to_modify[iphs] = reduced_array
            # For all, including the reference, obtain VA and VB
            arrva, arrvb = al.get_VA_and_VB(reduced_array)
            list_arrays_va_to_modify[iphs] = arrva
            list_arrays_vb_to_modify[iphs] = arrvb
        except:
            print('\n Attention: Some error happened during processing of file ', phs)
            sys.exit(0)

    print('\n Finished reading the phs files')

    # Save the arrays as pickle objects
    save_double_array = open(os.path.join(clust_fold, 'double_array.pkl'), 'wb')
    pickle.dump(list_arrays_to_modify, save_double_array)
    save_double_array.close()
    save_arrva = open(os.path.join(clust_fold, 'arrva.pkl'), 'wb')
    pickle.dump(list_arrays_va_to_modify, save_arrva)
    save_arrva.close()
    save_arrvb = open(os.path.join(clust_fold, 'arrvb.pkl'), 'wb')
    pickle.dump(list_arrays_vb_to_modify, save_arrvb)
    save_arrvb.close()

    # Now test all references in the list
    for _, reference in enumerate(list_references):
        print("\n Testing reference", reference)
        name_phi = (os.path.split(reference)[1])[:-4] + '_ref.phi'
        path_phi = os.path.join(clust_fold, name_phi)
        position = list_names_phs.index(reference)
        dictio_clusters[path_phi] = {}
        # We load the arrays again for each reference to make sure we have the unmodified original ones
        back_double_array = open(os.path.join(clust_fold, 'double_array.pkl'), 'rb')
        list_arrays_to_modify = pickle.load(back_double_array)
        back_double_array.close()
        array_ref = copy.deepcopy(list_arrays_to_modify[position])
        back_arrva = open(os.path.join(clust_fold, 'arrva.pkl'), 'rb')
        list_arrays_va_to_modify = pickle.load(back_arrva)
        back_arrva.close()
        back_arrvb = open(os.path.join(clust_fold, 'arrvb.pkl'), 'rb')
        list_arrays_vb_to_modify = pickle.load(back_arrvb)
        back_arrvb.close()
        # Phase combination macrocycles
        for c in range(cycles):
            print('\n Cluster analysis cycle ', str(c + 1))
            print('\n N' + '\t' + 'wMPE' + '\t' + 'Dif' + '\t' + 'MapCC' + '\t' + 'Origin shift' + '\t\t' + 'Phase file')
            dictio_clusters[path_phi][c + 1] = {}  # We will save the results cycle by cycle
            # For every phs, find and apply origin shifts relative to reference phases
            dict_wmpes_sel = {}
            list_wmpes_sel = []
            for pos, _ in enumerate(list_arrays_to_modify):
                name_current_phs = list_names_phs[pos]
                dict_wmpes_sel[name_current_phs] = {"wMPE": 0.0, "diff_wMPE": 0.0, "mapcc": 0.0}
                s = 0.0
                t = 0.0
                # Check that the number of reflections is the expected one (all should have the same)
                nreflections_current = len(list_arrays_to_modify[pos])
                if nreflections_current != nreflections:
                    print('The number of reflections of this phase file is not compatible with the reference file')
                    print('Please check, some error in the files is expected')
                    sys.exit(0)
                for r, _ in enumerate(list_arrays_to_modify[pos]):
                    list_arrays_to_modify[pos][r][1] = list_arrays_vb_to_modify[pos][r]  # Phases setting
                    # Check the FOM to be set
                    if f_fom == True:
                        list_arrays_to_modify[pos][r][0] = array_f_sigf[r][0] * list_arrays_va_to_modify[pos][
                            r]  # Structure Factor current reflection * FOM current reflection
                    elif f_fom == False:
                        list_arrays_to_modify[pos][r][0] = array_evalues[r] * list_arrays_va_to_modify[pos][
                            r]  # E-value current reflection * FOM current reflection
                    s = s + list_arrays_to_modify[pos][r][0] # Summatory of the FOMs
                    t = t + list_arrays_to_modify[pos][r][0] * abs(
                        ((900.0 + list_arrays_to_modify[pos][r][1] - list_arrays_vb_to_modify[pos][r]) % 360.0) - 180.0)
                # Here is where when we have to apply the origin shifts and calculate the wMPE and the mapCC
                current_weights = list_arrays_va_to_modify[pos]  # array with the FOMs of the current phs
                sorted_list_wmpe, sorted_list_mapcc = al.apply_origin_shift_and_compute_wMPE_and_CC(n_reflections=nreflections,
                                                                                                    symops=symops,
                                                                                                    array_ref=array_ref,
                                                                                                    array_miller_indices=
                                                                                                    array_miller_indices,
                                                                                                    array_f_sigf=array_f_sigf,
                                                                                                    current_array=
                                                                                                    list_arrays_to_modify[pos],
                                                                                                    current_weights=
                                                                                                    current_weights,
                                                                                                    array_evalues=
                                                                                                    array_evalues,
                                                                                                    array_aux=array_aux,
                                                                                                    sg_number=sg_number,
                                                                                                    f_fom=f_fom)
                shift_to_apply = sorted_list_wmpe[0][1]
                wmpe_shift = sorted_list_wmpe[0][0]
                for i in range(len(sorted_list_mapcc)):  # Get the mapCC that corresponds to that shift
                    if sorted_list_mapcc[i][1] == shift_to_apply:
                        map_CC = sorted_list_mapcc[i][0]
                # Get difference top best/second best for the wMPE if we are not in a polar sg
                if polar == False:
                    diff_mpe = sorted_list_wmpe[1][0] - sorted_list_wmpe[0][0]
                elif polar == True:
                    diff_mpe = 0
                dict_wmpes_sel[name_current_phs] = {"wMPE": wmpe_shift, "diff_wMPE": diff_mpe, "mapcc": map_CC,
                                                    'shift': shift_to_apply}
                list_wmpes_sel.append((name_current_phs, wmpe_shift))
                for r, _ in enumerate(list_arrays_vb_to_modify[pos]):  # Modify the phases saved
                    list_arrays_vb_to_modify[pos][r] = ((720.0 + (360.0 * (((
                                                                            shift_to_apply[0] * array_miller_indices[r][
                                                                                0]) + (
                                                                            shift_to_apply[1] * array_miller_indices[r][
                                                                                1]) + (
                                                                            shift_to_apply[2] * array_miller_indices[r][
                                                                                2])) % 1.0)) +
                                                         list_arrays_vb_to_modify[pos][r]) % 360.0)

            # Sort the phase sets according to their mean phase error
            sorted_by_mpe = sorted(list_wmpes_sel, key=lambda x: x[1], reverse=False)
            # Check if anything will cluster under the tolerance we set
            if len(sorted_by_mpe) > 1:
                if sorted_by_mpe[1][1] > tolerance:
                    print('There are not solutions to cluster under the tolerance set')
                    if c + 1 != 1:
                        print('HEY, THIS HAPPENED IN A CYCLE DIFFERENT FROM CYCLE 1')
                        print('Error, please report to bugs-borges@ibmb.csic.es')
                        sys.exit(0)
                    dictio_clusters[path_phi] = {sorted_by_mpe[0][0]: {'wMPE': sorted_by_mpe[0][1],
                                                                       'diff_wMPE': dict_wmpes_sel[sorted_by_mpe[0][0]][
                                                                           'diff_wMPE'],
                                                                       'mapcc': dict_wmpes_sel[sorted_by_mpe[0][0]][
                                                                           'mapcc'], 'shift': [0.0, 0.0, 0.0]}}
                    # Write the phases with the resolution cut to a file
                    file_phi = open(path_phi, 'w')
                    pos = list_names_phs.index(sorted_by_mpe[0][0])  # Position of the reference array in the reading
                    nreflections = len(list_arrays_va_to_modify[pos])
                    for r in range(nreflections):
                        # 3I4,F9.2,F8.4,F8.1,F8.2
                        file_phi.write('%4i%4i%4i%9.2f%8.4f%8.1f%8.2f\n' % (
                        array_miller_indices[r][0], array_miller_indices[r][1], array_miller_indices[r][2],
                        array_f_sigf[r][0], list_arrays_va_to_modify[pos][r], list_arrays_vb_to_modify[pos][r],
                        array_f_sigf[r][1]))
                    del file_phi
                    return dictio_clusters

            # Combine phases for cluster
            # 1) Generate clean arrays of contributions VA and VB and for the combination
            va = [0.0 for _ in range(len(array_ref))]  # fom
            vb = [0.0 for _ in range(len(array_ref))]  # phases
            wa_combi = [0.0 for _ in range(len(array_ref))]
            # 2) Iterate over the phs files (consider sorting)
            for ind in range(len(sorted_by_mpe)):
                current_phs = sorted_by_mpe[ind][0]
                current_wmpe = sorted_by_mpe[ind][1]
                current_dif_wmpe = dict_wmpes_sel[current_phs]['diff_wMPE']
                current_mapcc = dict_wmpes_sel[current_phs]['mapcc']
                current_shift = dict_wmpes_sel[current_phs]['shift']
                pos = list_names_phs.index(current_phs)
                if current_wmpe < tolerance:
                    print(' ', ind + 1, '\t', "{0:.1f}".format(current_wmpe), '\t', "{0:.1f}".format(
                        current_dif_wmpe), '\t', "{0:.2f}".format(current_mapcc), '\t', current_shift,'\t' ,current_phs)
                    dictio_clusters[path_phi][c + 1][current_phs] = copy.deepcopy(dict_wmpes_sel[current_phs])
                    for r in range(nreflections):
                        list_arrays_to_modify[pos][r][1] = list_arrays_vb_to_modify[pos][r]
                        t = 0.0174533 * list_arrays_to_modify[pos][r][1]  # 0.0174533 is 2pi/360
                        s = list_arrays_va_to_modify[pos][r]
                        va[r] = va[r] + (s * (numpy.cos(t)))
                        vb[r] = vb[r] + (s * (numpy.sin(t)))
                    t = numpy.sqrt(1.0 / (ind + 1))
                    for r in range(nreflections):
                        wa_combi[r] = min(1.0, numpy.sqrt(math.pow(va[r], 2) + math.pow(vb[r], 2)) * t)
                        # Use either structure factors or normalized structure factors for the combined phases
                        list_arrays_to_modify[pos][r][0] = wa_combi[r] * array_evalues[
                            r]  # e-weighted,as it is in the fortran prototype
                        ##                        if f_fom==True:
                        ##                            list_arrays_to_modify[pos][r][0]=array_f_sigf[r][0]*wa_combi[r] #  StructureFactor * new_weight
                        ##                        elif f_fom==False:
                        ##                            alist_arrays_to_modify[pos][r][0]=array_evalues[r]*wa_combi[r] # E-value * new_weight
                        if wa_combi[r] > 0.0001:
                            list_arrays_to_modify[pos][r][1] = (720.0 + 57.29578 * numpy.arctan2(vb[r], va[r])) % 360
                        # NOTE: experimenting what is happening here
                        #current_weights[r] = list_arrays_to_modify[pos][r][0] # Save the new weight
                        # NOTE: experimenting what is happening here
                    # Compute again the shift, because now we changed the phases
                    sorted_list_wmpe2, sorted_list_mapcc2 = al.apply_origin_shift_and_compute_wMPE_and_CC(n_reflections
                                                                                                          =nreflections,
                                                                                                          symops=symops,
                                                                                                          array_ref=
                                                                                                          array_ref,
                                                                                                          array_miller_indices=array_miller_indices,
                                                                                                          array_f_sigf=array_f_sigf,
                                                                                                          current_array=list_arrays_to_modify[
                                                                                                              pos],
                                                                                                          current_weights=current_weights,
                                                                                                          array_evalues=array_evalues,
                                                                                                          array_aux=array_aux,
                                                                                                          sg_number=sg_number,
                                                                                                          f_fom=f_fom)
                    shift_to_apply2 = sorted_list_wmpe2[0][1]
                    if shift_to_apply2 != [0.0, 0.0, 0.0]:  # Check if there ever is another shift after
                        if not (abs(shift_to_apply2[0]) < 0.01 and abs(shift_to_apply2[1]) < 0.01 and abs(
                                shift_to_apply2[2]) < 0.01):
                            print("There is another shift to apply after phase merging ", shift_to_apply2)
                            #sys.exit(0)
                            print("Applying it")
                            for r in range(nreflections):
                                list_arrays_to_modify[pos][r][1] = ((720.0 + (360.0 * (((
                                                                            shift_to_apply2[0] * array_miller_indices[r][
                                                                                0]) + (
                                                                            shift_to_apply2[1] * array_miller_indices[r][
                                                                                1]) + (
                                                                            shift_to_apply2[2] * array_miller_indices[r][
                                                                                2])) % 1.0)) +
                                                         list_arrays_vb_to_modify[pos][r]) % 360.0)
                    # Change the phases in the reference array so that they correspond to the combined map                                                 list_arrays_to_modify[pos][r][1]) % 360.0)
                    for r in range(nreflections):
                        array_ref[r][1] = list_arrays_to_modify[pos][r][1]
        # Write the cumulative phases to a file
        file_phi = open(path_phi, 'w')
        # print 'path_phi',path_phi
        for r in range(len(array_ref)):
            # 3I4,F9.2,F8.4,F8.1,F8.2
            file_phi.write('%4i%4i%4i%9.2f%8.4f%8.1f%8.2f\n' % (
            array_miller_indices[r][0], array_miller_indices[r][1], array_miller_indices[r][2], array_f_sigf[r][0],
            wa_combi[r], array_ref[r][1], array_f_sigf[r][1]))
        del file_phi

    print('\n Cleaning up....')
    for fich in os.listdir(clust_fold):
        if fich.endswith('.pkl'):
            os.remove(os.path.join(clust_fold, fich))
    # Return just the last cycle results
    # dictio_clusters_third = {}
    # for key in dictio_clusters.keys():
    #     dictio_clusters_third[key] = dictio_clusters[key][cycles]
    # end = datetime.datetime.now()
    # print " ALIXE took  ", end - start, "to run"
    # return dictio_clusters_third
    # NOTE CM: do we really only want the last cycle?
    # NOTE CM: first cycle is more representative of what has happened with the original files
    dictio_clusters_first = {}
    for key in dictio_clusters.keys():
        dictio_clusters_first[key] = dictio_clusters[key][1]
    return dictio_clusters_first


def clustering_all_in_ALIXE_under_a_tolerance_python(clust_fold, reference_hkl, list_phs, cell, sg_symbol, tolerance,
                                              resolution, cycles, fom_weigth, ncores):
    '''Sequentially calls startALIXE in order to generate all possible clusters under a certain tolerance.

    :param clust_fold:
    :type clust_fold: str
    :param reference_hkl:
    :type reference_hkl: str
    :param list_phs:
    :type list_phs: list
    :param cell:
    :type cell: list
    :param sg_symbol:
    :type sg_symbol: str
    :param tolerance:
    :type tolerance: float
    :param resolution:
    :type resolution: float
    :param cycles:
    :type cycles: int
    :param fom_weigth: if True, weight applied is by Structure Factors, if False, by E-values
    :type fom_weigth: bool
    :param ncores:
    :type ncores: int
    :return dictio_clusters:  a dictionary with the results of the clustering.
    Keys are phi paths, and value is another dictionary with the following structure:
    :rtype dictio_clusters: dict


    '''
    # Initialize required variables
    dictio_clusters = {}
    sg_number = al.get_space_group_number_from_symbol(sg_symbol)

    # Main loop, until all the phs in the list have been processed or we will not expand them anyway
    while (len(list_phs) > 0) and (len(dictio_clusters.keys()) <= ncores):
        dict_phs = {}
        for i in range(len(list_phs)):
            if i == 0:
                dict_phs[list_phs[i]] = True
            else:
                dict_phs[list_phs[i]] = False
        results = startALIXEasPHSTAT(clust_fold, reference_hkl, dict_phs, cell, sg_number, tolerance, resolution,
                                     cycles, fom_weigth)
        # I can safely assume that if I just give one reference,
        # the results dictionary keys list will have just one phi name
        phi_name = list(results.keys())[0]
        phs_to_remove = list(results[phi_name].keys())
        n_phs = len(phs_to_remove)
        dictio_clusters[phi_name] = {'dictio_result': results[phi_name], 'n_phs': n_phs, 'dict_FOMs': {}}
        new_list_phs = []
        for phs in list_phs:
            if phs in phs_to_remove:
                continue
            else:
                new_list_phs.append(phs)
        list_phs = new_list_phs
    return dictio_clusters


# Main module
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("\nUsage: ALIXE.py name.ls [options]")
        print("\nOptions:")
        print("\n-s=name_reference Use the name_reference phase file in the ls file as reference for clustering. It also accepts a list separated by commas.")
        print("\n-t= Use a tolerance of N degrees for the mean phase difference between the phase sets compared")
        print("\n-r=N Use data to a resolution of N angstroms. Default is 2.0")
        print("\n-c=N Do N macrocycles of phase clustering between the sets")
        # print "-h=hkl_filename Reference hkl to calculate evalues"
        # TODO: it is better that symmetry is given either as a number of the sg or a line in the ls (if maps are given)
        print("\n-p=pdb_filename Read symmetry information from a pdb file")
        print("\n-w=f or -w=e Use f-weights or e-weights for the calculation of mean phase errors. Default is f")
        print("\n-d=working_directory Indicate the folder were to put the results. Default is the current working directory")
        sys.exit(0)
    print("\n Starting date & time " + time.strftime("%c"))  # Print initial time
    # Read ls file and save the files in a list
    name_ls = sys.argv[1]
    fich_ls = open(name_ls, 'r')
    list_phs = fich_ls.read().splitlines()
    list_phs = [ phs.strip() for phs in list_phs]
    dictio_phs = {}
    for phs in list_phs:
        dictio_phs[phs] = False
    n_phs = len(list_phs)
    print("\n ", str(n_phs), " phase files found in ", name_ls)
    # Read the arguments or set the defaults
    list_options = sys.argv[2:]
    # Defaults
    reference_set = list_phs[0]  # The first one in the ls
    position_ref = 1
    tolerance = 60
    resolution = 2.0
    dictio_phs[reference_set] = True  # Default is to use the first phs in the list
    cycles = 3
    f_fom = True
    reference_hkl = None  # TEMPORARY, NEED TO CHECK WITH ISABEL
    clust_fold = os.getcwd()
    cell = None

    for option in list_options:
        if option.startswith("-s"):
            # Check if they have given a single reference or a list separated by comma
            # if len(option[3:].split(','))>1:
            #    list_references=option[3:].split(',')
            #    for reference in list_references:
            #        dictio_phs[reference]=True
            # elif len(option[3:].split(','))==1: # Then we have a single reference
            # print 'option[3:]',option[3:]
            ref = option[3:]
            dictio_phs[ref] = True
            # If it is not the same one, remove te True from the default
            if ref != reference_set:
                dictio_phs[reference_set] = False
        elif option.startswith("-t"):
            tolerance = float(option[3:])
        elif option.startswith("-r"):
            resolution = float(option[3:])
        elif option.startswith("-h"):
            reference_hkl = option[3:]
        elif option.startswith("-c"):
            cycles = int(option[3:])
        elif option.startswith("-w"):
            weight_fom = option[3:]
            if weight_fom == 'e':
                f_fom = False
        elif option.startswith("-p"):  # Read the symmetry from a pdb file
            pdb_path = str(option[3:])
            cell, sg = al.read_cell_and_sg_from_pdb(pdb_path)  # Cell is a list of floats
            sg_number = al.get_space_group_number_from_symbol(sg)
        elif option.startswith("-d"):
            clust_fold = str(option[3:])

    # Check we have the symmetry info
    if cell == None:
        print("Sorry, you need to provide some pdb file to extract the symmetry information")
        sys.exit(0)

    # Generate a fake ins that SHELXE can read for expansions
    path_ins = os.path.join(clust_fold, 'name.ins')
    al.generate_fake_ins_for_shelxe(path_ins, cell, sg_number)

    # print 'dictio_phs before start alixe',dictio_phs
    # Call the startALIXE function with the appropiate input
    startALIXEasPHSTAT(clust_fold, reference_hkl, dictio_phs, cell, sg_number, tolerance, resolution, cycles, f_fom)
    print("\n Ending date & time " + time.strftime("%c"))  # Print initial time
