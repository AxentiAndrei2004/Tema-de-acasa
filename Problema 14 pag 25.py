n=int(input('Introduceti de la tastatura un tablou patratic cu n linii='))
C=[[int(input()) for i in range(n)] for j in range(n)]
S1=0
for i in range(0,len(C)):
    S1+=[i][i]
S2=0
for i in range(0,len(C)):
    S2+=C[len(C)-i-1][i]
print('Suma coponentelor de pe diagonala principala',S1)
print('Suma coponentelor de pe diagonala secundara',S2)
S3=0
S4=0
for i in range(0,n):
    for j in range(0,n):
        if i<j:
            S3+=C[i][j]
        if i>j:
            S4+=C[i][j]
print('Suma componentelor mai sus de diagonala principala',S3)
print('Suma componentelor mai jos de diagonala principala',S4)
S5=0
S6=0
for i in range(0,n):
    for j in range(0,n):
        if (i+j)<(n+1):
            S5+=C[i][j]
        if (i+j)>(n+1):
            S6+=C[i][j]
print('Suma componentelor mai de diagonala principala ',S5)
print('Suma componentelor mai jos de diagonala secundara',S6)