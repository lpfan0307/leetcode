def gen_seq(seq, n):
    if len(seq) >= n:
        return 
    print(seq)
    gen_seq(seq + [0], n)
    gen_seq(seq + [1], n)

gen_seq([], 6)