##1.修改冒險模式外的3次返回偵錯機制
from sikuli import *
from javax.swing import JFrame, JLabel, JButton, JTextField, JTextArea, JScrollPane
from java.awt import FlowLayout
from java.awt import *

from datetime import datetime
import time
import sys
import random
import controller as ctr
#reload(controller)
#from controller import * 

def initial():
    global f ##文件
    global txt
    global number_of_occurrence
    reload(sys)
    sys.setdefaultencoding('utf-8')
    ctr.init()
    ctr.set_value('flag',0)
    ctr.set_value('reload_check',0)
    ctr.set_value('world_boss_check',0)
    ctr.set_value('raid_check',0)
    #ctr.set_value('raid_check',None)
    number_of_occurrence=0
    ctr.set_value('max_level_check',None)
    ctr.set_value('return_check',0)
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




def Exception_Handling():
    if exists("1542794650734.png",0.001):
        click("1542794659537.png")
        sleep(3)
        log_add('活動關閉')
        return
    if exists("1542794712763.png",0.001):
        click("1542794659537.png")
        sleep(3)
        log_add('活動關閉')
        return
 
    
    if exists("1542521458095.png",0.001):
        click(Pattern("1542521458095.png").similar(0.65))
        sleep(3)
        log_add('重新嘗試連線')
        return
    if exists("1542580085681.png",0.001):
        click("1542580085681.png")
        log_add('一週決鬥場結果,點擊畫面')
        return
    if exists("1542580241827.png",0.001):
        click("1542580241827.png")
        log_add('決鬥場一週獎勵,點擊畫面')
        return
    if exists("1542580477052.png",0.001):
         
        click("1542580477052.png")
        log_add('決鬥場一週結果,點擊畫面')
        return
    if exists("1542665915094.png",0.001):
        click("1542665922296.png")
        log_add('簽到獎勵,點擊關閉')
        return
        
    return_times=ctr.get_value('return_check')
    #if exists("1543357612727.png",0.001):
        #click("1543357612727.png")
        #log_add('新星決鬥場獎勵,點擊關閉')
        #return
        
    if return_times>2:
        click("1541462696985.png")
        log_add('無法辨識,回上步驟')
        ctr.set_value('return_check',0)
        return
        
         
        
        



def log_add(x):
    ticks = time.time()
    txt.append(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(ticks))+'->'+unicode(x, encoding='utf-8')+'\n') 
    txt.setCaretPosition(txt.getDocument().getLength()); 
    f.write(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(ticks))+'->'+x+'\n')
    f.flush
    ctr.set_value('return_check',0)
    

def Deploy():
    log_add('檢查(1,1)傭兵')
    click(Location(294, 502))
    Change_mercenary(294, 502)
    log_add('檢查(1,2)傭兵')
    click(Location(409, 505))
    Change_mercenary(409, 505)
    log_add('檢查(1,3)傭兵')
    click(Location(519, 506))
    Change_mercenary(519, 506)
    log_add('檢查(1,4)傭兵')
    click(Location(635, 506))
    Change_mercenary(635, 506)
    log_add('檢查(1,5)傭兵')
    click(Location(750, 504))
    Change_mercenary(750, 504)
    log_add('檢查(1,6)傭兵')
    click(Location(863, 500))
    Change_mercenary(863, 500)
    #log_add('檢查(2,1)傭兵')
    #click(Location(269, 608))
    #Change_mercenary(269, 608)
    
    #log_add('檢查(3,1)傭兵')
    #click(Location(242, 713))
    #Change_mercenary(242, 713)
    ctr.set_value('raid_check',1)
            
    
def Change_mercenary(x,y):   
    dict={1:Location(485, 842),2:Location(600, 839),3:Location(718, 835),4:Location(830, 842),5:Location(945, 838),6:Location(1057, 839),7:Location(1176, 838),8:Location(1289, 838),9:Location(1407, 837),10:Location(1522, 837),11:Location(1638, 833)}
    if exists(Pattern("1541266421429.png").exact()):
        click(Pattern("1541266425739.png").exact())
        
    if exists(Pattern("1541260976063.png").similar(0.52)):
        if exists("1541261009633.png"):
            click("1541261009633.png")
        if exists("1541261041175.png"):
            click("1541261041175.png")
        if exists("1541261047593.png"):
            click("1541261047593.png")
        if exists("1541261057674.png"):
            click("1541261057674.png")
        number=random.randint(1,11)
        note='替換第'+str(number)+'隻新肥料'
        log_add(note)
        click(dict[number])##第n隻新肥料
        click(Location(x, y))
        click("1541261569467.png")
        sleep(1)
    if exists(Pattern("1541266421429.png").exact()):
       click(Pattern("1541266425739.png").exact())
        

