import csv
import numpy as np
import glob
import os.path
from keras.utils import to_categorical
import random

class Dataset():
    def __init__(self, seq_length):
        self.seq_length = seq_length

        self.data = self.get_data()
        self.train_data = self.get_train_data()
        self.val_data = self.get_val_data()
        self.test_data = self.get_test_data()
        self.classes = self.get_classes()
        self.videos = self.get_videos()

    def get_data(self):
        with open(os.path.join('data', 'data_file.csv'), 'r') as fin:
            reader = csv.reader(fin)
            data = list(reader)
        return data

    def get_train_data(self):
        train_data = []
        for item in self.data:
            if item[0] == 'train':
                train_data.append(item)
        return train_data

    def get_val_data(self):
        val_data = []
        for item in self.data:
            if item[0] == 'validation':
                val_data.append(item)
        return val_data

    def get_test_data(self):
        test_data = []
        for item in self.data:
            if item[0] == 'test':
                test_data.append(item)
        return test_data

    def get_classes(self):
        classes = []
        for item in self.data:
            if item[1] not in classes:
                classes.append(item[1])
        return classes

    def get_videos(self):
        videos = []
        for item in self.data:
            videos.append(item[2])
        return videos

    @staticmethod
    def return_label(class_name):
        if class_name == 'real':
            return 1
        else:
            return 0

    @staticmethod
    def get_frame_files(item):
        frame_path = os.path.join('data', item[0], item[1])
        video_name = item[2]
        frame_images = glob.glob((os.path.join(frame_path, video_name + '*.jpg')))
        return frame_images

    @staticmethod
    def rescale_list(input_list,size):
        assert len(input_list)>=size
        skip=len(input_list)//size
        output=[input_list[i] for i in range(0,len(input_list),skip)]
        return output[:size]
    
    def frame_generator(self,batch_size,purpose):
        if purpose=='train':
            data=self.train_data
        else:
            data=self.val_data
        print("Creating %s generator with %d samples."%(purpose,len(data)))
        while 1:
            for _ in range(batch_size):
                sample=random.choice(data)
data=Dataset(40)
