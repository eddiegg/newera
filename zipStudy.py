import zipfile

# with zipfile.ZipFile('./test/ziptt.zip', 'w') as zz:
#     zz.write('./pw.py', compress_type=zipfile.ZIP_DEFLATED)
#
# with zipfile.ZipFile('./test/ziptt.zip', 'a') as zz:
#     zz.write('./test/tt.txt', compress_type=zipfile.ZIP_DEFLATED)

with zipfile.ZipFile('./test/ziptt.zip') as zz:
    print(zz.namelist())
    print(zz.getinfo('test/tt.txt'))
    print(zz.getinfo('test/tt.txt').file_size)
    print(zz.getinfo('test/tt.txt').compress_size)
    # zz.extractall('./extracted/')
    zz.extract('pw.py', './extracted/')
