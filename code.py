def superDigit(n, k):
    P = str((sum([int(i) for i in n])*k))
    return superDigit(P,1) if len(P) != 1 else P






