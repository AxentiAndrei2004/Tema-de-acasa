Numere_zecimale=[0,1,2,3,4,5,6,7,8,9]
cod=[['0000','0001','0011','0010','0110','0111','0101','0100','1100','1101'],
    ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001'],
    ['0000','0001','0010','0011','0100','1011','1100','1101','1110','1111'],
    ['0011','0100','0101','0110','0111','1000','1001','1010','1011','1100']]   
a=int(input('Introduceti denumirea codului numeric='))
if a=='Gray':
    print('Numerele zecimale',cod[0])
elif a=='Direct':
    print('Numerele zecimale', cod[1])
elif a=='Aiken':
    print('Numerele zecimale', cod[2])
elif a=='Exces 3':
    print('Numerele zecimale', cod[3])

