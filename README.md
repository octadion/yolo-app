# YOLO Object Detection Project
This repository contains the code for a YOLO-NAS object detection project. The project includes two methods for running the object detection: via command line and via an API.

## Dependencies Installation
Before running the project, you need to install the necessary dependencies. You can do this by running the following command:
```bash
pip install -r requirements.txt
```
## Downloading the Model
Download the models from the provided link ([Model](https://drive.google.com/file/d/1HTFkFX01ScF7byQaoS--gkAQ2lVNTfCE/view?usp=sharing)).
After downloading, place the model file in the weights directory.

## Running the Application
There are two methods to run the application:

### Method 1: Command Line
You can run the application from the command line with the following command:
```bash
python app.py <input image path> <output image path>
```
Note: This method is currently commented out in the app.py file.

### Method 2: API
You can also run the application as an API. To do this, run the following command:
```bash
python app.py
```
Once the application is running, you can call the API with a POST request. The request should include form data with a key of file and the image you want to process as the value.

## Accessing the Deployed API
Once the API is deployed, you can access it at the following link: [API](http://167.71.211.12:8002/api/image_detection).
