#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 0021 16:07
# @Author  : YaoKai
# @Site    : 
# @File    : HeadImage.py
# @Software: PyCharm
import itchat
import PIL.Image as Image
import math
import os


def save_avatar(itchat, avator_file_path):
    friends = itchat.get_friends(update=True)[0:]
    num = 0
    for friend in friends:
        img = itchat.get_head_img(userName=friend['UserName'])
        save_path = avator_file_path + "/" + str(num) + ".png"
        try:
            with open(save_path, "wb") as f:
                f.write(img)
                print("正在保存第%d张头像" % num)
        except Exception as e:
            print(e)
        finally:
            num += 1
            f.close()


def make_path():
    avator_dir = "avator"
    avator_file_path = r"/PyCharm_Space/PythonDaily/img/" + avator_dir
    if not os.path.exists(avator_file_path):
        os.makedirs(avator_file_path)
    return avator_file_path


def merge_avator(path):
    length = len(os.listdir(path))
    each_size = int(math.sqrt(float(2000 * 2000) / length))
    cols = int(2000 / each_size)
    image = Image.new('RGBA', (2000, 2050), 'white')
    x = 0
    y = 0
    for i in range(0, length):
        try:
            img = Image.open(path + '/' + str(i) + '.png')

        except IOError:
            print(IOError)
        else:
            img = img.resize((each_size, each_size), Image.ANTIALIAS)
            image.paste(img, (x * each_size, y * each_size))
            print("合成第%d张图片" % (i + 1))
            x += 1
            if x == cols:
                x = 0
                y += 1
    image.save(path + "/" + "all.png")
    return image


if __name__ == "__main__":
    itchat.auto_login(True)  # 登录微信
    avator_path = make_path()
    save_avatar(itchat, avator_path)
    print('=' * 30)
    image = merge_avator(avator_path)
    # itchat.send(image, toUserName="filehelper")
