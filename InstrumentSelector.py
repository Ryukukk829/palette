#
#

import os
import sys

import numpy as np
import pretty_midi
import csv
from tqdm import tqdm
from matplotlib import pyplot as plt




class InstrumentSelector():
    def __init__(self, file_name):
        self.file_name = file_name
        self.set_midi(file_name)

    def set_midi(self, file_name):
        self.file_name = file_name
        self.midi = pretty_midi.PrettyMIDI(file_name)

    def get_instruments(self):
        md_tracks = self.midi.instruments
        return [m.program for m in md_tracks]

    #楽器数の取得
    def get_num_instruments(self):
        md_tracks = self.midi.instruments
        return len([m for m in md_tracks])

    #[楽器数, 3] の配列
    def set_instruments_from_color(self, colors):
        for i in range(len(self.midi.instruments)):
            self.midi.instruments[i].program=self.color2instrument(colors[i]) 
        return self.get_instruments()

    #色から楽器を設定
    """
    def color2instrument(self, color):
        color = list(color)
        i = 0
        if (max(color) - min(color)  <= 30) and max(color) >= 80:
            i = 56#らっぱ
        elif min(color) >= 150:
            i = 23#アコーディオン
        elif max(color) <= 30:
            i = 44#チェロ
        elif color.index(max(color)) == 0:
            i = 47#ティンパニ
        elif color.index(max(color)) == 1:
            i = 70#オーボエ
        elif color.index(max(color)) == 2:
            i = 77#尺八
        else:
            i = 42#ヴァイオリン
            
        print(color, i)
        return i
    """
    #colorは3次元配列
    def color2instrument(self, color):
        if color.mean() >= 127:
            return 1
        else:
            return 0
    
    #ファイルへの書き込み
    def write(self, f = "./imgs/hoge.mid"):
        self.midi.write(f)
        return True
        
        

if __name__ == "__main__":
    file_name = sys.argv[1]
    #save_file = ""
    is_ = InstrumentSelector(file_name)
    c = [[0, 0, 255], [0, 255, 0], [255, 0, 0], [0,0,0]]
    is_.set_instruments_from_color(c)
    is_.write()
    

