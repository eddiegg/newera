import shutil,os, send2trash
with open('./test.txt', 'w') as testfile:
    testfile.write('hello, eddie!')

send2trash.send2trash('./test.txt')
for dir, subdirs, files in os.walk('./'):
    print('current dir is: ' + dir)

    for subdir in subdirs:
        print('sub folder of ' + dir + ' is: ' + subdir)

    for file in files:
        print('file inside ' + dir + ': ' + file)