def Adventure_mode():##冒險模式
    global number_of_occurrence 
    ticks = time.time()
    if exists(Pattern("1543187454308.png").exact(),0.001):
        click("1541462696985.png")
        log_add('冒險模式:處於冒險王模式')
        return 
        
        
    if exists("1540537145861.png",0.001): ##主畫面的最近戰役
        click("1540537154537.png")
        log_add('冒險模式:主畫面點擊進入最近戰役')
        return 

    if exists("1542408398866.png",0.001):
        click("1542408398866.png")
        log_add('冒險模式:戰役地圖畫面')
        return 
        
    if exists("1540537271505.png",0.001):
        click("1540537277742.png")
        log_add('冒險模式:入場')
        sleep(5)
        return
    if exists(Pattern("1540542965316.png").exact(),0.001):
        max_level_decision=ctr.get_value('max_level_check')
        if max_level_decision==None:
            log_add('冒險模式:肥料皆未滿等')
        if max_level_decision!=None:
            log_add('冒險模式:肥料滿等')
            Deploy()
        click("1541111918637.png")
        number_of_occurrence+=1
        log_add('冒險模式:點選戰鬥開始,第'+str(number_of_occurrence)+'次關卡')
        sleep(15)
        return
    if exists(Pattern("1541111878580.png").exact(),0.001):
        max_level_decision=ctr.get_value('max_level_check')
        if max_level_decision==None:
            log_add('冒險模式:肥料皆未滿等')
        if max_level_decision!=None:
            log_add('冒險模式:肥料滿等')
            Deploy()
        click("1541111918637.png")
        number_of_occurrence+=1
        log_add('冒險模式:點選戰鬥開始,第'+str(number_of_occurrence)+'次關卡')
        sleep(15)
        return 
    if exists(Pattern("1542468428863.png").exact(),0.001):
        max_level_decision=ctr.get_value('max_level_check')
        if max_level_decision==None:
            log_add('冒險模式:肥料皆未滿等')
        if max_level_decision!=None:
            log_add('冒險模式:肥料滿等')
            Deploy()
        click("1541111918637.png")
        number_of_occurrence+=1
        log_add('冒險模式:點選戰鬥開始,第'+str(number_of_occurrence)+'次關卡')
        sleep(15)
        return 
        
    if exists(Pattern("1540538755053.png").similar(0.75),0.001):
        #max_level_check=Region(651,598,875,193).exists("1542600578944.png",0.001)
        max_level_check=Region(773,590,756,191).exists("1542600578944.png",0.001)
        ctr.set_value('max_level_check',max_level_check)

        click("1540538760800.png")
        log_add('冒險模式:冒險模式對戰完畢,再次對戰')
        sleep(5)
        return
    if exists(Pattern("1540543360197.png").exact(),0.001):
        click("1540543395770.png")
        if exists("1540806249159.png"):
            
            click("1540543456633.png")
            ctr.set_value('flag',1)
            log_add('冒險模式:馬蹄耗盡,變更競技場模式')
            return
    if exists(Pattern("1541112406348.png").exact(),0.001):
        click("1540543395770.png")
        if exists("1540806249159.png"):
            
            click("1540543456633.png")
            ctr.set_value('flag',1)
            log_add('冒險模式:馬蹄耗盡,變更競技場模式')
            return
    if exists(Pattern("1542468361790.png").exact(),0.001):
        click("1540543395770.png")
        if exists("1540806249159.png"):
            
            click("1540543456633.png")
            ctr.set_value('flag',1)
            log_add('冒險模式:馬蹄耗盡,變更競技場模式')
            return

    
    if exists(Pattern("1540562330551.png").exact(),0.001):
        log_add('冒險模式:冒險模式對戰進行中')
        sleep(15)
        return
    if exists("1542603976698.png",0.001):
        sleep(3)
        log_add('冒險模式:獎勵畫面')
        return
    
    else:        
        return_times=ctr.get_value('return_check')
        return_times+=1
        ctr.set_value('return_check',return_times)
        print('冒險模式:無法辨識次數:'+str(return_times))
        return
               

