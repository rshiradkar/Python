import scipy
import pandas as pd
import os
from scipy.io import loadmat

path = 'G:\\.shortcut-targets-by-id\\1YKJmC9bzTUqncCWUJdAy3ZSVLcEt10UD\\KiTS Project\\TextureFeatures\\FullRing\\0-3mm'

dir_list = os.listdir(path)

features = loadmat(os.path.join(path,dir_list[0]))

feature_keys = features.keys()

feats_df = pd.DataFrame(features['patientFeats'])

print(feats_df)
