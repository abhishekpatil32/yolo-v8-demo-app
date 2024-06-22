# YOLO v8 Demo App

This project is a Streamlit-based web application that allows users to upload an image, run YOLO v8 object detection on it, and download the detection results as a JSON file. The project uses the `ultralytics` YOLO library for object detection.

The main steps for the project include:
1. Upload an image in PNG, JPG, or JPEG format.
2. Run YOLO v8 object detection on the uploaded image.
3. Display the image with detected objects highlighted and
4. Download the detection results as a JSON file.

# Installation Steps:

1. Clone the repository:

git clone https://github.com/yourusername/yolo-v8-demo-app.git
cd yolo-v8-demo-app

2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
 

3. Install the required packages:

pip install -r requirements.txt

4. Download the YOLO v8 weights and place them in the `weights` directory:

mkdir weights
# Download the yolov8n.pt file and place it in the weights directory


## Usage

1. Run the Streamlit app:

streamlit run data.py

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an image, adjust the model confidence slider, and view the detected objects on the uploaded image.

4. Click the "Download JSON" button to download the detection results as a JSON file.


## File Structure
yolo-v8-demo-app/
├── weights/
│   └── yolov8n.pt  # Place your YOLO v8 weights here
├── app.py
├── requirements.txt
└── README.md