def Arena_mode():  ##競技場模式 
    ticks = time.time()

    if exists("1541478988282.png",0.001):
        click("1541462696985.png")
        log_add('競技場模式:主畫面異常,點擊返回')
        return
        
        
    if exists(Pattern("1540601955210.png").exact(),0.001):
        click("1540601960789.png")
        log_add('競技場模式:主畫面點擊進入對戰')
        return
        
    if exists("1540521286397.png",0.001): ##對決找決鬥場##
        click("1540521291914.png")
        log_add('競技場模式:點選對戰的競技場')
        return
    if exists(Pattern("1540545300325.png").exact(),0.001):
        sleep(10)
        click("1540545324733.png")
        ctr.set_value('flag',2)
        log_add('競技場模式:指揮劍耗盡,更改為新星競技場模式')
        return

    if exists("1541337347773.png",0.001):
        sleep(10)
        click("1540545324733.png")
        ctr.set_value('flag',2)
        log_add('競技場模式:競技場模式關閉,更改為新星競技場模式')
        return
        
        
    if exists(Pattern("1540543619349.png").exact(),0.001):
        click("1540770795698.png")   
        log_add('競技場模式:競技場內點選開始攻擊')
        sleep(15)
        return
    if exists(Pattern("1540543934058.png").exact(),0.001):
        click("1540543940947.png")
        log_add('競技場模式:競技場對戰完畢,再次對戰')
        return

    if exists("1541486945021.png",0.001):
        click("1541486951031.png")
        log_add('競技場模式:競技場對戰中被暫停,繼續對戰')
        return
        
        
    if exists("1540544965399.png",0.001):
        click("1540544972728.png")
        click("1540545190674.png")
        log_add('競技場模式:指揮劍不足,回首頁')
        return
    if exists(Pattern("1540562330551.png").exact(),0.001):
        log_add('競技場模式:競技場模式對戰進行中')
        sleep(30)
        return


    
    else:
        click("1541462696985.png")
        log_add('競技場模式:無法辨識,回上步驟')
            

def New_star_mode():
    ticks = time.time()

    if exists("1541478988282.png",0.001):
        click("1541462696985.png")
        log_add('新星競技場模式:主畫面異常,點擊返回')
        return
    
    if exists(Pattern("1540572910287.png").exact(),0.001):
        click("1540683400142.png")
        
        log_add('新星競技場模式:主畫面點擊進入對戰')
        return
        
    if exists("1540553413359.png",0.001):
        click("1540553419487.png")
        log_add('新星競技場模式:點選對戰的新星競技場')
        return
        
    if exists(Pattern("1540554945534.png").exact(),0.001):
        click("1541462696985.png")
        ctr.set_value('flag',0);
        log_add('新星競技場模式:指揮劍耗盡,更改為冒險模式')
        return
        

    
    if exists("1540553458432.png",0.001):
        click("1540553468356.png")
        log_add('新星競技場模式:新星競技場內點選開始攻擊')
        sleep(15)
        return

    if exists("1541486945021.png",0.001):
        click("1541486951031.png")
        log_add('新星競技場模式:新星競技場對戰中被暫停,繼續對戰')
        return
    if exists(Pattern("1540553630139.png").exact(),0.001):
        click("1540553637628.png")
        log_add('新星競技場模式:新星競技場對戰完畢,再次對戰')
        return
    
    if exists("1542115587603.png",0.001):
        
        sleep(10)
        click("1542115623560.png")
        
        ctr.set_value('flag',0)
        log_add('新星競技場模式:新星競技場模式關閉,更改為冒險模式')
        return
    
    if exists("1540634388492.png",0.001):
        click("1540634396123.png")
        log_add('新星競技場模式:指揮劍不足,回首頁')
        return
    

        
    if exists(Pattern("1540562330551.png").exact(),0.001):
        log_add('新星競技場模式:新星競技場對戰進行中')
        sleep(30)
        return
    else:
        click("1541462696985.png")
        log_add('新星競技場模式:無法辨識,回上步驟')

