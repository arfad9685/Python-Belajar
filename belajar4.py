#merubah dari satu tipe ke tipe lain (casting)

#integer
print("=====INTEGER=====")
data_int = 9;
print("data = ",data_int,",type=",type(data_int))


data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)#akan false jika nilai int =0

print("data = ",data_float,",type = ",type(data_float))
print("data = ",data_str,",type = ",type(data_str))
print("data = ",data_bool,",type = ",type(data_bool))

#float
print("======FLOAT=====")
data_float=9.5;
print("data = ",data_float,",type=",type(data_float))

data_int = float(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("data = ",data_int,",type = ",type(data_int))
print("data = ",data_str,",type = ",type(data_str))
print("data = ",data_bool,",type = ",type(data_bool))

#boolean
print("======BOOLEAN=====")
data_bool=True;
print("data = ",data_bool,",type=",type(data_bool))

data_int = float(data_bool)
data_str = str(data_bool)
data_bool = bool(data_bool)

print("data = ",data_int,",type = ",type(data_int))
print("data = ",data_str,",type = ",type(data_str))
print("data = ",data_float,",type = ",type(data_float))

#string
print("======STRING=====")
data_str="10";
print("data = ",data_str,",type=",type(data_str))

data_int = int(data_str)
data_float = str(data_str)
data_bool = bool(data_str)

print("data = ",data_int,",type = ",type(data_int))
print("data = ",data_float,",type = ",type(data_float))#string hrs angka
print("data = ",data_bool,",type = ",type(data_bool))


