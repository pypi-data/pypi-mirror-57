#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <omp.h>

int read_plink_bed(char *bed_file, long num_id, long num_snp, double *marker_mat);
int print_out(long i, long *snp_lst_0, long num_snp, long num_id, double *marker_mat, double *pymat, double eff_cut, FILE *out_res);
int remma_epiAA_eff_cpu(char *bed_file, long num_id, long num_snp, 
     long *snp_lst_0, long len_snp_lst_0, double *pymat, double eff_cut, char* out_file)
{
	//标记矩阵声明空间
	double *marker_mat = (double*) calloc(num_id*num_snp, sizeof(double));
	read_plink_bed(bed_file, num_id, num_snp, marker_mat);
	
	//标记矩阵中心化，-2p 
	long i = 0, j = 0;
    double pFreq = 0.0;// frequence of one allele for each SNP
    //double scale = 0;// scale factor
    for(i = 0; i < num_snp; i++){
      	pFreq = 0;
      	for(j = 0; j < num_id; j++){    		
	      	pFreq +=  marker_mat[i*num_id+j]/(2*num_id);			   
        }
        for(j = 0; j < num_id; j++){      	
        	marker_mat[i*num_id+j] -= 2*pFreq; 	
        }
        //scale += 2*pFreq*(1-pFreq);
    }
    
    FILE *out_res = fopen(out_file, "w");
	if(out_res==NULL){
		printf("Fail to build the output file.\n");
		exit(1);
	}
	
	#pragma omp parallel for
	for(i = 0; i < len_snp_lst_0; i++){
		//printf("%ld %ld ", i, snp_lst_0[i]);
		print_out(i, snp_lst_0, num_snp, num_id, marker_mat, pymat, eff_cut, out_res);
	}
	fclose(out_res);   
	return 1;
}

int print_out(long i, long *snp_lst_0, long num_snp, long num_id, double *marker_mat, double *pymat, double eff_cut, FILE *out_res) {
	long j=0, k=0;
	double epi_effect=0.0;
	for(j = snp_lst_0[i]+1; j < num_snp; j++){
		epi_effect = 0.0;
	    for(k = 0; k < num_id; k++){
			epi_effect += marker_mat[snp_lst_0[i]*num_id + k] * marker_mat[j*num_id + k] * pymat[k];
		}
		if(epi_effect >= eff_cut || epi_effect	<= -eff_cut){
        	fprintf(out_res, "%ld %ld %g\n", snp_lst_0[i], j, epi_effect);
    	}
	}
	return 0;
}


int read_plink_bed(char *bed_file, long num_id, long num_snp, double *marker_mat)
{
	
	//打开bed file
	char in_file[1000];
	strcpy(in_file, bed_file);
	strcat(in_file, ".bed");
	FILE *fin_bed = fopen(in_file, "r");
	if(fin_bed==NULL){
		printf("Fail to open the plink bed file: %s.\n", in_file);
		exit(1);
	}
	
	//读取文件
	long num_block = num_id/4 + 1; //存储一个位点所有SNP占据的block（一个字节），每个字节可存储4个SNP 
	long num_snp_last = num_id % 4; //最后一个block存储的SNP数 
	if(num_snp_last == 0){
		num_snp_last = 4;
		num_block = num_block - 1;
	}
	
	//按顺序读取每个字节
	long i = 0, m = 0, k = 0;
	char x03 = '3' - 48;
	unsigned char one_byte;
	int code_val;
	fseek(fin_bed, 3, SEEK_SET); //跳过开头三个字节 
	while(fread(&one_byte, sizeof(char), 1, fin_bed) == 1){
		i++;
		if(i % num_block != 0){
			for(m = 0; m < 4; m++){
				code_val = (one_byte >> (2*m)) & x03;
				marker_mat[k++] = (code_val*code_val + code_val)/6.0;
			}
		}
		else{
			for(m = 0; m < num_snp_last; m++){
				code_val = (one_byte >> (2*m)) & x03;
				marker_mat[k++] = (code_val*code_val + code_val)/6.0;
			}
		}
		
	}
	fclose(fin_bed);
	fin_bed=NULL;
	return 1;
}




