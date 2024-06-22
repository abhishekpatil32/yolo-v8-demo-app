import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import json
import torch

# Set title
st.title('YOLO v8 Demo App')

# Set header
st.header('Please upload an image')

# Upload file
file = st.file_uploader('', type=['png', 'jpg', 'jpeg'])

# Load model
model_path = 'weights/yolov8n.pt'
confidence = float(st.slider("Select Model Confidence", 25, 100, 40)) / 100

try:
    model = YOLO(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)
    st.stop()  # Stop the script if the model cannot be loaded

# Load image
if file:
    image = Image.open(file).convert('RGB')
    image_array = np.asarray(image)

    try:
        # Detect objects
        res = model.predict(image_array, conf=confidence)
        boxes = res[0].boxes
        res_plotted = res[0].plot()  # This should maintain the original color

        st.image(res_plotted, caption='Detected Image', use_column_width=True)

        detection_results = []

        for box in boxes:
            x, y, w, h = box.xywh[0]  # Assuming the box tensor is in xywh format
            detection_results.append({
                "name": "person",
                "c": {"x": float(x), "y": float(y), "z": None},
                "wh": {"x": float(w), "y": float(h), "z": None}
            })

        # Save results to a JSON file
        json_path = 'detection_results.json'
        with open(json_path, 'w') as f:
            json.dump(detection_results, f, indent=4)

        st.download_button(label="Download JSON", data=json.dumps(detection_results, indent=4), file_name='detection_results.json')

    except Exception as ex:
        st.error("Error in object detection")
        st.error(ex)
