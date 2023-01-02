import os
import dicom2nifti
import numpy as np
import pandas

baseDir = input('Enter the cohort path:')
outputDir = 'C:/Users/rshirad/OneDrive - Emory University/Kidney_Cabo_project/restructured'

patients = os.listdir(baseDir)

for patient in patients:
    patientPath = os.path.join(baseDir,patient)
    patDir = os.path.join(outputDir,patient)
    os.mkdir(patDir)
    timePoints = os.listdir(patientPath)
    foldNum = 0

    for timeP in timePoints:
        tpDir = os.path.join(patDir,'timePoint' + str(foldNum))
        os.mkdir(tpDir)
        sequencesPath = os.path.join(patientPath,timeP)
        sequences = os.listdir(sequencesPath)

        for seq in sequences:
            sequencePath = os.path.join(sequencesPath,seq)
            print(os.path.isdir(sequencePath))
            dicom2nifti.convert_directory(sequencePath,tpDir)

        foldNum += 1

    del foldNum

