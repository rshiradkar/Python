# Define libraries

import pathlib
import dicom2nifti
import medpy
import shutil
import numpy as np
import pydicom as pd
import matplotlib.pyplot as plt

from os import listdir, mkdir
from os.path import exists, isfile, join
from medpy_apparent_diffusion_coefficient_rs import adcCalc

path = 'G:\\.shortcut-targets-by-id\\1i32rnNPsd6afsr-jYRpOVjPThWJ9aChs\\StVincent\\Data\\19410514\\20150831\\DWI-3b-Ax-FOLD-OVER-SWAPED\\701'
nPath = 'C:\\Temp'


files = listdir(path)
files.sort()
dcmExt = '.dcm'
# files = files[1:len(files)]
if pathlib.Path(files[0]).suffix != dcmExt:
    del files[0]

# organize files by b-values
numFiles = len(files)
filesPerSet = numFiles/3
j=0

for j in range(3):

    temp = pd.dcmread(path+'\\'+files[j*int(filesPerSet)])
    dest = path+'\\'+'b'+str(int(temp.DiffusionBValue))
    mkdir(dest)

    for i in range(filesPerSet):
        shutil.copy(path+'\\'+files[int(j*filesPerSet)+i],dest)


# I1 = pd.dcmread(path+'\\'+files[i])
# I2 = pd.dcmread(path+'\\'+files[i+int(filesPerSet)])

# convert dicom to nifti
bvals = [0,800,1500]
tPath = 'C:\\Temp\\DWI'
dicom2nifti.dicom_series_to_nifti((tPath+'\\'+'b0'),(tPath+'\\b0.nii.gz'))
dicom2nifti.dicom_series_to_nifti((tPath+'\\'+'b800'),(tPath+'\\b800.nii.gz'))
dicom2nifti.dicom_series_to_nifti((tPath+'\\'+'b1500'),(tPath+'\\b1500.nii.gz'))

tPath = 'C:\\Temp\\DWI'

adcCalc((tPath+'\\b0.nii.gz'),(tPath+'\\b800.nii.gz'),800,(tPath+'\\ADC_800.nii.gz'),0)
adcCalc((tPath+'\\b0.nii.gz'),(tPath+'\\b1500.nii.gz'),1500,(tPath+'\\ADC_1500.nii.gz'),0)