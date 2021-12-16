#
#

import sys
import os


#とりあえず音符ごとにハ長調から任意の調に変換する
class ScaleConverter(object):
    def __init__(self):
        self.scales = {
            "gf":-6, "df":-5, "af":-4, "ef":-3, "bf":-2, "f":-1,
            "c":0, "g":1, "d":2, "a":3, "e":4, "b":5, "fs":6,
            "efm":-6, "bfm":-5, "fm":-4, "cm":-3, "gm":-2, "dm":-1,
            "am":0, "em":1, "bm":2, "fsm":3, "csm":4, "gsm":5,"dsm":6,
        }
        self.source_scale = "c"
        self.target_scale = "c"
        self.pitch = .5 #HSVのSの値を入れる 音高
        self.v = None   #HSVのVの値 長調か短調か決める?

    #指定可能な調のリストを取得
    def get_supported_scale(self):
        return list(self.scales.keys())

    #変換先の指定
    def set_target_scale(self, target_scale):
        if target_scale in self.scales:
            self.target_scale = target_scale
        else:
            print("scale :{} is not supported. ".format(target_scale))
        return target_scale
        
    #入力のノート番号をsourceからtargetの調に変換する
    def convert(self, num):
        return num + (8 * self.l() % 12) + 12 * int((self.pitch - .5) * 4)

    #変換に使うsourceとtargetの調の距離
    def l(self):
        l = self.scales[self.target_scale] - self.scales[self.source_scale]
        return l
    
    
def main(args):
    import pretty_midi
    
    sc = ScaleConverter()
    sc.set_target_scale(args[2])
    #print("converted note number is ", sc.convert(n))
    file_name = args[1]
    midi = pretty_midi.PrettyMIDI(file_name)
    for instrument in midi.instruments:
        # Don't want to shift drum notes
        if not instrument.is_drum:
            for note in instrument.notes:
                note.pitch = sc.convert(note.pitch)
    midi.write("out.midi")

    
    
if __name__ == "__main__":
    #n = int(sys.argv[1])
    #inputで出力ファイル名と変換したい調を入力する
    n = sys.argv
    main(n)
