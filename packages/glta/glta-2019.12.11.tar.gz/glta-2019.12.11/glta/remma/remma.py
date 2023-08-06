import numpy as np
import pandas as pd
from functools import reduce
import gc
import time
from scipy.stats import chi2

from glta.process_plink.process_plink import read_plink, impute_geno


def remma_add(y, xmat, gmat_lst, var_com, bed_file):
    """
    # 加性检验
    :param y: 表型
    :param xmat: 固定效应设计矩阵
    :param gmat_lst: 基因组关系矩阵列表
    :param var_com: 方差组分
    :param bed_file: plink文件
    :return:
    """
    # 计算V矩阵
    y = np.array(y).reshape(-1, 1)
    n = y.shape[0]
    xmat = np.array(xmat).reshape(n, -1)
    vmat = np.diag([var_com[-1]] * n)
    for val in range(len(gmat_lst)):
        vmat += gmat_lst[val] * var_com[val]
    vmat_inv = np.linalg.inv(vmat)
    # 计算P矩阵
    vxmat = np.dot(vmat_inv, xmat)
    xvxmat = np.dot(xmat.T, vxmat)
    xvxmat = np.linalg.inv(xvxmat)
    pmat = reduce(np.dot, [vxmat, xvxmat, vxmat.T])
    pmat = vmat_inv - pmat
    pymat = np.dot(pmat, y)
    pvpmat = reduce(np.dot, [pmat, vmat, pmat])
    del vmat, vmat_inv, pmat
    gc.collect()
    # 读取SNP文件
    snp_mat = read_plink(bed_file)
    if np.any(np.isnan(snp_mat)):
        print('Missing genotypes are imputed with random genotypes.')
        snp_mat = impute_geno(snp_mat)
    freq = np.sum(snp_mat, axis=0) / (2 * snp_mat.shape[0])
    freq.shape = (1, snp_mat.shape[1])
    snp_mat = snp_mat - 2 * freq
    scale = np.sum(2*freq*(1-freq))
    eff_vec = np.dot(snp_mat.T, pymat)[:, -1] * var_com[0]/scale
    var_vec = np.sum(snp_mat * np.dot(pvpmat, snp_mat), axis=0) * var_com[0] * var_com[0]
    eff_vec_to_fixed = eff_vec * var_com[0]/var_vec
    chi_vec = eff_vec*eff_vec/var_vec
    p_vec = chi2.sf(chi_vec, 1)
    snp_info_file = bed_file + '.bim'
    snp_info = pd.read_csv(snp_info_file, sep='\s+', header=None)
    res_df = snp_info.iloc[:, [0, 1, 3, 4, 5]]
    res_df.columns = ['chro', 'snp_ID', 'pos', 'allele1', 'allele2']
    res_df.loc[:, 'eff_val'] = eff_vec
    res_df.loc[:, 'chi_val'] = chi_vec
    res_df.loc[:, 'eff_val_to_fixed'] = eff_vec_to_fixed
    res_df.loc[:, 'p_val'] = p_vec
    return res_df


