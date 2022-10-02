import os

if __name__ == '__main__':
    reference = './reference_data/cow_reference/GCA_000003055.5_Bos_taurus_UMD_3.1.1_genomic.fna'
    input_folder = 'parchment_data_fasta'
    format = '.fasta'
    files = os.listdir(input_folder)
    names = [file.replace(format, '') for file in files if format in file]
    output_folder = 'mapping_oneHit'
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(output_folder+'_commands', exist_ok=True)
    with open(output_folder+'_commands/run.sh', 'w') as new:
        new.write('makeblastdb -in .'+ reference +' -dbtype nucl\n')
        for name in names:
            print()
            new.write('sbatch -c 8 ' + name + '.sh\n')
        new.close()
    for name in names:
        with open(output_folder+'_commands/' + name + '.sh', 'w') as new:
            new.write('#!/bin/sh\n')
            new.write('blastn -query ../' + input_folder + '/' + name + format +
                      ' -db .'+ reference +' -num_threads 8 -out ../' + output_folder
                      + '/' + name + '.csv -outfmt 6 -task megablast -max_hsps 1 -max_target_seqs 1\n')
            new.close()

