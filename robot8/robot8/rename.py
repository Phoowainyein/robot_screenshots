import os

path=os.chdir('robot9/robot9')
i = 0
for file in os.listdir(path):
    new_file_name ="robot9_{}.jpg".format(i)
    os.rename(file,new_file_name)
    i=i+1
