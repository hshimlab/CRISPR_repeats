from Bio import SeqIO

file = 'Class1_IA.fa'
open_file = list(SeqIO.parse(open(file), 'fasta'))


labels = list(str(label.id) for label in open_file)
seqs = list(str(seq.seq) for seq in open_file)


labelled_file = open('{}'.format(file.removesuffix('.fa')) + '_labelled.fa', 'w')

prev_name = labels[0]
repeat_counter = 1
pos = 0
read = '>' + labels[0] + '_1' + '\n'
read += seqs[0] + '\n'

for description, sequence in zip(labels[1:], seqs[1:]):


    if description == prev_name:
        repeat_counter += 1
    
        read += '>' + description + '_{}'.format(repeat_counter) +'\n'
        read += sequence + '\n'
        pos += 1

    else:
        repeat_counter = 1
        read += '>' + description + '_{}'.format(repeat_counter) + '\n'
        read += sequence + '\n'
        
        pos += 1
        prev_name = labels[pos]

labelled_file.write(read)
labelled_file.close()
print(read)
