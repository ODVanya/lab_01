A = int(input())
B = int(input())
def EVC(A, B):
    while A != 0 and B != 0:
        if A >= B:
            A %= B
        else:
            B %= A
    return A or B
print(EVC(A,B))