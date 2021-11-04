#coding:utf-8
#

import sys
import os

import numpy as np
#from PIL import Image
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import cv2
import imghdr


#RGBになってる。
class ColorPalette():
    def __init__(self, file_name, k = 5):
        self.file_name = "null"
        self.k = k
        self.seed = 0
        self.palette = self.set_palette([])
        self.set_image(file_name)

    
    #カラーパレットを作成したい画像(あるいは動画)ファイルを取得
    # 動画の場合、ランダムにフレームをとってきて、set_imageする。
    # file_name == VideoCapture のとき、カメラから画像を撮影し、set_imageする。
    # deviceid は、VideoCaptureのデバイスID
    def set_image(self, file_name, deviceid = 0):
        self.img_colors = np.zeros(3)
        #img = Image.open(file_name)
        if file_name == "VideoCapture":
            capture = cv2.VideoCapture(deviceid)
            print(capture.isOpened())
            ret, frame = capture.read()
            cv2.imwrite("tmp.jpg", frame)
            self.set_image("tmp.jpg")
            self.file_name = "tmp.jpg"
            
        elif imghdr.what(file_name) != None:
            img = cv2.imread(file_name)
            self.img_array = np.asarray(img[:,:,::-1])
            self.img_colors = np.vstack((self.img_colors,
                                         self.img_array.reshape(-1, 3) / 255))
            self.file_name = file_name
        else:
            try:
                print("mov")
                cap = cv2.VideoCapture(file_name)
                ret, frame = cap.read()
                print("ret", ret)
                fmax = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                print(fmax, file_name)
                for i in np.random.randint(1, fmax, 10):
                    self.save_frame(file_name,
                                    i,
                                    "tmp.jpg")
                    self.set_image("tmp.jpg")
                    self.file_name = "tmp.jpg"
            except RuntimeError:
                print("{} should be a video or an image file.".format(file_name))
        #print("{}".format(img_array))
        #print(img_array.mean(), img_array.max())

    def get_palette(self):
        return self.palette

    def set_palette(self, palette):
        self.palette = palette
        
    def save_frame(self, video_path, frame_num, result_path):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            return
        #os.makedirs(os.path.dirname(result_path), exist_ok=True)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(result_path, frame)

    
    #学習時の初期値を設定する
    def get_initial_centers(self):
        ini_c = np.array([[1, 1, 1],
                          [1, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1],
                          [1, 1, 0],
                          [1, 0, 1],
                          [0, 1, 1],
                          [0, 0, 0]])
        if self.k <= len(ini_c):
            ini_c = ini_c[:self.k]
        else:
            ini_c = "random"
            
        return ini_c

        
    #カラーパレットの作成
    def choice_color(self, flag = True):
        if flag:
            ini_c = self.get_initial_centers()
        else:
            ini_c = "k-means++"
        kmeans = KMeans(n_clusters=self.k,
                        random_state=self.seed,
                        init = ini_c,
                        max_iter = 1).fit(self.img_colors)
        self.set_palette((np.array(kmeans.cluster_centers_) * 255).astype(int))

    
    #画像と作成されたパレットの可視化
    def show_palette(self):
        plt.figure(figsize = (3, 4))
        ax = plt.axes([.1, .3, .8, .6])
        ax.imshow(self.img_array)
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        for i, c in enumerate(self.palette):
            ax = plt.axes([i * (1/self.k), .1, 1/self.k, .3])
            ax.imshow(np.array(list(c) * 4).reshape(2, 2, -1))
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
            
        plt.show()
        

if __name__ == "__main__":
    #file_name = "imgs/sakura.jpeg"
    file_name = sys.argv[1]
    cp = ColorPalette(file_name)
    cp.choice_color()
    cp.show_palette()

    cp.choice_color(flag = False)
    cp.show_palette()
