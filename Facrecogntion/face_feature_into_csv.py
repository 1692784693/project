# @Time    : 2018/12/3 19:29
# @Author  : pangguoyi
# @File    : face_feature_into_csv.py

#人脸识别库
import dlib
#数据处理库
import numpy as np
#图片处理
import cv2
import os
from skimage import io
import pandas as pd
import csv

#初始化dlib人脸检测器
detector = dlib.get_frontal_face_detector()
#初始化68 点特征预测器
predictor = dlib.shape_predictor('lib/shape_predictor_68_face_landmarks.dat')
#定义人脸识别模型
recognition = dlib.face_recognition_model_v1('lib/dlib_face_recognition_resnet_model_v1.dat')
#定义检测人脸图形的路径
face_photo_path = 'data/data_face_photo_from_camera/'
#定义人脸特征数据保存路径
face_feature_path = 'data/data_face_photo_feature_csv'
#定义获取图片特征的方法
def get_128d_features(face_path):
    img = io.imread(face_path)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)

    faces = detector(img_gray,1)
    print('总共有人脸数',len(faces))
    if len(faces)>0:
        face_shape = predictor(img_gray,faces[0])
        face_feature = recognition.compute_face_descriptor(img_gray,face_shape)
    else:
        face_feature = 0
        print('没有检测到人脸')
    return face_feature

#将人脸图形的特征写入csv文件中
#face_photo_path表示人脸图形的根目录路径，获取每张图片需要listdir
#csv_path是我们写入人脸特征的路径
def write_face_feature_to_csv(face_photo_path,csv_path):
    face_folders = os.listdir(face_photo_path)
    with open(csv_path,'w',newline='')as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(face_folders)):
            #提取每张人脸图片的128d特征
            face_128d_feature = get_128d_features(face_photo_path+'/'+face_folders[i])
            print('读取人脸特征：',face_photo_path+face_folders[i])
            if face_128d_feature==0:
                i = i+1
            else:
                writer.writerow(face_128d_feature)

#读取所有人脸图片的特征数据，写入到csv文件
faces = os.listdir(face_photo_path)
for x in faces:
    print('特征文件保存路径',face_feature_path+x+'.csv')
    print('图片路径',face_photo_path+x)
    write_face_feature_to_csv(face_photo_path+x,face_feature_path+x+'.csv')

#定义一个函数，求取128d特征的均值
def get_feature_mean(csv_path):

    colomn_name = []
    for x in range(128):
        colomn_name.append(str(x+1))
        #利用padans读取csv数据
    rd_csv = pd.read_csv(csv_path,names=colomn_name)
    #定义一个集合存放特征的均值
    csv_feature_mean = []

    for x in range(128):
        tmp = rd_csv[str(x+1)]
        tmp = np.array(tmp)

        #计算某一特征的均值
        tmp_mean = np.mean(tmp)
        csv_feature_mean.append(tmp_mean)
    return csv_feature_mean










