from PIL import Image, ImageOps
import numpy as np

def preprocess_image(image):
    if image.mode == 'RGBA':
        image = image.convert("RGBA")
        canvas = Image.new('RGB', image.size, (255, 255, 255))
        canvas.paste(image, mask=image.split()[3]) 
        image = canvas
    elif image.mode in ['LA', 'P']:
        image = ImageOps.grayscale(image.convert('RGBA'))
    # Resized the image to 28x28 pixels, maintaining aspect ratio
    aspect_ratio = min(28 / image.size[0], 28 / image.size[1])
    new_size = (int(image.size[0] * aspect_ratio), int(image.size[1] * aspect_ratio))
    image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    # Created a 28x28 white background and pasted the resized image onto the center
    background = Image.new('L', (28, 28), 255)
    background.paste(image, (int((28 - new_size[0]) / 2), int((28 - new_size[1]) / 2)))
    
    # Inverted the colors to match the MNIST dataset
    image = ImageOps.invert(background)
    
    image_array = np.asarray(image).astype(np.float32) / 255.0
    
    image_array = np.expand_dims(image_array, axis=-1)
    
    # Batch dimension added
    image_array = np.expand_dims(image_array, axis=0)
    
    return image_array