def Co_op_raid():
    if exists("1543186174586.png",0.001):
        click("1543186208548.png")
        log_add('協力征討戰模式:處於戰役模式入場畫面,點擊返回')
        return
        
        
    
    if exists("1542347246901.png",0.001):
        click("1541462696985.png")
        log_add('協力征討戰模式:處於主畫面對戰,點擊返回')
        return
    if exists("1542347298977.png",0.001):
        click("1542347374692.png")
        log_add('協力征討戰模式:處於主畫面結束遊戲,點擊取消')
        return 

        
    if exists("1541459381777.png",0.001):
        click("1541459381777.png")
        log_add('協力征討戰模式:點擊協力征討')
        return
    if exists(Pattern("1541464191081.png").similar(0.89),0.001):
        click("1541464191081.png")
        log_add('協力征討戰模式:主畫面點擊進入挑戰')
        return 
    if exists(Pattern("1543359173538.png").exact(),0.001):
        click(Pattern("1543359173538.png").exact())
        log_add('協力征討戰模式:主畫面點擊進入挑戰')
        return 
        
    if exists(Pattern("1542408702575.png").similar(0.95),0.001):
        click(Pattern("1542408702575.png").similar(0.90))
        log_add('協力征討戰模式:主畫面點擊進入挑戰')
        return 
        
    if exists(Pattern("1541464797738.png").exact(),0.001):        
        click("1541462696985.png")
        ctr.set_value('flag',4);
        ctr.set_value('raid_check',1);
        log_add('協力征討戰模式:征討號角耗盡,更改為世界王模式')
        return
    if exists("1541640882819.png",0.001):
        click("1541462696985.png")
        wait(1)
        click("1541462696985.png")
        wait(1)
        ctr.set_value('flag',4);
        ctr.set_value('raid_check',1);
        log_add('協力征討戰模式:征討號角耗盡,更改為世界王模式')
        return
        
        
    if exists("1541461967766.png",0.001):
        click("1541461967766.png")
        log_add('協力征討戰模式:點擊創立隊伍')
        return
    if exists(Pattern("1542581465581.png").exact(),0.001):
        click(Location(745, 625))
        sleep(1)
        click(Location(745, 625))
        log_add('協力征討戰模式:更改隊伍人數')
        return
        
       
        
        
    if exists("1541462029490.png",0.001):
        click("1541462029490.png")
        log_add('協力征討戰模式:點擊創立隊伍')
        return
    if exists("1541462786814.png",0.001):
        click("1541462696985.png")
        log_add('協力征討戰模式:隊伍完成征討,點擊返回以退出隊伍')
        if exists("1541462838778.png"):
            click("1541462843345.png")
            log_add('協力征討戰模式:確認退出隊伍')
        return
    if exists("1541462684027.png",0.001):
        click("1541462696985.png")
        click("1541462696985.png")
        log_add('協力征討戰模式:隊伍完成征討,點擊返回以退出隊伍')
        if exists("1541462838778.png"):
            click("1541462843345.png")
            log_add('協力征討戰模式:確認退出隊伍')
        return
    if exists("1541462342399.png",0.001):
        click("1541462342399.png")
        return
    if exists("1541462448774.png",0.001):
        click("1541462448774.png")
        return
    if exists(Pattern("1541462398719.png").exact(),0.001):
        click("1541462398719.png")
        log_add('協力征討戰模式:戰鬥開始')
        return
    if exists("1541462951589.png",0.001):
        click("1541462951589.png")
        log_add('協力征討戰模式:征討狀態已變更')
        return
    if exists("1541463275079.png",0.001):
        click("1541463280365.png")
        log_add('協力征討戰模式:戰鬥結束,點擊確認')
        return
    if exists(Pattern("1540562330551.png").exact(),0.001):
        log_add('協力征討戰模式:協力征討戰進行中')
        return
    else:
        click("1541462696985.png")
        log_add('協力征討戰模式:無法辨識,回上步驟')

