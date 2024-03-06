import cv2
import argparse
from model import image_detection
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import os

# def main(input_path, output_path):
    
#     image = next(image_detection(input_path))

#     cv2.imwrite(output_path, image)

# if __name__ == "__main__":

#     parser = argparse.ArgumentParser(description='Run object detection on an image.')
#     parser.add_argument('input_path', help='Path to the input image.')
#     parser.add_argument('output_path', help='Path to save the output image.')

#     args = parser.parse_args()

#     main(args.input_path, args.output_path)

def generate_frames_image(path_x=''):
    yolo_output = image_detection(path_x)
    for detection_ in yolo_output:
        ret, buffer = cv2.imencode('.jpg', detection_)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')
        
app = Flask(__name__)

app.config['IMAGE_UPLOAD_FOLDER'] = 'output'

@app.route('/api/image_detection', methods=['POST'])

def api_image_detection():
    img = request.files['file']
    filename = secure_filename(img.filename)
    img.save(os.path.join(app.config['IMAGE_UPLOAD_FOLDER'], filename))

    result_generator = generate_frames_image(path_x=os.path.join(app.config['IMAGE_UPLOAD_FOLDER'], filename))
    for idx, result in enumerate(result_generator):
        result_filename = f"result_{idx}_" + filename
        with open(os.path.join(app.config['IMAGE_UPLOAD_FOLDER'], result_filename), 'wb') as f:
            f.write(result.split(b'\r\n\r\n')[1])

    return send_file(os.path.join(app.config['IMAGE_UPLOAD_FOLDER'], result_filename))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8002')