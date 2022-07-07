import collageradiomics
import pydicom
import numpy as np
import SimpleITK as sitk
import matplotlib.pyplot as plt
import nibabel as nib
import os
import time
from matplotlib.patches import Rectangle
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle
from mpl_toolkits.axes_grid1 import make_axes_locatable

data_path_loc = "G:\\My Drive\\MRI_data_prostate\\nifti\\ProstateX-0000"

T2path = os.path.join(data_path_loc,"T2W.nii.gz")
LSpath = os.path.join(data_path_loc,"LS1.nii.gz")

T2 = nib.load(T2path)
T2 = np.array(T2.dataobj)

LS = nib.load(LSpath)
LS = np.array(LS.dataobj)

# for i in range(LS.shape[2]):
#     temp = LS[:,:,i]
#     temp = temp.sum(axis=1)
#     temp = temp.sum(axis=0)
#     temp = temp.reshape(-1)
#     print(temp)

T2_ = T2[:,:,8]
LS_ = LS[:,:,8]



collage = collageradiomics.Collage(T2_,LS_)
full_image = collage.execute()

inds = np.where(LS_ == 1)


# print(full_image[np.array(inds[0]), np.array(inds[1]),0])

# print(full_image.shape)
collageFeats = []
for i in range(full_image.shape[2]):
    tempFeat = full_image[np.array(inds[0]), np.array(inds[1]),i]
    tempFeat = tempFeat.reshape(-1)
    # print(np.shape(tempFeat.reshape(1,-1)))
    collageFeats.append(tempFeat.tolist())

collageFeats = np.array(collageFeats)
print(collageFeats.shape)