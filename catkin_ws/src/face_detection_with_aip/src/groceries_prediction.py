#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib
import rospy
import numpy as np
from aip import AipFace
import cv2
import matplotlib.pyplot as plt
from std_msgs.msg import String
from std_msgs.msg import Int8
import os


class groceries_prediction:
    def __init__(self):
        self.filename = '/home/kamerider/catkin_ws/src/face_detection_with_aip/groceries.jpg'
	self.result = '/home/kamerider/darknet/predictions.jpg'
        self.darknetpath = '/home/kamerider/darknet'
        #发布器
        self.pub = rospy.Publisher('/prediction_end',String,queue_size=15)
        #订阅器
        rospy.Subscriber('/saving_groceries_photo',String,self.detection)

    #检测函数
    def detection(self,msg):
         msg.data=msg.data.lower()
         if msg.data == 'cupboard_photo_saved':
            #读取原始图像
            img = cv2.imread('/home/kamerider/catkin_ws/src/face_detection_with_aip/cupboard_groceries.jpg')
            cv2.imshow('source',img)
            
	    #通过os直接调用darknet
	    os.getcwd()
	    os.chdir(self.darknetpath)
	    os.system("./darknet detector test cfg/voc.data cfg/yolo-voc.2.0.cfg backup/yolo-voc_900.weights /home/kamerider/catkin_ws/src/face_detection_with_aip/cupboard_groceries.jpg")
            result = cv2.imread(self.result)
	    reslutCupboard = result.copy()
	    cv2.imwrite('/home/kamerider/darknet/predictionCupboard.jpg',resultCupboard)
            self.pub.publish('finish')

	 if msg.data == 'table_photo_saved':
            #读取原始图像
            img = cv2.imread('/home/kamerider/catkin_ws/src/face_detection_with_aip/table_groceries.jpg')
            cv2.imshow('source',img)
            
	    #通过os直接调用darknet
	    os.getcwd()
	    os.chdir(self.darknetpath)
	    os.system("./darknet detector test cfg/voc.data cfg/yolo-voc.2.0.cfg backup/yolo-voc_900.weights /home/kamerider/catkin_ws/src/face_detection_with_aip/table_groceries.jpg")
            result = cv2.imread(self.result)
	    reslutCupboard = result.copy()
	    cv2.imwrite('/home/kamerider/darknet/predictionTable.jpg',resultCupboard)
	    self.pub.publish('finish')
            
            
if __name__ =='__main__':
    #初始化节点
    rospy.init_node('groceries_prediction')
    print '----------init----------'
    print '-----WAITING FOR IMAGE-----'
    groceries_prediction()
    rospy.spin()
