#!/bin/sh
blastn -query ../parchment_data_fasta/SG-002_S1_L001_R2_001.fasta -db ../reference_data/cow_reference/cow_reference -num_threads 16 -out ../ref_withY/SG-002_S1_L001_R2_001.csv -outfmt 6 -evalue 1000 -max_hsps 1 -max_target_seqs 1
