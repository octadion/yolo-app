import cv2
import torch
from super_gradients.training import models
import numpy as np
import math
import yaml

def image_detection(path_x):
    image = cv2.imread(path_x)

    device = torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")

    model = models.get('yolo_nas_s', num_classes= 77, checkpoint_path='weights/ckpt_best2.pth').to(device)
    with open('data/config/data2.yaml', 'r') as file:
        data = yaml.safe_load(file)

    classNames = data.pop('names')

    result = model.predict(image, conf=0.30)
    bbox_xyxys = result.prediction.bboxes_xyxy.tolist()
    confidences = result.prediction.confidence
    labels = result.prediction.labels.tolist()
    class_final_names = []
    for (bbox_xyxy, confidence, cls) in zip(bbox_xyxys, confidences, labels):
        bbox = np.array(bbox_xyxy)
        x1, y1, x2, y2 = bbox[0], bbox[1], bbox[2], bbox[3]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        classname = int(cls)
        class_name= classNames[classname]
        class_final_names.append(class_name)
        conf = math.ceil((confidence*100))/100
        label = f'{class_name}{conf}'
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 255), 3)
        t_size = cv2.getTextSize(label, 0, fontScale = 1, thickness=2)[0]
        c2 = x1+t_size[0], y1-t_size[1] - 3
        cv2.rectangle(image, (x1, y1), c2, [255, 144, 30], -1, cv2.LINE_AA)
        cv2.putText(image, label, (x1, y1-2), 0, 1, [255, 255, 255], thickness=1, lineType = cv2.LINE_AA)
    yield image