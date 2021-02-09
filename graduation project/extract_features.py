import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import numpy as np
import os.path
from tqdm import tqdm
from data import Dataset
from CNN_extractor import CNN_Extractor

seq_length=60
data=Dataset(seq_length)
cnn_model=CNN_Extractor()
bar=tqdm(total=len(data.data))

for item in data.data:
    path=os.path.join('data','features',item[2]+'-'+'features')

    if os.path.isfile(path+'.npy'):
        bar.update(1)
        continue

    frames=data.get_frame_files(item)
    frames=data.rescale_list(frames,seq_length)

    sequence=[]
    for image in frames:
        features=cnn_model.extract_features(image)
        sequence.append(features)
    np.save(path,sequence)
    bar.update(1)

bar.close()


