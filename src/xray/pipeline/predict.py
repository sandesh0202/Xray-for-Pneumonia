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

        # Load and preprocess the image
        image = load_img(self.filename, target_size=(150, 150))
        image = img_to_array(image)
        image = image / 255.0 
        image = np.expand_dims(image, axis=0)
 
        # Make prediction
        prediction = model.predict(image)
        labels = ["Pneumonia", "Normal"]
        predicted_label = labels[int(np.round(prediction[0][0]))]
        

        return [{"prediction": predicted_label}]
