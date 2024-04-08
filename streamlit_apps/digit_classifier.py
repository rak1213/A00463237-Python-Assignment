import streamlit as st
from utils.model_utils import load_model, make_prediction
from utils.image_utils import preprocess_image
from PIL import Image

def show_app_digit_classifier():

    st.title('Digit Classifier')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        model = load_model('model/digit_classifier_model.keras')
        preprocessed_image = preprocess_image(image)
        predicted_class, confidence = make_prediction(model, preprocessed_image)
        st.success(f'Prediction: {predicted_class} with confidence {confidence:.2f}')
        
        # Display the uploaded image below the button
        st.image(image, caption='Uploaded Image', use_column_width=True)
