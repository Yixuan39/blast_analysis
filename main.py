import os

if __name__ == '__main__':
    reference = '../../referenceFiles/GCA_021347905.1_ARS-LIC_NZ_Holstein-Friesian_1_genomic.fna'
    reference_out = '../reference_data/cow_reference/cow_reference'
    input_folder = 'parchment_data_fasta'
    format = '.fasta'
    files = os.listdir(input_folder)
    names = [file.replace(format, '') for file in files if format in file]
    output_folder = 'ref_withY2'
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(output_folder+'_commands', exist_ok=True)
    with open(output_folder+'_commands/run.sh', 'w') as new:
        new.write('makeblastdb -in '+ reference +' -dbtype nucl -out ' + reference_out + '\n')
        for name in names:
            new.write('sbatch -c 16 ' + name + '.sh\n')
        new.close()
    for name in names:
        with open(output_folder+'_commands/' + name + '.sh', 'w') as new:
            new.write('#!/bin/sh\n')
            new.write('blastn -query ../' + input_folder + '/' + name + format +
                      ' -db '+ reference_out +' -num_threads 16 -out ../' + output_folder
                      + '/' + name + '.csv -outfmt 6 -evalue 1000 -max_hsps 1 -max_target_seqs 1\n')
            new.close()
