import numpy as np
import os.path
from data import Dataset
from CNN_extractor import CNN_Extractor

seq_length=60
data=Dataset(seq_length)

print(data.train_data)
