# encoding:utf-8
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  # 词云库
from PIL import Image
import matplotlib.pyplot as plt  # 数学绘图库
import numpy as np


class Word_Cloud:
    def __init__(self):
        pass

    def en_wordcloud_file_gen(filePath, imagePath, imageSavePath, isImageColor):
        '''
        英文词云图生成器
        :param filePath: 本地文本文件路径
        :param imagePath: 本地图片(最好是白底)路径
        :param imageSavePath: 词云图保存路径
        :param isImageColor: 是否使用背景图片颜色作为词的颜色(bool值)
        '''
        with open(filePath, 'r', encoding='gbk') as f:
            # 1、读入txt文本数据
            text = f.read()
            # 2、设置停用词(可通过add方法添加所需英文词汇或标点符号)
            stopwords = set(STOPWORDS)
            # file = open('stop_words.txt', 'r')

            # 3.1、获取本地背景图片
            image = np.array(Image.open(imagePath))
            if isImageColor:
                # 3.2、获取背景图片颜色
                image_colors = ImageColorGenerator(image)
            # 4、创建WordCloud实例并自定义设置参数(如背景色,背景图片和停用词等)
            wc = WordCloud(mask=image, background_color='white', max_font_size=60,
                           width=1000, height=600, scale=4,
                           stopwords=stopwords, random_state=42, max_words=2000)
            # 5、根据设置的参数，统计词频并生成词云图
            wc.generate(text)
            # 6.将生成的词云图保存在本地
            plt.figure('词云图')  # 指定所绘图名称
            if isImageColor:
                plt.imshow(wc.recolor(color_func=image_colors))  # 以图片的形式显示词云,并依据背景色重置词的颜色
            else:
                plt.imshow(wc)
            plt.axis('off')      # 关闭图像坐标系
            plt.show()           # 在IDE中显示图片
            wc.to_file(imageSavePath)  # 按照背景图的宽高度保存词云图

    def en_wordcloud_text_gen(input_text, imagePath, imageSavePath, isImageColor):
        # 1、读入txt文本数据
        text = input_text
        # 2、设置停用词(可通过add方法添加所需英文词汇或标点符号)
        stopwords = set(STOPWORDS)
        # file = open('stop_words.txt', 'r')

        # 3.1、获取本地背景图片
        image = np.array(Image.open(imagePath))
        if isImageColor:
            # 3.2、获取背景图片颜色
            image_colors = ImageColorGenerator(image)
        # 4、创建WordCloud实例并自定义设置参数(如背景色,背景图片和停用词等)
        wc = WordCloud(mask=image, background_color='white', max_font_size=60,
                       width=1000, height=600, scale=4,
                       stopwords=stopwords, random_state=42, max_words=2000)
        # 5、根据设置的参数，统计词频并生成词云图
        wc.generate(text)
        # 6.将生成的词云图保存在本地
        return wc.to_file(imageSavePath)  # 按照背景图的宽高度保存词云图
