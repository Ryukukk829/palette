#
#
import sys
import os
from ColorPalette import ColorPalette
from InstrumentSelector import InstrumentSelector

def main(img_file, mid_file, save_file = "./samples/hoge.mid"):
    selector = InstrumentSelector(mid_file)
    cp = ColorPalette(img_file, k = selector.get_num_instruments())

    #cp.choice_color()
    cp.choice_color(flag = False)
    selector.set_instruments_from_color(cp.get_palette())
    selector.write(save_file)
    cp.show_palette()
    
        

if __name__ == "__main__":
    f_img = sys.argv[1]
    f_mid = sys.argv[2]
    main(f_img, f_mid)

