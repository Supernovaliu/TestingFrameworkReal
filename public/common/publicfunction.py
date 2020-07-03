#coding=utf-8

from config import globalparam


# put screenshots to img folder
def get_img(dr, filename):
    path = globalparam.img_path + '\\' + filename
    dr.take_screenshot(path)
