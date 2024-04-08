import numpy as np
from tensorflow.keras.models import load_model as keras_load_model

def load_model(model_path):
    return keras_load_model(model_path)

def make_prediction(model, preprocessed_image):
    predictions = model.predict(preprocessed_image)
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)
    return predicted_class, confidence
