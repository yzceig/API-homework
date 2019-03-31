#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys  
from PyQt5.QtGui import QImage, QPixmap,   QPainter
from PyQt5.QtWidgets import QApplication , QMainWindow
from dilidiliWin import Ui_dilidili
from bs4 import BeautifulSoup
import requests
import os
import time
import datetime
#import re
# regular expression


class MainWindow(QMainWindow ):
#初始化声明从dilidili调用的类
    def __init__(self, parent=None):    
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_dilidili()
        self.ui.setupUi(self)

#从网页上提取动画更新数据
    def queryAnime(self):
        
        dayName = self.ui.comboBox.currentText()
        dayAttri = self.transDayName(dayName)
            
        url='http://www.dilidili.name/'  
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/55.0.2883.87 Safari/537.36'}  #伪造浏览器标识
        html = requests.get(url, headers=headers)
        html.encoding = 'utf-8'

        soup = BeautifulSoup(html.content, "lxml")#对请求的网页转换格式

        day_Attri=soup.select(dayAttri)  #提取网页中某一class属性对应周几的list数据

        if dayAttri == '.elmnt-one':
            list_num=1
        elif dayAttri =='.elmnt-two' :
            list_num=1
        elif dayAttri == '.elmnt-three':
            list_num=1
        elif dayAttri == '.elmnt-four':
            list_num=0
        elif dayAttri == '.elmnt-five':
            list_num=0
        elif dayAttri == '.elmnt-six':
            list_num=0
        elif dayAttri == '.elmnt-seven':
            list_num=0
    #此判别是因为提取的list长度为2，但周一至周三对应的有效内容在list[1],周四到周日在list[0]
    
        day_Attri_img=day_Attri[list_num].find_all('img')#提取class属性对应周几的数据下img属性数据

        day_Attri_figcaption=day_Attri[list_num].find_all('figcaption')
        #提取class属性对应周几的数据下figcaption属性数据
        day_Attri_figure=day_Attri[list_num].find_all('figure')
        result=''#定义str类型结果变量

        for i in range(len(day_Attri_img)):
            #print(i,bq0[i].get('alt'),bq0[i].get('src'),end=" ")
            
            p=day_Attri_figcaption[i].select('p')

            span=day_Attri_figure[i].select('span')
            

            if len(p)==1:
                upgrade='   无更新   '
            else:
                upgrade='   更新至'+p[1].get_text()+'   '  #提取更新信息

            #此处提取番剧是否是本周最新更新，若是则显现'NEW'
            if span:
                new=span[0].get_text()
                
            else:
                new=' '


            r= day_Attri_img[i].get('alt') #提取动漫名
            r=r.ljust(30)
            
            text=r+upgrade+new+'\n'
            result+=text
        self.ui.resultText.setText(result)



    def transDayName(self ,dayName):
        dayAttri= ''
        if dayName == '周一' :
            dayAttri = '.elmnt-one'
        elif dayName == '周二' :
            dayAttri = '.elmnt-two'
        elif dayName == '周三' :
            dayAttri = '.elmnt-three'
        elif dayName == '周四' :
            dayAttri = '.elmnt-four'
        elif dayName == '周五' :
            dayAttri = '.elmnt-five'
        elif dayName == '周六' :
            dayAttri = '.elmnt-six'
        elif dayName == '周日' :
            dayAttri = '.elmnt-seven'    

        return dayAttri
    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap("./images/starry.jpg")
        #绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(),pixmap) 

    def clearResult(self):
        print('* clearResult  ')
        self.ui.resultText.clear()

if __name__=="__main__":  
    app = QApplication(sys.argv)  
    win = MainWindow()  
    win.setWindowOpacity(0.85)
    win.show()  
    sys.exit(app.exec_())