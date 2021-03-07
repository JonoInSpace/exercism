def distance(strand_a, strand_b):
    count = 0
    if strand_a == '':
        if strand_b == '': return 0
        else:
            raise ValueError('Strands must not be empty!')
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands do not have the same length!')
    else:
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                count +=1
        return count