def remma_dom(y, xmat, gmat_lst, var_com, bed_file):
    """
    # 显性检验
    :param y: 表型
    :param xmat: 固定效应设计矩阵
    :param gmat_lst: 基因组关系矩阵列表
    :param var_com: 方差组分
    :param bed_file: plink文件
    :return:
    """
    # 计算V矩阵
    y = np.array(y).reshape(-1, 1)
    n = y.shape[0]
    xmat = np.array(xmat).reshape(n, -1)
    vmat = np.diag([var_com[-1]] * n)
    for val in range(len(gmat_lst)):
        vmat += gmat_lst[val] * var_com[val]
    vmat_inv = np.linalg.inv(vmat)
    # 计算P矩阵
    vxmat = np.dot(vmat_inv, xmat)
    xvxmat = np.dot(xmat.T, vxmat)
    xvxmat = np.linalg.inv(xvxmat)
    pmat = reduce(np.dot, [vxmat, xvxmat, vxmat.T])
    pmat = vmat_inv - pmat
    pymat = np.dot(pmat, y)
    pvpmat = reduce(np.dot, [pmat, vmat, pmat])
    del vmat, vmat_inv, pmat
    gc.collect()
    # 读取SNP文件
    snp_mat = read_plink(bed_file)
    if np.any(np.isnan(snp_mat)):
        print('Missing genotypes are imputed with random genotypes.')
        snp_mat = impute_geno(snp_mat)
    freq = np.sum(snp_mat, axis=0) / (2 * snp_mat.shape[0])
    freq.shape = (1, snp_mat.shape[1])
    snp_mat[snp_mat > 1.5] = 0.0
    snp_mat = snp_mat - 2 * freq * (1 - freq)
    eff_vec = np.dot(snp_mat.T, pymat)[:, -1]
    var_vec = np.sum(snp_mat * np.dot(pvpmat, snp_mat), axis=0)
    chi_vec = eff_vec*eff_vec/var_vec
    p_vec = chi2.sf(chi_vec, 1)
    snp_info_file = bed_file + '.bim'
    snp_info = pd.read_csv(snp_info_file, sep='\s+', header=None)
    res_df = snp_info.iloc[:, [0, 1, 3, 4, 5]]
    res_df.columns = ['chro', 'snp_ID', 'pos', 'allele1', 'allele2']
    res_df.loc[:, 'eff_val'] = eff_vec
    res_df.loc[:, 'chi_val'] = chi_vec
    res_df.loc[:, 'p_val'] = p_vec
    return res_df


def remma_epiAA_cpu(y, xmat, gmat_lst, var_com, bed_file):
    """
    加加上位检验
    :param y: 表型
    :param xmat: 固定效应设计矩阵
    :param gmat_lst: 基因组关系矩阵列表
    :param var_com: 方差组分
    :param bed_file: plink文件
    :return:
    """
    # 计算V矩阵
    y = np.array(y).reshape(-1, 1)
    n = y.shape[0]
    xmat = np.array(xmat).reshape(n, -1)
    vmat = np.diag([var_com[-1]] * n)
    for val in range(len(gmat_lst)):
        vmat += gmat_lst[val] * var_com[val]
    vmat_inv = np.linalg.inv(vmat)
    # 计算P矩阵
    vxmat = np.dot(vmat_inv, xmat)
    xvxmat = np.dot(xmat.T, vxmat)
    xvxmat = np.linalg.inv(xvxmat)
    pmat = reduce(np.dot, [vxmat, xvxmat, vxmat.T])
    pmat = vmat_inv - pmat
    pymat = np.dot(pmat, y)
    pvpmat = reduce(np.dot, [pmat, vmat, pmat])
    del vmat, vmat_inv, pmat
    gc.collect()
    # 读取SNP文件
    snp_mat = read_plink(bed_file)
    if np.any(np.isnan(snp_mat)):
        print('Missing genotypes are imputed with random genotypes.')
        snp_mat = impute_geno(snp_mat)
    freq = np.sum(snp_mat, axis=0) / (2 * snp_mat.shape[0])
    freq.shape = (1, snp_mat.shape[1])
    snp_mat = snp_mat - 2 * freq
    # 开始检验
    clock_t0 = time.perf_counter()
    cpu_t0 = time.process_time()
    res_dct = {}
    for i in range(snp_mat.shape[1] - 1):
        epi_mat = snp_mat[:, i:(i+1)] * snp_mat[:, (i+1):]
        eff_vec = np.dot(epi_mat.T, pymat)
        var_vec = np.sum(epi_mat * np.dot(pvpmat, epi_mat), axis=0)
        var_vec = var_vec.reshape(len(var_vec), -1)
        chi_vec = eff_vec * eff_vec / var_vec
        p_vec = chi2.sf(chi_vec, 1)
        res = np.concatenate([np.array([i]*(snp_mat.shape[1]-i-1)).reshape(snp_mat.shape[1]-i-1, -1), np.arange((i+1), snp_mat.shape[1]).reshape(snp_mat.shape[1]-i-1, -1), eff_vec, p_vec], axis=1)
        res_dct[i] = res[res[:, -1] < 1, :]
    clock_t1 = time.perf_counter()
    cpu_t1 = time.process_time()
    print("Running time: Clock time, {:.5f} sec; CPU time, {:.5f} sec.".format(clock_t1 - clock_t0, cpu_t1 - cpu_t0))
    return res_dct


