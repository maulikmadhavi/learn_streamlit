import streamlit as st
import cv2
import numpy as np
from PIL import Image
import requests
from streamlit_image_comparison import image_comparison

st.write("Streamlit is also great for more traditional ML use cases like computer vision or NLP. Here's an example of edge detection using OpenCV. 👁️") 
    

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
else:
    image = Image.open(requests.get("https://picsum.photos/200/120", stream=True).raw)

edges = cv2.Canny(np.array(image), 100, 200)
tab1, tab2 = st.tabs(["Detected edges", "Original"])
tab1.image(edges, width="stretch")
tab2.image(image, width="stretch")


# render image-comparison
image_comparison(
    img1=edges,
    img2=image,
)