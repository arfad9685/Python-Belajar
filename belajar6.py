#operasi aritmatika

a = 10
b = 3

hasil = a + b
print(a,'+',b,'=',hasil)


#operasi eksponen (pangkat)
hasil = a ** b
print(a,'**',b,'=',hasil)

#operasi modulus
hasil = a % b
print(a,'%',b,'=',hasil)

#operasi floor division
hasil = a // b
print(a,'//',b,'=',hasil)

#priotitas operasi,
'''
    1. ()
    2. exponen
    3. perkalian dkk
    4. pertambahan
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**', y,'*',z,'+', x, '/', y,'-',y,'% ',z,'//', x,'=',hasil)

hasil = x + y * z
print(x, '+', y, '*', z,'=',hasil)

hasil = (x + y) * z
print('(',x, '+', y,') *', z,'=',hasil)



