import sys
import numpy as np
import scipy.sparse as sp
import pandas as pd
from scipy.sparse.linalg import norm
from scipy.io import loadmat, savemat
from stratipy.nbs_class import Ppi, Patient
from subprocess import call
import os
import glob
import time
import datetime

# NOTE mutationProfileDiffusion -> propagation
# mutationProfile -> M, PPIAdjacencyMatrix -> adj, dataFolder -> result_folder
# PPI_influence_min -> ppi_influence_min, PPI_influence_max-> ppi_influence_max
# PPI_influence()-> calcul_ppi_influence(), PPI_influence -> ppi_influence
# influenceDistance->influence_distance
# influenceMat -> ppi_influence, PPIneighboorsMax -> ngh_max,
# bestInfluencers -> best_influencers
# filteredGenes -> deg0, keepSingletons -> keep_singletons
# mutationsMin -> min_mutation, mutationsMax -> mutationsMax
# newnet -> ppi_ngh, netFinal -> ppi_final, mutFinal -> mut_final
# filteredPatients -> filtered_patients


# @profile
def propagation(M, adj, alpha, tol=10e-6):  # TODO equation, M, alpha
    """Network propagation iterative process

    Iterative algorithm for apply propagation using random walk on a network:
        Initialize::
            X1 = M

        Repeat::
            X2 = alpha * X1.A + (1-alpha) * M
            X1 = X2

        Until::
            norm(X2-X1) < tol

        Where::
            A : degree-normalized adjacency matrix

    Parameters
    ----------
    M : sparse matrix
        Data matrix to be diffused.

    adj : sparse matrix
        Adjacency matrice.

    alpha : float
        Diffusion/propagation factor with 0 <= alpha <= 1.
        For alpha = 0 : no diffusion.
        For alpha = 1 :

    tol : float, default: 10e-6
        Convergence threshold.

    Returns
    -------
    X2 : sparse matrix
        Smoothed matrix.
    """

    n = adj.shape[0]
    # diagonal = 1 -> degree
    # TODO to set diagonal = 0 before applying eye
    adj = adj+sp.eye(n, dtype=np.float32)

    d = sp.dia_matrix((np.array(adj.sum(axis=0))**-1, [0]),
                      shape=(n,  n),
                      dtype=np.float32)
    A = adj.dot(d)

    X1 = M.astype(np.float32)
    X2 = alpha * X1.dot(A) + (1-alpha) * M

    if tol:
        i = 0
        while norm(X2-X1) > tol:
            X1 = X2
            X2 = alpha * X1.dot(A) + (1-alpha) * M
            i += 1
            print(' Propagation iteration = {}  ----- {}'.format(
                i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                  flush=True)
    return X2


# @profile
def compare_ij_ji(ppi, out_min=True, out_max=True):
    """Helper function for calcul_ppi_influence

    In most cases the influence (propagation) is not symmetric. We have to
    compare weight (a_ij) and (a_ji) for all pairs in order to obtain symmetric
    matrix/matrices. 2 choices available: minimum or maximum weight.
        a = min [(a_ij),(a_ji)]
        a = max [(a_ij),(a_ji)]
    Minimum weight is chosen to avoid Hubs phenomenon.

    Parameters
    ----------
    ppi : sparse matrix
        Matrice to apply comparison.

    out_min, out_max : boolean, default: True
        Minimum and/or maximum weight is chosen.

    Returns
    -------
    ppi_min, ppi_max : sparse matrix
        Symmertric matrix with minimum and/or maximum weight.

    Remarks
    -------
    This implements the algorithm described in Vandin, Upfal, Raphael:
    Algorithms for Detecting Significantly Mutated Pathways in Cancer
    - Journal of Computational Biology, 2010, doi: 10.1089/cmb.2010.0265
    """
    # TODO matrice type of ppi
    n = ppi.shape[0]
    ppi = ppi.tolil()  # need "lil_matrix" for reshape
    # transpose to compare ppi(ij) and ppi(ji)
    ppi_transp = sp.lil_matrix.transpose(ppi)
    # reshape to 1D matrix
    ppi_1d = ppi.reshape((1, n**2))
    ppi_1d_transp = ppi_transp.reshape((1, n**2))

    # reshapeto original size matrix after comparison (min/max)
    if out_min and out_max:
        ppi_min = (sp.coo_matrix.tolil(
            sp.coo_matrix.min(sp.vstack([ppi_1d, ppi_1d_transp]), axis=0))
                   ).reshape((n, n)).astype(np.float32)
        ppi_max = (sp.coo_matrix.tolil(
            sp.coo_matrix.max(sp.vstack([ppi_1d, ppi_1d_transp]), axis=0))
                   ).reshape((n, n)).astype(np.float32)
        return ppi_min, ppi_max

    elif out_min:
        ppi_min = (sp.coo_matrix.tolil(
            sp.coo_matrix.min(sp.vstack([ppi_1d, ppi_1d_transp]), axis=0,
                              dtype=np.float32))).reshape((n, n))
        return ppi_min

    elif out_max:
        ppi_max = (sp.coo_matrix.tolil(
            sp.coo_matrix.max(sp.vstack([ppi_1d, ppi_1d_transp]), axis=0,
                              dtype=np.float32))).reshape((n, n))
        return ppi_max
    else:
        print('You have to choice Min or Max')  # TODO change error message


# @profile
def calcul_final_influence(M, adj, result_folder, alpha, influence_weight='min',
                           simplification=True, compute=False, overwrite=False,
                           tol=10e-6):
    """Compute network influence score

    Network propagation iterative process is applied on PPI. (1) The  network
    influence distance matrix and (2) influence matrices based on minimum /
    maximum weight are saved as MATLAB-style files (.mat).
        - (1) : 'influence_distance_alpha={}_tol={}.mat'
                in 'influence_distance' directory
        - (2) : 'ppi_influence_alpha={}_tol={}.mat'
                in 'ppi_influence' directory
    Where {} are parameter values. The directories will be automatically
    created if not exist.

    If compute=False, the latest data of directory will be taken into
    account:
        - latest data with same parameters (alpha and tol)
        - if not exist, latest data of directory but with differents parameters

    Parameters
    ----------
    M : sparse matrix
        Data matrix to be diffused.

    adj : sparse matrix
        Adjacency matrice.

    result_folder : str
        Path to create a new directory for save new files. If you want to creat
        in current directory, enter '/directory_name'. Absolute path is also
        supported.

    influence_weight :

    simplification : boolean, default: True

    compute : boolean, default: False
        If True, new network influence score will be computed.
        If False, the latest network influence score  will be taken into
        account.

    overwrite : boolean, default: False
        If True, new network influence score will be computed even if the file
        which same parameters already exists in the directory.

    alpha : float
        Diffusion (propagation) factor with 0 <= alpha <= 1.
        For alpha = 0 : no diffusion.
        For alpha = 1 :

    tol : float, default: 10e-6
        Convergence threshold.

    Returns
    -------
    final_influence : sparse matrix
        Smoothed PPI influence matrices based on minimum / maximum weight.
    """
    influence_distance_directory = result_folder + 'influence_distance/'
    influence_distance_file = (
        influence_distance_directory +
        'influence_distance_PPI_alpha={}_tol={}.mat'.format(alpha, tol))
    #######
    final_influence_directory = result_folder + 'final_influence/'
    final_influence_file = (
        final_influence_directory +
        'final_influence_PPI_simp={}_alpha={}_tol={}.mat'.format(
            simplification, alpha, tol))
    #######

    existance_same_param = os.path.exists(final_influence_file)
    # TODO overwrite condition
    print("+++++", final_influence_file)
    # check if same parameters file exists in directory
    if existance_same_param:
        final_influence_data = loadmat(final_influence_file)
        if influence_weight == 'min':
            final_influence = final_influence_data['final_influence_min']
        else:
            final_influence = final_influence_data['final_influence_max']
        # print('final influence matrix', type(final_influence), final_influence.shape)
        print(' **** Same parameters file of FINAL INFLUENCE already exists')

    else:
        if compute:
            # check if influence distance file exists
            existance_same_influence = os.path.exists(influence_distance_file)
            print("+++++", influence_distance_file)
            if existance_same_influence:
                influence_data = loadmat(influence_distance_file)
                influence = influence_data['influence_distance']
                print(' **** Same parameters file of INFLUENCE DISTANCE on PPI network already exists')
            else:
                print(' ==== Diffusion over PPI network (it can take approximately 10 min) ==== ')
                influence = propagation(M, adj, alpha, tol)

                # save influence distance before simplification with parameters' values in filename
                os.makedirs(influence_distance_directory, exist_ok=True)  # NOTE For Python ≥ 3.2
                print(' Start to save INFLUENCE DISTANCE (before filtering) ----- {}'
                      .format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                savemat(influence_distance_file,
                        {'influence_distance': influence,
                         'alpha': alpha},
                        do_compression=True)

            # simplification: multiply by PPI adjacency matrix
            if simplification:
                influence = influence.multiply(sp.lil_matrix(adj))
                # -> influence as csr_matrix
            else:
                print("---------- No simplification ----------")
                pass

            final_influence_min, final_influence_max = compare_ij_ji(
                influence, out_min=True, out_max=True)

            # save final influence with parameters' values in filename
            os.makedirs(final_influence_directory, exist_ok=True)

            print(' Start to save FINAL INFLUENCE (after filtering) ----- {}'
                  .format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            savemat(final_influence_file,
                    {'final_influence_min': final_influence_min,
                     'final_influence_max': final_influence_max,
                     'alpha': alpha}, do_compression=True)

            if influence_weight == 'min':
                final_influence = final_influence_min
            else:
                final_influence = final_influence_max

        # take most recent file
        else:
            for x in final_influence_file, influence_distance_directory:
                print(x)
                newest_file = max(glob.iglob(x + '*.mat'),
                                  key=os.path.getctime)
                final_influence_data = loadmat(newest_file)
                if x == final_influence_directory:
                    if influence_weight == 'min':
                        final_influence = final_influence_data['final_influence_min']
                    else:
                        final_influence = final_influence_data['final_influence_max']
    return final_influence


# @profile
def best_neighboors(ppi_filt, final_influence, ngh_max):
    """Helper function for filter_ppi_patients

    Keeps only the connections with the best influencers.

    Parameters
    ----------
    ppi_filt : sparse matrix
        Filtration from ppi_total : only genes in PPI are considered.

    final_influence :
        Smoothed PPI influence matrices based on minimum or maximum weight.

    ngh_max : int
        Number of best influencers in PPI.

    Returns
    -------
    ppi_ngh : sparse matrix
        PPI with only best influencers.
    """
    ngh_max = ngh_max + 1  # central protein included
    final_influence = final_influence.todense()
    ppi_filt = ppi_filt.todense()
    ppi_ngh = np.zeros(ppi_filt.shape, dtype=np.float32)
    for i in range(ppi_filt.shape[0]):
        best_influencers = np.argpartition(-final_influence[i, :], ngh_max)
        best_influencers = np.asarray(best_influencers).squeeze()[:ngh_max]
        #NOTE different result if same value exists several times
        ppi_ngh[i, best_influencers] = ppi_filt[i, best_influencers]
    ppi_ngh = np.max(np.dstack((ppi_ngh, ppi_ngh.T)), axis=2)
    # too stringent if np.min
    return sp.csc_matrix(ppi_ngh)


# @profile
def filter_ppi_patients(result_folder, influence_weight, simplification, alpha, tol, ppi_total,
                        mut_total, ppi_filt, final_influence, ngh_max,
                        keep_singletons=False, min_mutation=0, max_mutation=2000):
    """Keeping only the connections with the best influencers and Filtering some
    patients based on mutation number

    'the 11 most influential neighbors of each gene in the network as
    determined by network influence distance were used'
    'Only mutation data generated using the Illumina GAIIx platform were
    retained for subsequent analy- sis, and patients with fewer than 10
    mutations were discarded.'

    Parameters
    ----------
    ppi_total : sparse matrix
        Built from all sparse sub-matrices (AA, ... , CC).

    mut_total : sparse matrix
        Patients' mutation profiles of all genes (rows: patients,
        columns: genes of AA, BB and CC).

    ppi_filt : sparse matrix
        Filtration from ppi_total : only genes in PPI are considered.

    final_influence :
        Smoothed PPI influence matrices based on minimum or maximum weight.

    ngh_max : int
        Number of best influencers in PPI.

    keep_singletons : boolean, default: False
        If True, proteins not annotated in PPI (genes founded only in patients'
        mutation profiles) will be also considered.
        If False, only annotated proteins in PPI will be considered.

    min_mutation, max_mutation : int
        Numbers of lowest mutations and highest mutations per patient.

    Returns
    -------
    ppi_final, mut_final : sparse matrix
        PPI and mutation profiles after filtering.
    """
    ppi_final_directory = result_folder + 'final_influence/'
    ppi_final_file = (
        ppi_final_directory +
        'PPI_final_weight={}_simp={}_alpha={}_tol={}_singletons={}_ngh={}.mat'
        .format(influence_weight, simplification, alpha, tol, keep_singletons,
                ngh_max))

    existance_same_param = os.path.exists(ppi_final_file)
    if existance_same_param:
        ppi_final_data = loadmat(ppi_final_file)
        ppi_final = ppi_final_data['ppi_final']
        print(' **** Same parameters file of PPI FINAL already exists')
        if keep_singletons:
            mut_final = mut_total
        else:
            mut_final = mut_total[:, Ppi(ppi_total).deg > 0]
    else:
        ppi_ngh = best_neighboors(ppi_filt, final_influence, ngh_max)
        deg0 = Ppi(ppi_total).deg == 0  # True if protein degree = 0

        if keep_singletons:
            ppi_final = sp.bmat([
                [ppi_ngh, sp.csc_matrix((ppi_ngh.shape[0], sum(deg0)))],
                [sp.csc_matrix((sum(deg0), ppi_ngh.shape[0])),
                 sp.csc_matrix((sum(deg0), sum(deg0)))]
                ])  # -> COO matrix
            # mut_final=sp.bmat([[mut_total[:,deg0==False],mut_total[:,deg0==True]]])
            mut_final = mut_total
        else:
            ppi_final = ppi_ngh
            mut_final = mut_total[:, Ppi(ppi_total).deg > 0]

        savemat(ppi_final_file, {'ppi_final': ppi_final}, do_compression=True)

    # to avoid worse comparison '== False'
    mut_final = mut_final[np.array([min_mutation <= k <= max_mutation for k in
                                    Patient(mut_final).mut_per_patient])]

    print(" Removing %i patients with less than %i or more than %i mutations" %
          (mut_total.shape[0]-mut_final.shape[0], min_mutation, max_mutation))

    return ppi_final, mut_final


def quantile_norm_mean(df):
    """Helper function for propagation_profile

    Forces the observations/variables to have identical intensity distribution.

    Parameters
    ----------

    Returns
    -------

    """
    if not isinstance(df, pd.DataFrame):
        df = pd.DataFrame(df)
    rank_mean = df.stack().groupby(df.rank(method='first').stack().astype(int)).mean()
    df_norm = df.rank(method='min').stack().astype(int).map(rank_mean).unstack()
    return df_norm.values


def quantile_norm_median(df):
    """Helper function for propagation_profile

    Forces the observations/variables to have identical intensity distribution.

    Parameters
    ----------

    Returns
    -------

    """
    if not isinstance(df, pd.DataFrame):
        df = pd.DataFrame(df)
    rank_median = df.stack().groupby(df.rank(method='first').stack().astype(int)).median()
    df_norm = df.rank(method='min').stack().astype(int).map(rank_median).unstack()
    return df_norm.values


def propagation_profile(mut_raw, adj, result_folder, alpha, tol, mut_type):
    #  TODO error messages
    final_influence_mutation_directory = result_folder + 'final_influence/'
    final_influence_mutation_file = (
        final_influence_mutation_directory +
        'final_influence_mutation_profile_{}_alpha={}_tol={}.mat'.format(
            mut_type, alpha, tol))
    existance_same_param = os.path.exists(final_influence_mutation_file)
    if existance_same_param:
        final_influence_data = loadmat(final_influence_mutation_file)
        mut_propag = final_influence_data['mut_propag']
        print(' **** Same parameters file of FINAL INFLUENCE on Mutation Profile already exists')

    else:
        if mut_type == 'raw':
            mut_propag = mut_raw.todense()
        else:
            print(' ==== Diffusion over mutation profile ==== ')
            mut_propag = propagation(mut_raw, adj, alpha, tol).todense()
            mut_propag[np.isnan(mut_propag)] = 0
            if mut_type == 'mean_qn':
                mut_propag = quantile_norm_mean(mut_propag)
            elif mut_type == 'median_qn':
                mut_propag = quantile_norm_median(mut_propag)

        savemat(final_influence_mutation_file,
                    {'mut_propag': mut_propag,
                     'alpha': alpha}, do_compression=True)

    return mut_propag


def filtering(ppi_filt, result_folder, influence_weight, simplification,
              compute, overwrite, alpha, tol, ppi_total, mut_total, ngh_max,
              keep_singletons, min_mutation, max_mutation, mut_type):
    final_influence = (calcul_final_influence(
        sp.eye(ppi_filt.shape[0], dtype=np.float32), ppi_filt, result_folder,
        alpha, influence_weight, simplification, compute, overwrite, tol))

    ppi_final, mut_final = filter_ppi_patients(
        result_folder, influence_weight, simplification, alpha, tol, ppi_total,
        mut_total, ppi_filt, final_influence, ngh_max, keep_singletons,
        min_mutation, max_mutation)

    mut_propag = propagation_profile(
        mut_final, ppi_filt, result_folder, alpha, tol, mut_type)

    return ppi_final, mut_propag
