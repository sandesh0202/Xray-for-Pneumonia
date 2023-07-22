from xray.constants import *
import os
import tensorflow as tf
import numpy as np
import cv2
from pathlib import Path
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense, Dropout, BatchNormalization, Flatten
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
from xray.entity.config_entity import TrainingConfig

class Training:
    def __init__(self, config: TrainingConfig) -> None:
        self.config = config
        
    def get_training_data(self, data_dir):
        image_size = self.config.params_image_size
        labels = self.config.params_label
        data = []
        for label in labels:
            path = os.path.join(data_dir, label)
            class_num = labels.index(label)
            
            for image in os.listdir(path):
                try:
                    img_array = cv2.imread(os.path.join(path,image))
        
                    resized_arr = cv2.resize(img_array, (image_size, image_size))
                    data.append([resized_arr, class_num])
                except Exception as e:
                    print(e)
                    
        return np.array(data)
    
    def process_data(self):
        train_data = self.get_training_data('artifacts/data_ingestion/chest_xray/chest_xray/train')
        test_data = self.get_training_data('artifacts/data_ingestion/chest_xray/chest_xray/test')
        val_data = self.get_training_data('artifacts/data_ingestion/chest_xray/chest_xray/val')

        X_train, y_train = self.process_data_helper(train_data)
        X_test, y_test = self.process_data_helper(test_data)
        X_val, y_val = self.process_data_helper(val_data)

        X_train = X_train / 255
        X_test = X_test / 255
        X_val = X_val / 255

        y_train = y_train.reshape(-1, 1)
        y_test = y_test.reshape(-1, 1)
        y_val = y_val.reshape(-1, 1)

        return X_train, y_train, X_test, y_test, X_val, y_val

    def process_data_helper(self, data):
        X = []
        y = []
        for array, label in data:
            X.append(array)
            y.append(label)
        return np.array(X), np.array(y)
    
    def data_augmentation(self, X_train):
        train_aug = ImageDataGenerator(
            featurewise_center=False,
            samplewise_center=False,
            featurewise_std_normalization=False,
            samplewise_std_normalization=False,
            zca_whitening=False,
            rotation_range=30,
            zoom_range=0.2,
            width_shift_range=0.1,
            height_shift_range=0.1,
            horizontal_flip=True,
            vertical_flip=False
        )
        train_aug.fit(X_train)
        return train_aug
    
    def build_model(self):
        image_size = self.config.params_image_size
        model = Sequential()
        model.add(Conv2D(32 , (3,3) , strides=1 , padding='same' , activation='relu' , input_shape=(image_size, image_size, 3)))
        model.add(BatchNormalization())
        model.add(MaxPool2D((2,2) , strides=2 , padding='same'))
        model.add(Conv2D(64 , (3,3) , strides=1 , padding='same' , activation='relu'))
        model.add(Dropout(0.1))
        model.add(BatchNormalization())
        model.add(MaxPool2D((2,2) , strides=2 , padding='same'))
        model.add(Conv2D(64 , (3,3) , strides=1 , padding='same' , activation='relu'))
        model.add(BatchNormalization())
        model.add(MaxPool2D((2,2) , strides=2 , padding='same'))
        model.add(Conv2D(128 , (3,3) , strides=1 , padding='same' , activation='relu'))
        model.add(Dropout(0.2))
        model.add(BatchNormalization())
        model.add(MaxPool2D((2,2) , strides=2 , padding='same'))
        model.add(Conv2D(256 , (3,3) , strides=1 , padding='same' , activation='relu'))
        model.add(Dropout(0.2))
        model.add(BatchNormalization())
        model.add(MaxPool2D((2,2) , strides=2 , padding='same'))
        model.add(Flatten())
        model.add(Dense(units=128 , activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(units=1 , activation='sigmoid'))
        model.compile(optimizer="adam" , loss='binary_crossentropy' , metrics=['accuracy'])
        return model
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        
    def train_model(self, model, X_train, y_train, X_val, y_val):
        learning_rate_reduction = ReduceLROnPlateau(monitor='val_accuracy', patience=2, verbose=1, factor=0.3, min_lr=0.000001)
        class_weights = {0: 0.4, 1: 1.0}
        epochs = self.config.params_epochs
        batch_size = self.config.params_batch_size

        train_aug = self.data_augmentation(X_train)

        history = model.fit(train_aug.flow(X_train, y_train, batch_size=batch_size), 
                            epochs=epochs,
                            validation_data=(train_aug.flow(X_val, y_val)),
                            class_weight=class_weights,
                            callbacks=[learning_rate_reduction])

        # Save the trained model
        self.save_model(path=self.config.trained_model_path, model=model)

        return history