#tipe data
#angka satuan (integer)
data_integer = 1
print("data : ",data_integer)
print("-bertipe : ",type(data_integer))

data_float=1.5
print("data : ",data_float)
print("tipe =",type(data_float))

data_string = "Arfad"
print("data : ",data_string)
print("tipe =",type(data_string))

data_bool = False
print("data : ",data_bool)
print("tipe =",type(data_bool))

#tipe data khusus
#bilangan kompleks

data_complex = complex(5,6)
print("data : ",data_complex)
print("tipe :",type(data_complex))

#tipe data dr bahasa C

from ctypes import c_double
data_c_double = c_double(5.6)
print("data : ",data_c_double)
print("tipe :",type(data_c_double))






