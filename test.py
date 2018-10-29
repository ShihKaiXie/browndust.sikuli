import time
flag=1
ticks = time.time()
date=time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(ticks))+'_日誌'
f = open(date+'.txt','w',0)
def set_flag(x):
    global flag 
    flag=x;
    print flag

def Adventure_mode():##冒險模式
    ticks = time.time()
    if exists("1540537145861.png"): ##主畫面的最近戰役
        click("1540537154537.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->冒險模式:主畫面點擊進入最近戰役\n')
        f.flush
        return 
    if exists("1540537271505.png"):
        click("1540537277742.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->冒險模式:入場\n')
        f.flush
        return
    if exists(Pattern("1540542965316.png").exact()):
        click("1540542977160.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->冒險模式:點選戰鬥開始\n')
        f.flush
        return
        
    if exists(Pattern("1540538755053.png").exact()):
        click("1540538760800.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->冒險模式:冒險模式對戰完畢,再次對戰\n')
        f.flush
        return
    if exists(Pattern("1540543360197.png").exact()):
        click("1540543395770.png")
        click("1540543456633.png")
        set_flag(1)
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->冒險模式:馬蹄耗盡,變更競技場模式\n')
        f.flush
        return
    if exists("1540562330551.png"):
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->冒險模式:冒險模式對戰進行中\n')
        f.flush
        return
    
    else:
        type(Key.ESC)
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->冒險模式:無法辨識,回上步驟\n')
        f.flush
        
        
        
        
        
        
        

def Arena_mode():  ##競技場模式 
    ticks = time.time()
    if exists(Pattern("1540601955210.png").exact()):
        click("1540601960789.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->競技場模式:主畫面點擊進入對戰\n')
        f.flush
        return
        
    if exists("1540521286397.png"): ##對決找決鬥場##
        click("1540521291914.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->競技場模式:點選對戰的競技場\n')
        f.flush
        return
    if exists(Pattern("1540545300325.png").exact()):
        sleep(10)
        click("1540545324733.png")
        set_flag(2)
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->競技場模式:指揮劍耗盡,更改為新星競技場模式\n')
        f.flush
        return
        
    if exists(Pattern("1540543619349.png").exact()):
        click("1540770795698.png")   
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->競技場模式:競技場內點選開始攻擊\n')
        f.flush
        return
    if exists(Pattern("1540543934058.png").exact()):
        click("1540543940947.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->競技場模式:競技場對戰完畢,再次對戰\n')
        f.flush
        return
    if exists("1540544965399.png"):
        click("1540544972728.png")
        click("1540545190674.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->競技場模式:指揮劍不足,回首頁\n')
        f.flush
        return
    if exists("1540562330551.png"):
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->競技場模式:競技場模式對戰進行中\n')
        f.flush
        return
    else:
        type(Key.ESC)
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->競技場模式:無法辨識,回上步驟\n')
        f.flush
            
            

            
            
            
        

def New_star_mode():
    ticks = time.time()

    if exists(Pattern("1540572910287.png").exact()):
        click("1540683400142.png")
        
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->新星競技場模式:主畫面點擊進入對戰\n')
        f.flush
        return
        
    if exists("1540553413359.png"):
        click("1540553419487.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->新星競技場模式:點選對戰的新星競技場\n')
        f.flush
        return
        
    if exists(Pattern("1540554945534.png").exact()):
        sleep(10)
        click("1540554971536.png")
        set_flag(0);
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->新星競技場模式:指揮劍耗盡,更改為冒險模式\n')
        f.flush
        return
        

    
    if exists("1540553458432.png"):
        click("1540553468356.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->新星競技場模式:新星競技場內點選開始攻擊\n')
        f.flush
        return
    if exists(Pattern("1540553630139.png").exact()):
        click("1540553637628.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->新星競技場模式:新星競技場對戰完畢,再次對戰\n')
        f.flush
        return

    if exists("1540634388492.png"):
        click("1540634396123.png")
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->新星競技場模式:指揮劍不足,回首頁\n')
        f.flush
        return
    

        
    if exists("1540562330551.png"):
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->新星競技場模式:新星競技場對戰進行中\n')
        f.flush
        return
    else:
        type(Key.ESC)
        f.write(time.strftime("%m %d %Y %H:%M:%S", time.localtime(ticks))+'->新星競技場模式:無法辨識,回上步驟\n')
        f.flush
        
        
    
    
      

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










        
    
        