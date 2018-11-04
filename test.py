from javax.swing import JFrame, JLabel, JButton, JTextField, JTextArea, JScrollPane
from java.awt import FlowLayout
from java.awt import *

import time 
import sys
import random

def initial():
    global flag
    global ticks
    global f
    global txt
    reload(sys)
    sys.setdefaultencoding('utf-8')
    flag=1
    ticks = time.time()
    date=time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(ticks))+'_日誌'
    f = open(date+'.txt','w',0)

    frame = JFrame("Log")
    txt = JTextArea(19,55)
    scrollPane=JScrollPane(txt);
    ##frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setLocation(2000,100)
    frame.setSize(480,450)
    frame.setLayout(FlowLayout())
    ##label = JLabel('記錄:')
    scrollPane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
    ##frame.add(label)
    frame.add(scrollPane)
    frame.setVisible(True)
    



def log_add(x):
    ticks = time.time()
    txt.append(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(ticks))+'->'+unicode(x, encoding='utf-8')+'\n') 
    txt.setCaretPosition(txt.getDocument().getLength()); 
    f.write(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(ticks))+'->'+x+'\n')
    f.flush
    
def set_flag(x):
    global flag 
    flag=x;

def Deploy():
    log_add('檢查第一隻傭兵')
    click(Location(294, 502))
    Change_mercenary(294, 502)
    log_add('檢查第二隻傭兵')
    click(Location(409, 505))
    Change_mercenary(409, 505)
    log_add('檢查第三隻傭兵')
    click(Location(519, 506))
    Change_mercenary(519, 506)
    log_add('檢查第四隻傭兵')
    click(Location(635, 506))
    Change_mercenary(635, 506)
    log_add('檢查第五隻傭兵')
    click(Location(750, 504))
    Change_mercenary(750, 504)
    log_add('檢查第六隻傭兵')
    click(Location(863, 500))
    Change_mercenary(863, 500)
    log_add('檢查第七隻傭兵')
    click(Location(269, 608))
    Change_mercenary(269, 608)
    
    
    
    
    
    
    
def Change_mercenary(x,y):   
    dict={1:Location(485, 842),2:Location(600, 839),3:Location(718, 835),4:Location(830, 842),5:Location(945, 838),6:Location(1057, 839),7:Location(1176, 838),8:Location(1289, 838),9:Location(1407, 837),10:Location(1522, 837),11:Location(1638, 833)}
    if exists(Pattern("1541266421429.png").exact()):
        click(Pattern("1541266425739.png").exact())
        
    if exists(Pattern("1541260976063.png").similar(0.52)):
        click("1541261009633.png")
        click("1541261041175.png")
        click("1541261047593.png")
        click("1541261057674.png")
        number=random.randint(1,11)
        print(number)
        note='替換第'+str(number)+'隻新肥料'
        log_add(note)
        click(dict[number])##第n隻新肥料
        click(Location(x, y))
        click("1541261569467.png")
        sleep(1)
    if exists(Pattern("1541266421429.png").exact()):
       click(Pattern("1541266425739.png").exact())
        

def Adventure_mode():##冒險模式
    ticks = time.time()
    if exists("1540537145861.png"): ##主畫面的最近戰役
        click("1540537154537.png")
        log_add('冒險模式:主畫面點擊進入最近戰役')
        return 
    if exists("1540537271505.png"):
        click("1540537277742.png")
        log_add('冒險模式:入場')
        return
    if exists(Pattern("1540542965316.png").exact()):
        Deploy()
        click("1541111918637.png")
        
        log_add('冒險模式:點選戰鬥開始')
        return
    if exists(Pattern("1541111878580.png").exact()):
        Deploy()
        click("1541111918637.png")
        
        log_add('冒險模式:點選戰鬥開始')
        return 
    if exists(Pattern("1540538755053.png").similar(0.75)):
        click("1540538760800.png")
        log_add('冒險模式:冒險模式對戰完畢,再次對戰')
        return
    if exists(Pattern("1540543360197.png").exact()):
        click("1540543395770.png")
        if exists("1540806249159.png"):
            
            click("1540543456633.png")
            set_flag(1)
            log_add('冒險模式:馬蹄耗盡,變更競技場模式')
            return
    if exists(Pattern("1541112406348.png").exact()):
        click("1540543395770.png")
        if exists("1540806249159.png"):
            
            click("1540543456633.png")
            set_flag(1)
            log_add('冒險模式:馬蹄耗盡,變更競技場模式')
            return
        
        

    
    if exists(Pattern("1540562330551.png").exact()):
        log_add('冒險模式:冒險模式對戰進行中')
        sleep(15)
        return
     
    else:
        type(Key.ESC)
        log_add('冒險模式:無法辨識,回上步驟')    
               

def Arena_mode():  ##競技場模式 
    ticks = time.time()
    if exists(Pattern("1540601955210.png").exact()):
        click("1540601960789.png")
        log_add('競技場模式:主畫面點擊進入對戰')
        return
        
    if exists("1540521286397.png"): ##對決找決鬥場##
        click("1540521291914.png")
        log_add('競技場模式:點選對戰的競技場')
        return
    if exists(Pattern("1540545300325.png").exact()):
        sleep(10)
        click("1540545324733.png")
        set_flag(2)
        log_add('競技場模式:指揮劍耗盡,更改為新星競技場模式')
        return
        
    if exists(Pattern("1540543619349.png").exact()):
        click("1540770795698.png")   
        log_add('競技場模式:競技場內點選開始攻擊')
        return
    if exists(Pattern("1540543934058.png").exact()):
        click("1540543940947.png")
        log_add('競技場模式:競技場對戰完畢,再次對戰')
        return
    if exists("1540544965399.png"):
        click("1540544972728.png")
        click("1540545190674.png")
        log_add('競技場模式:指揮劍不足,回首頁')
        return
    if exists(Pattern("1540562330551.png").exact()):
        log_add('競技場模式:競技場模式對戰進行中')
        return
    else:
        type(Key.ESC)
        log_add('競技場模式:無法辨識,回上步驟')
            

def New_star_mode():
    ticks = time.time()

    if exists(Pattern("1540572910287.png").exact()):
        click("1540683400142.png")
        
        log_add('新星競技場模式:主畫面點擊進入對戰')
        return
        
    if exists("1540553413359.png"):
        click("1540553419487.png")
        log_add('新星競技場模式:點選對戰的新星競技場')
        return
        
    if exists(Pattern("1540554945534.png").exact()):
        sleep(0)
        click("1540554971536.png")
        set_flag(0);
        log_add('新星競技場模式:指揮劍耗盡,更改為冒險模式')
        return
        

    
    if exists("1540553458432.png"):
        click("1540553468356.png")
        log_add('新星競技場模式:新星競技場內點選開始攻擊')
        return
    if exists(Pattern("1540553630139.png").exact()):
        click("1540553637628.png")
        log_add('新星競技場模式:新星競技場對戰完畢,再次對戰')
        return

    if exists("1540634388492.png"):
        click("1540634396123.png")
        log_add('新星競技場模式:指揮劍不足,回首頁')
        return
    

        
    if exists(Pattern("1540562330551.png").exact()):
        log_add('新星競技場模式:新星競技場對戰進行中')
        return
    else:
        type(Key.ESC)
        log_add('新星競技場模式:無法辨識,回上步驟')




if __name__ == '__main__':
    initial() 
    while 1: 
        global flag
        print flag
        if flag==0:
            Adventure_mode();
            wait(3.5)
        
        if flag==1:          
            Arena_mode()
            wait(3.5)       
        
        if flag==2:
            New_star_mode()
            wait(3.5)











        
    
        