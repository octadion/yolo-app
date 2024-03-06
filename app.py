import cv2
import argparse
from model import image_detection
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

# def main(input_path, output_path):
    
#     image = next(image_detection(input_path))

#     cv2.imwrite(output_path, image)

# if __name__ == "__main__":

#     parser = argparse.ArgumentParser(description='Run object detection on an image.')
#     parser.add_argument('input_path', help='Path to the input image.')
#     parser.add_argument('output_path', help='Path to save the output image.')

#     args = parser.parse_args()

#     main(args.input_path, args.output_path)

app = Flask(__name__)

@app.route('/api/image_detection', methods=['POST'])

def api_image_detection():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(filename)

    image = image_detection(filename)
    output_filename = 'output/' + filename
    cv2.imwrite(output_filename, image)

    return send_file(output_filename, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8002')