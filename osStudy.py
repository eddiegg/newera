import os,random
print(os.path.abspath('C:\\Users\\user\\Desktop\\跑团\\文章.txt'))
print(os.path.basename('C:\\Users\\user\\Desktop\\跑团\\文章.txt'))
print(os.path.dirname('C:\\Users\\user\\Desktop\\跑团\\文章.txt'))
print(os.path.realpath('C:\\Users\\user\\Desktop\\跑团\\文章.txt'))
print(os.path.relpath('C:\\Users\\user\\Desktop\\跑团\\文章.txt','C:\\Users\\user\\'))

for dirpath,dirnames,files in os.walk("E:\\"):
    # print("current dir is: "+dirpath)
    # for dirname in dirnames:
    #     print("sub dir of "+dirpath+" is: "+dirname)
    for file in files:
        if file.endswith('.pdf'):
            print("pdf file found with name: "+file)
            print(dirpath)
