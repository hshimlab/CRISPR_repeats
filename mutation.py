def identify_mutation(seq1, seq2):

    # initialise hamming distance counter
    hamming_distance = 0
    pos_of_mutation = []

    # iterating over each nucleotide in two DNA sequences
    for i, letter in enumerate(seq1):
        # if they are not the same, add 1 to hamming distance
        if letter != seq2[i]:
            hamming_distance += 1
            pos_of_mutation.append(i+1)
    return hamming_distance, pos_of_mutation