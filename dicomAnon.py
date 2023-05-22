import pydicom as pd
import os
import numpy as np
from pathlib import Path
from dicomanonymizer import anonymize_dicom_file
import matplotlib.pyplot as plt
from collections import defaultdict

data_folder = Path("C:/temp/data/patient1")
data_op_folder = Path("C:/temp/anon_data")

files = os.listdir(data_folder)
for file in files:
    if file[-4:] == '.dcm':
        filePath = data_folder / file
        dcmFile = pd.dcmread(filePath)
        img = dcmFile.pixel_array
        nRows, nCols = img.shape
        tagName = file + ".tag"
        tagfilePath = data_folder / tagName

        mask = np.zeros((nRows,nCols))

        unique_val = defaultdict(int)
        with open(tagfilePath, 'rb') as f:
            byte = f.read(1)
            result = ''
            while byte != b'\x0C':
                result += byte.decode('ascii')
                byte = f.read(1)
            for i in range(nRows):
                for j in range(nCols):
                    if ord(byte) != 0:
                        mask[j][i] = ord(byte)
                    byte = f.read(1)

        # plt.imshow(mask, cmap=plt.cm.gray)
        # plt.colorbar()
        # plt.show()
        dcmFile.PixelData = mask.tobytes()
        dcmFile.save_as(data_op_folder / 'out.dcm')
    
# print(type(mask))
# print(type(dcmFile.pixel_array))
# anonymize_dicom_file(filePath,file_op_path)

# print(op_file_name)