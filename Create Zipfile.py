import zipfile
# create open zip file in write mode
with zipfile.ZipFile('SGX4.zip', 'w') as zip:
    # write files to a zip file
    zip.write('SGX1.pdf') #masukkan jenis file
    zip.write('SGX2.pdf')
print('Zip File is created successfully')