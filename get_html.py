#
#

######## chrm drivr ###########
### https://chromedriver.storage.googleapis.com/index.html?path=95.0.4638.69/
###############################
import os
import sys

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import base64
import time
import ffmpeg


def main(wait_time = 2, path = "imgs/screenshot"):
    crmdrv = "/Users/ryukunobusue/pro/color_palette/chromedriver"#ChoromeDriverのパス
    #url = sys.argv[1]#
    url = "https://10.0.1.100"
    driver = webdriver.Chrome(crmdrv)
    #ログイン時のURL
    #url = ""#開きたいURL
    driver.get(""+ url)
    
    button = driver.find_elements_by_id("details-button")[0]
    button.click()
    button = driver.find_elements_by_id("proceed-link")[0]
    button.click()
    
    ID = "cclab"
    PASS = "surfonentropy"
    #ログイン
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders",
                           {"headers": get_auth_header(ID, PASS)})
    driver.get(""+ url)
    #動画のURL
    src = "api/holographic/stream/live_high.mp4"
    driver.get("{}/{}".format(url, src))
    
    #stream = ffmpeg.input("{}/{}".format(url, src))
    #stream = ffmpeg.output(video, "imgs/hoge.mp4")
    #ffmpeg.run(stream, capture_stdout=True, capture_stderr=True)

    #stream = ffmpeg.output(stream, 'images/%05d.jpg',r=5 ,f='image2')
    # 実行
    #ffmpeg.run(stream)

    time.sleep(5) 
    for i in range(wait_time):
        time.sleep(1)
        driver.save_screenshot('{}{}.png'.format(path, i))


    """
    while(True):
        #except KeyboardInterrupt:
        #break
        wait_time = 10
        time.sleep(wait_time)
        driver.save_screenshot('{}{}.png'.format(path, i))
        print("hoge")
    """
    driver.quit()

    print("end")


# Authorizationヘッダを付与
def get_auth_header(user, password):
    b64 = "Basic " + base64.b64encode("{}:{}".format(user, password).encode("utf-8")).decode("utf-8")
    return {"Authorization": b64}



if __name__ == "__main__":
    """
    import argparse
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("out", type = str,
                        help = "path to output file.")
    """
    main()

"""
##参考サイト
#https://ai-inter1.com/python-selenium/
#https://qiita.com/syunyo/items/09cc636344212112a6fc


検索メソッド：
find_element_by_{id, name, css_selector, etc...}()

SeleniumでBasic認証を突破する
https://qiita.com/mochi_yu2/items/ce598ec57afe44453e98

"""
