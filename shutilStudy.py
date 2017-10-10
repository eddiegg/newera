import shutil,os, send2trash
with open('./test.txt', 'w') as testfile:
    testfile.write('hello, eddie!')

send2trash.send2trash('./test.txt')
for dir, subdir, files in os.walk('./'):
    print(dir, subdir, files)