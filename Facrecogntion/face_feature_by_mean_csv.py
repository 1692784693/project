# @Time    : 2018/12/4 17:15
# @Author  : pangguoyi
# @File    : face_feature_by_mean_csv.py

import dlib
import numpy as np
import cv2
import pandas as pd

#首先还是初始化128d的人脸特征模型
recognition = dlib.face_recognition_model_v1('lib/dlib_face_recognition_resnet_model_v1.dat')

#计算向量间的距离
#fea_1 表示从特征均值文件中拿到特征数据
#fea_2 表示从摄像头拍摄到的人脸特征数据
def get_xiangliang_distance(fea_1,fea_2):
    fea_1 = np.array(fea_1)
    fea_2 = np.array(fea_2)

    distanct = np.sqrt(np.sum(np.square(fea_1-fea_2)))

    #根据阈值来判断是否是同一个人，当向量距离差异和大于30% 也就是0.3的时候，也就不是同一个人

    print('distanct==========',distanct)
    if distanct >0.5:
        return 'N'
    else:
        return 'Y'

#首先读取存放人脸特征值数据的csv文件

path_face_feature_mean_csv = 'data/feature_mean_all.csv'
csv_rd = pd.read_csv(path_face_feature_mean_csv)

#定义一个集合存放所有人特征的均值

csv_feature_mean = []

print('========',csv_rd.shape[0])

#csv_rd.shape[0] 取出有多少个存放了特征的人脸数

for x in range(csv_rd.shape[0]):
    #定义一个每个人特征数据的集合
    every_feature_mean = []
    for y in range(len(csv_rd.ix[x])):
        every_feature_mean.append(csv_rd.ix[x][y])
    #将个人的特征均值放在csv_feature_mean  这里面

    csv_feature_mean.append(every_feature_mean)
print('存放的人脸特征数据有:',len(csv_feature_mean))

#通过摄像头获取人脸特征数据
#初始化dlib人脸检测器
detector = dlib.get_frontal_face_detector()

#初始化68 点特征预测器
predictor = dlib.shape_predictor('lib/shape_predictor_68_face_landmarks.dat')

#使用OpenCV调用摄像头
cap = cv2.VideoCapture(0)
#设置视频的大小参数
cap.set(3,480)
#定义获取图片特征的方法
def get_128d_features(face_path):
    faces = detector(img_gray,1)

    print('总共有人脸数',len(faces))
    face_features = []
    if len(faces)>0:
        face_shape = predictor(img_gray,faces[0])
        face_features.append(recognition.compute_face_descriptor(img_gray,face_shape))
    else:
        face_features = []
        print('没有检测到人脸')
    return face_features

#当摄像头打开的时候
while cap.isOpened():
    #默认摄像头640 x 480
    flag, img_rd = cap.read()

    # 接受外部一个输入命令
    kk = cv2.waitKey(1)

    img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)
    # 判断有多少个人脸
    faces = detector(img_gray, 0)
    #定义两个集合存放摄像头中的人物名字以及名字的坐标
    name_position_list =[]
    name_list = []

    font = cv2.FONT_HERSHEY_COMPLEX

    #如果检测到人脸
    if len(faces)>0:
        #将摄像头中所有人物的特征取出来存放到集合中
        feature_camera_list = []
        for x in range(len(faces)):
            #通过模型取出人物特征
            faces_shape = predictor(img_gray,faces[0])
            feature_camera_list.append(recognition.compute_face_descriptor(img_rd,faces_shape))
        #遍历摄像头中所有的人脸，获取任务对应名字需要存放的坐标地址
        for x in range(len(faces)):
            #如果没有检测到人脸，那么人脸名字会比特征集合少，绘制时候会出错，所以即使没有检测到，也要增加空的名字
            name_list.append('null')
            name_position_list.append(tuple([faces[x].left(),faces[x].bottom()-10]))
            #循环所有均值csv文件中的人脸特征，和摄像头中的人脸进行对比
            for i in range(len(csv_feature_mean)):
                print('=========person_',str(i))
                #将人脸进行对比
                ret = get_xiangliang_distance(feature_camera_list[x],csv_feature_mean[i])
                print('ret====================',ret)
                if ret == 'Y':
                    name_list[x] = 'person_'+str(i)

            #绘制显示的矩形框
            for k,d in enumerate(faces):
                #绘制人物头像框
                cv2.rectangle(img_rd,tuple([d.left(),d.top()]),tuple([d.right(),d.bottom()]),(0,0,255),2)
                #将人物名字根据坐标填写到人物头像框下面
        print(name_list[0])
        print(name_position_list[0])

        for x in range(len(faces)):
            cv2.putText(img_rd,name_list[x],name_position_list[x],font,0.8,(0,0,255),1,cv2.LINE_AA)

    cv2.imshow('camera',img_rd)

