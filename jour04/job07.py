def numdiv(L,n):
    i = 0
    for x in L:
        if ( x%n == 0):
            i = i + 1
    return i
n=3
L = [8, 24, 48, 2, 16]
print("Le nombre de multiples de 3 présents dans la liste L sont", numdiv(L,n))