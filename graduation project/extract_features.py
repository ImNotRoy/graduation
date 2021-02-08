import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import numpy as np
import os.path
from tqdm import tqdm
from data import Dataset
from CNN_extractor import CNN_Extractor

seq_length=60
data=Dataset(seq_length)
