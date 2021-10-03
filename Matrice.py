A=[[1,2,3,4,5],
  [6,7,8,9,10],
  [11,12,13,14,15],
  [16,17,18,19,20],
  [21,22,23,24,25]]

Dp=A[0][0]+A[1][1]+A[2][2]+A[3][3]+A[4][4]
Ds=A[0][4]+A[1][3]+A[2][2]+A[3][1]+A[4][0]
print('Diagonala principala',Dp)
print('Diagonala secundara',Ds)
for i in A:
    print('Suma elementelor de pe fiecare rand=', sum(i))
j=0
suma=0
for j in range(5):
    for i in A:
        suma+=i[j]
    print('Suma elementelor pe coloana=',suma)


