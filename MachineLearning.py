import random

import face_recognition
import cv2
import argparse


class MachineLearning:
    def __init__(self):
        pass

    def face_location(self, img_file_addr):
        """
        The origin in the lower left
        X1, Y1, X2, Y2
        :param img_file_addr:
        :return:
        """
        image = face_recognition.load_image_file(img_file_addr)
        face_locations = face_recognition.face_locations(image, model="cnn")
        return face_locations

    def face_encoding(self, img_file_addr):
        image = face_recognition.load_image_file(img_file_addr)
        face_encodings = face_recognition.face_encodings(image)
        return face_encodings

    def face_compare(self, students_list, face_encoding, tolerance=0.4):

        for e in students_list:
            l = len(e.encodings)
            if l > 0:
                n = min(10, l)
                num = 0
                for _ in range(n):
                    idx = random.randint(0, l - 1)
                    encoding = e.encodings[idx]
                    matches = face_recognition.compare_faces([encoding], face_encoding, tolerance=tolerance)
                    if True in matches:
                        num += 1
                if num >= n * .4:
                    return e
        return None

    def face_split(self, frame):
        locations = face_recognition.face_locations(frame)
        spt = []
        for location in locations:
            # print(location)
            roi = frame[location[0]:location[2], location[3]:location[1]]
            spt.append(roi)
        return spt


if __name__ == '__main__':
    # img = cv2.imread("233.png")
    # img2 = MachineLearning().face_split(img)[0]
    # cv2.namedWindow('img')
    # cv2.imshow('img', img2)
    # cv2.waitKey(0)
    # ml = MachineLearning()
    # print(ml.face_location("image/4.jpg"))
    pass
