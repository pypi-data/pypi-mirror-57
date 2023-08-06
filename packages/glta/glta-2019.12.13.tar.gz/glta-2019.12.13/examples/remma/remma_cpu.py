import pandas as pd
import numpy as np
from scipy.stats import chi2
import logging
from glta.gmat import agmat, dgmat_as
from glta.uvlmm import wemai_multi_gmat
from glta.remma import remma_add, remma_epiAA_cpu, remma_epiAA_eff_cpu, remma_epiAA_select_cpu


bed_file = '../data/plink'
df = pd.read_csv("../data/pheno", header=None, sep='\s+')

y = np.array(df.iloc[:, -1:])
xmat = np.array(df.iloc[:, 2:-1])

logging.basicConfig(level=logging.INFO)

agmat_lst = agmat(bed_file, inv=True, small_val=0.001, out_fmt='mat')

gmat_lst = [agmat_lst[0], agmat_lst[0]*agmat_lst[0]]

var_com = wemai_multi_gmat(y, xmat, gmat_lst, init=None, maxiter=100, cc=1.0e-8)

res_add = remma_add(y, xmat, gmat_lst, var_com, bed_file, out_file='remma_add')

res_epiAA_cpu = remma_epiAA_cpu(y, xmat, gmat_lst, var_com, bed_file, snp_lst_0=None, p_cut=1, out_file='remma_epiAA_cpu')
p_vec = chi2.sf(res_epiAA_cpu[:, -1], 1)

res_epiAA_eff_cpu = remma_epiAA_eff_cpu(y, xmat, gmat_lst, var_com, bed_file, snp_lst_0=None, eff_cut=-999.0, out_file='remma_epiAA_eff_cpu')

res_epiAA_select_cpu = remma_epiAA_select_cpu(y, xmat, gmat_lst, var_com, bed_file, snp_lst_0=None, snp_lst_1=None, p_cut=1.0, out_file='remma_epiAA_select_cpu')

