# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:12:53 2018

@author: Administrator
"""

import cv2
import os
import numpy as np
from PIL import Image

# recognizer = cv2.createLBPHFaceRecognizer()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()


def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []

    for image_path in image_paths:
        image = Image.open(image_path).convert('L')
        image_np = np.array(image, 'uint8')
        if os.path.split(image_path)[-1].split(".")[-1] != 'jpg':
            continue
        image_id = int(os.path.split(image_path)[-1].split(".")[1])
        faces = detector.detectMultiScale(image_np)
        for (x, y, w, h) in faces:
            face_samples.append(image_np[y:y + h, x:x + w])
            ids.append(image_id)

    return face_samples, ids


faces, Ids = get_images_and_labels("D:\\picture\\face")
recognizer.train(faces, np.array(Ids))
recognizer.save("trainner.yml")