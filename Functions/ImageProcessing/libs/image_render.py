from __future__ import print_function
import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()
if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN()
capture = cv.VideoCapture(cv.samples.findFileOrKeep(args.input))
if not capture.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)
while True:
    ret, frame = capture.read()
    if frame is None:
        break

    fgMask = backSub.apply(frame)

    cv.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
# import os
# import shutil
# import tempfile
#
# import cv2
# import pyzbar.pyzbar as pyzbar
# import requests
#
# from methods.wrappers import timeit
#
#
# @timeit
# def execute(img_url):
#     fname = "x"
#     r = requests.get(img_url, allow_redirects=True)
#     tmp = tempfile.TemporaryDirectory()
#     t_path = os.path.join(tmp.name, fname)
#     print(r.status_code)
#     if r.status_code == 200:
#         with open(t_path, 'wb') as handler:
#             handler.write(r.content)
#         image = cv2.imread(t_path)
#         decodedObjects = pyzbar.decode(image)
#         for obj in decodedObjects:
#             print("Type:", obj.type)
#             print("Data: ", obj.data, "\n")
#     shutil.rmtree(tmp.name)
#
#
# img_url = r"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.seoclerk.com%2Fpics%2F000%2F877%2F296%2F69f422f6871658593d8640b467a4418c.png"
# execute(img_url)
#
# import timeit
#
# # test='output = 10*5'
# # print(test,timeit.timeit(test))
#
# import_module = '''
# import os
# import shutil
# import tempfile
#
# import cv2
# import pyzbar.pyzbar as pyzbar
# import requests
#
# from methods.wrappers import timeit
#
# @timeit
# def execute(img_url):
#     fname = "x"
#     r = requests.get(img_url, allow_redirects=True)
#     tmp = tempfile.TemporaryDirectory()
#     t_path = os.path.join(tmp.name, fname)
#     print(r.status_code)
#     if r.status_code == 200:
#         with open(t_path, 'wb') as handler:
#             handler.write(r.content)
#         image = cv2.imread(t_path)
#         decodedObjects = pyzbar.decode(image)
#         for obj in decodedObjects:
#             print("Type:", obj.type)
#             print("Data: ", obj.data)
#             print()
#     shutil.rmtree(tmp.name)
# '''
# testcode = '''
#
# img_url = r"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.seoclerk.com%2Fpics%2F000%2F877%2F296%2F69f422f6871658593d8640b467a4418c.png"
# execute(img_url)
# '''
# time_list = timeit.repeat(stmt=testcode, setup=import_module, number=1, repeat=10)
# from numpy import mean
#
# print(time_list)
# print("AVG:", mean(time_list))

#
