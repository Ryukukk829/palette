#
#
import sys
import os

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

class ColorPalette():
    def __init__(self, file_name, k = 5):
        self.k = k
        self.seed = 0
        self.palette = []
        self.set_image(file_name)
        

    #カラーパレットを作成したい画像ファイルを取得
    def set_image(self, file_name):
        img = Image.open(file_name)
        self.img_array = np.asarray(img)
        self.img_colors = self.img_array.reshape(-1, 3) / 255
        self.file_name = file_name
        #print("{}".format(img_array))
        #print(img_array.mean(), img_array.max())

    def get_palette(self):
        return self.palette
    
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
        self.palette = (np.array(kmeans.cluster_centers_) * 255).astype(int)

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
