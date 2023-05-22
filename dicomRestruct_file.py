import os
import dicom2nifti
import numpy as np
import pandas

baseDir = input('Enter the cohort path:')
outputDir = 'C:/Users/rshirad/OneDrive - Emory University/Kidney_Cabo_project/Missing Images'

dicom2nifti.convert_directory(baseDir,outputDir)