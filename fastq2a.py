import os

if __name__ == '__main__':
    input_folder = './parchment_data'
    output_folder = input_folder + '_fasta'
    os.makedirs(output_folder, exist_ok=True)
    names = os.listdir(input_folder)
    with open('convert_fastq.sh', 'w') as new:
        for name in names:
            new.write('seqtk seq -A ' + input_folder + '/' + name +
                      ' > ' + output_folder + '/' + name.replace('fastq', 'fasta') + '\n')
    os.system('bash convert_fastq.sh')