def boss_mode():
    if exists("1542347246901.png",0.001):
        click("1541462696985.png")
        log_add('協力征討戰模式:處於主畫面對戰,點擊返回')
        return
    if exists("1542347298977.png",0.001):
        click("1542347374692.png")
        log_add('協力征討戰模式:處於主畫面結束遊戲,點擊取消')
        return
    if exists(Pattern("1541464191081.png").similar(0.89),0.001) or exists(Pattern("1542408702575.png").exact(),0.001):
        click("1541464191081.png")
        log_add('世界王模式:主畫面點擊進入挑戰')
        return

    if exists(Pattern("1542523387268.png").exact(),0.001):
       click("1542401405585.png")
       log_add('世界王模式:點擊入場')
       return
    
    if exists("1542347435703.png",0.001):
        click("1542347435703.png")
        log_add('世界王模式:點擊進入世界魔王')
        return
    if exists("1542401134841.png",0.001):
        click("1542401134841.png")
        log_add('世界王模式:點擊進入世界魔王')
        return
    if exists("1542523034688.png",0.001):
        click("1542523034688.png")
        log_add('世界王模式:點擊進入世界魔王')
        return
    if exists("1542582213770.png",0.001):
        click("1542582213770.png")
        log_add('世界王模式:點擊進入世界魔王')
        return
        
        
    if exists("1542401208882.png",0.001):
        click("1542401225904.png")
        log_add('世界王模式:昨日世界王任務結果,點擊關閉')
        return
        
    if exists("1542401280468.png",0.001):
        click("1542401280468.png")
        log_add('世界王模式:昨日世界王任務結果,點擊關閉')
        return
        
    if exists("1542401362989.png",0.001):
        click("1542401368424.png")
        log_add('世界王模式:累積分數點擊確認')
        return


    
    if exists("1542401483544.png",0.001):
        click("1542401483544.png")
        log_add('世界王模式:點擊戰鬥開始')
        return
        
    if exists("1542401524784.png",0.001):
        click("1542401524784.png")
        log_add('世界王模式:點擊戰鬥開始')
        return
           
    if exists("1541486945021.png",0.001):
        click("1541486951031.png")
        log_add('世界王模式:世界王模式對戰中被暫停,繼續對戰')
        return 
    if exists(Pattern("1540562330551.png").exact(),0.001):
        log_add('世界王模式:世界王模式進行中')
        return
    if exists("1542347509662.png",0.001):
        click("1541462696985.png")
        wait(3)
        if exists("1542347535388.png"):
            click("1542347546360.png")
            wait(3)
            ctr.set_value('flag',1);
            ctr.set_value('world_boss_check',1)
            log_add('世界王模式:戰鬥次數耗盡,更改為競技場模式')
    else:
        click("1541462696985.png")
        log_add('世界王模式:無法辨識,回上步驟')

def reload_app():
    reload_decision=ctr.get_value('reload_check')
    if exists("1542346850592.png",0.001) and reload_decision==0:
        log_add('重啟模式:等候180秒後開始重啟')
        sleep(60)
        log_add('重啟模式:等候120秒後開始重啟')
        sleep(60)
        log_add('重啟模式:等候60秒後開始重啟')
        sleep(60)
        click(Location(559, 9))
        log_add('重啟模式:關閉程式')
        return
    if exists("1542346912153.png",0.001):
        ctr.set_value('reload_check',1)
        wait(3)
        click("1542346912153.png")
        log_add('重啟模式:啟動程式')
        sleep(30)
        return
    if exists("1542346980288.png",0.001):
        ctr.set_value('flag',3)
        log_add('重啟模式:重啟完成,進入協力爭討戰模式')
        return
    if exists("1540537145861.png",0.001): ##主畫面的最近戰役
        ctr.set_value('flag',3)
        log_add('重啟模式:重啟完成,進入協力爭討戰模式')
        return
    else:
        click("1541462696985.png")
        log_add('重啟模式:無法辨識,回上步驟')
        
        
        
        
        


if __name__ == '__main__':
    initial() 
    while 1: 
        Exception_Handling()
        curTime = datetime.now()
        reload_decision=ctr.get_value('reload_check')
        world_boss_decision=ctr.get_value('world_boss_check')
        raid_decision=ctr.get_value('raid_check')
        if curTime.hour==11 and reload_decision==0:
            ctr.set_value('flag',99)
        if curTime.hour==51 and raid_decision==0:
            ctr.set_value('flag',3)
        if curTime.hour==67 and world_boss_decision==0:
            ctr.set_value('flag',4)
        mode=ctr.get_value('flag')
        if mode==0:
            Adventure_mode();

        if mode==1:
            Arena_mode()
            
        if mode==2:
            New_star_mode()

        if mode==3:
            Co_op_raid()

        if mode==4:
            boss_mode()

        if mode==99:
            reload_app()

            
            











        
    
        