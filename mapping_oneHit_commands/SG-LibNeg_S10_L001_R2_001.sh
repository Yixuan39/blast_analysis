#!/bin/sh
blastn -query ../parchment_data_fasta/SG-LibNeg_S10_L001_R2_001.fasta -db ../reference_data/cow_reference/GCA_000003055.5_Bos_taurus_UMD_3.1.1_genomic.fna -num_threads 8 -out ../mapping_oneHit/SG-LibNeg_S10_L001_R2_001.csv -outfmt 6 -task megablast -max_hsps 1 -max_target_seqs 1
