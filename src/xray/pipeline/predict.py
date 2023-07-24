import numpy as np
from keras.models import load_model
from keras.utils import load_img, img_to_array
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename
        
    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename
        test_image = load_img(imagename, target_size = (150,150))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Pneumonia'
            return [{ "image" : prediction}]
        elif result[0] == 0:
            prediction = 'Normal'
            return [{ "image" : prediction}]