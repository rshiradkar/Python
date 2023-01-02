import os
import shutil

baseDir = input('Enter dir path: ')
destDir = 'C:/Users/rshirad/OneDrive - Emory University/Kidney_Cabo_project/data'

dirs = os.listdir(baseDir)

for i in dirs[9:]:
    srcDir = os.path.join(baseDir,i)
    dest = os.path.join(destDir,i)
    shutil.copy(srcDir,dest)