def remma_epiAA_gpu(y, xmat, gmat_lst, var_com, bed_file, snp_lst_0=None, p_cut=0.0001):
    """
    加加上位检验，GPU加速
    :param y: 表型
    :param xmat: 固定效应设计矩阵
    :param gmat_lst: 基因组关系矩阵列表
    :param var_com: 方差组分
    :param bed_file: plink文件
    :param snp_lst_0: 互作对第一个SNP列表
    :param p_cut: 依据阈值保留的互作对
    :return:
    """
    try:
        import cupy as cp
    except Exception as e:
        return e
        # 计算V矩阵
    y = np.array(y).reshape(-1, 1)
    n = y.shape[0]
    xmat = np.array(xmat).reshape(n, -1)
    vmat = np.diag([var_com[-1]] * n)
    for val in range(len(gmat_lst)):
        vmat += gmat_lst[val] * var_com[val]
    vmat_inv = np.linalg.inv(vmat)
    # 计算P矩阵
    vxmat = np.dot(vmat_inv, xmat)
    xvxmat = np.dot(xmat.T, vxmat)
    xvxmat = np.linalg.inv(xvxmat)
    pmat = reduce(np.dot, [vxmat, xvxmat, vxmat.T])
    pmat = vmat_inv - pmat
    pymat = np.dot(pmat, y)
    pvpmat = reduce(np.dot, [pmat, vmat, pmat])
    del vmat, vmat_inv, pmat
    gc.collect()
    # 读取SNP文件
    snp_mat = read_plink(bed_file)
    if np.any(np.isnan(snp_mat)):
        print('Missing genotypes are imputed with random genotypes.')
        snp_mat = impute_geno(snp_mat)
    freq = np.sum(snp_mat, axis=0) / (2 * snp_mat.shape[0])
    freq.shape = (1, snp_mat.shape[1])
    snp_mat = snp_mat - 2 * freq
    # 开始检验
    if snp_lst_0 is None:
        snp_lst_0 = range(snp_mat.shape[1] - 1)
    else:
        if max(snp_lst_0) >= snp_mat.shape[1] - 1 or min(snp_lst_0) < 0:
            print('snp_lst_0 is out of range!')
            exit()
    chi2_cut = chi2.isf(p_cut, 1)
    clock_t0 = time.perf_counter()
    cpu_t0 = time.process_time()
    res_dct = {}
    snp_mat = cp.asarray(snp_mat)
    pymat = cp.asarray(pymat)
    pvpmat = cp.asarray(pvpmat)
    for i in snp_lst_0:
        epi_mat = snp_mat[:, i:(i + 1)] * snp_mat[:, (i + 1):]
        eff_vec = cp.dot(epi_mat.T, pymat)
        var_vec = cp.sum(epi_mat * cp.dot(pvpmat, epi_mat), axis=0)
        var_vec = var_vec.reshape(len(var_vec), -1)
        chi_vec = eff_vec * eff_vec / var_vec
        res = cp.concatenate([cp.array([i] * (snp_mat.shape[1] - i - 1)).reshape(snp_mat.shape[1] - i - 1, -1),
                              cp.arange((i + 1), snp_mat.shape[1]).reshape(snp_mat.shape[1] - i - 1, -1), eff_vec,
                              chi_vec], axis=1)
        res_dct[i] = res[res[:, -1] > chi2_cut, :]
    clock_t1 = time.perf_counter()
    cpu_t1 = time.process_time()
    print("Running time: Clock time, {:.5f} sec; CPU time, {:.5f} sec.".format(clock_t1 - clock_t0, cpu_t1 - cpu_t0))
    return res_dct
