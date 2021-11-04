#
#

from selenium import webdriver
from time import sleep

crmdrv = ""#ChoromeDriverのパス
driver = webdriver.Chrome(crmdrv)

#ログイン時のURL
url = ""#開きたいURL
driver.get(url)

# テキストボックスに文字を入力
e = driver.find_element_by_id("user")
e.clear()
e.send_keys(USER)
e = driver.find_element_by_id("pass")
e.clear()
e.send_keys(PASS)
# フォームを送信
frm = driver.find_element_by_css_selector("#loginForm form")
frm.submit()

a = driver.find_element_by_css_selector("")
#ログイン後のURL
url = a.get_attribute("href")
e = driver.find_element_by_id("mrcLivePreviewPlayer")
f = e.get_attribute("src")
print(f)

"""
##参考サイト
#https://ai-inter1.com/python-selenium/
#https://qiita.com/syunyo/items/09cc636344212112a6fc


検索メソッド：
find_element_by_{id, name, css_selector, etc...}()




"""
