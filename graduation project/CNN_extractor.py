import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
import numpy as np
from keras.models import Model
from keras.preprocessing import image
from keras.applications.inception_v3 import InceptionV3, preprocess_input


class CNN_Extractor:
    def __init__(self):
        conv_base = InceptionV3(
            weights='imagenet',
            include_top=True
        )

        self.cnn_model = Model(
            inputs=conv_base.input,
            outputs=conv_base.get_layer('avg_pool').output
        )

    def extract_features(self, img_path):
        img = image.load_img(img_path, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        features = self.cnn_model.predict(x)
        features = features[0]
        return features
