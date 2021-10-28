import zipfile
# open zip file in read mode
with zipfile.ZipFile('SGX4.zip', 'r') as zip:
    # extract files
    zip.extractall('SGX4')
print('Zip File is extracted successfully')


##extract per file
#import zipfile
## open zip file in read mode
#with zipfile.ZipFile('SGX4.zip', 'r') as zip:
#    # extract specific one file
#    zip.extract('test.txt') #nama file yg di dalamnya
#print('Zip File is extracted successfully')