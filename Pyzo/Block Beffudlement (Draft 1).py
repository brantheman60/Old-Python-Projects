# Hardest Game Thing
from tkinter import *
import time
import copy

class Level():
    def __init__(self,descr, gmoveby,bmoveby,w,h,ghow_big,bhow_big,eventafter,vxs,vys,hxs,hys,ups,rights):
        self.description = descr
        self.moveby = gmoveby
        self.bad_move_by = bmoveby
        self.w = w
        self.h = h
        self.how_big = ghow_big
        self.how_big_bad = bhow_big
        self.event_after = eventafter
        self.gameover = False
        self.started = False
        self.victory = False
        self.verticalxs = vxs
        self.verticalys = vys
        self.horizontalxs = hxs
        self.horizontalys = hys
        self.ups = ups
        self.rights = rights
#descr, gmoveby,bmoveby,w,h,ghow_big,bhow_big,eventafter|,vxs,vys,hxs,hys,ups,rights
level = 0
levels= [ 
        Level("Bad speed: Slow; Level: Really Easy",
              20,10,300,300,40,40,50, [200], [40], [],[],[False],[]),
        Level("Bad speed: Slow; Level: Do the Wave",
              20,10,300,300,40,40,50,
              [], [],
              [40,80,120,160],[200,160,120,80],
              [],[True, True, True,True]),
        Level ("Bad speed: Slow; Level: Now Again",
               20,10,300,300,40,40,50,
               [250,210,170,130,90],[40,80,120,160,200],
               [240,200,160,120,80],[40,80,120,160,200],
               [False,False,False,False,False],[True, True,True,True,True]),
        Level ("Bad speed: Slow; Level: Between the Lines",
               20,10,300,300,40,40,50,
               [],[],
               [40,40,40,40,40,40,160,160,160,160,160,160,280,280,280,280,280,280],
               [40,80,120,160,200,240,40,80,120,160,200,240,40,80,120,160,200,240],
               [],[True, True,True, True,True,True,True,
                   True,True, True,True,True,True, True,True, True,True,True]),
        Level ("Bad speed: Slow; Level: Goalies",
               20,10,300,300,40,40,50,
               [300,300,300,260,260,260],[120,200,280,120,200,280],
               [120,200,280,120,200,280],[40,40,40,80,80,80],
               [False,False,False,False,False,False],[False,False,False,False,False,False]),
        Level ("Bad speed: Slow; Level: More Goalies",
               20,10,300,300,40,40,50,
               [300,300,300,260,260,260,220,220,220,180,180,180],[120,160,200,120,160,200,120,160,200,120,160,200],
               [120,200,280,120,200,280,120,200,280],[40,40,40,80,80,80,120,120,120],
               [False,False,False,False,False,False,False,False,False,False,False,False],
               [False,False,False,False,False,False,False,False,False]),
        Level ("Bad speed: Slow; Level: Frogger",
               20,10,300,300,40,40,50,
               [],[],
               [40,90,140,190,240,190,140,90,40,90,140,190,240,190,140,90],
               [240,240,240,240,240,240,240,240,60,60,60,60,60,60,60,60,60],
               [],[True, True,True, True,True,False, False, False, True, True,True,True,True, True, False, False,False]),
        Level("Bad speed: Slow; Level: Avalanche",
              20,10,300,300,40,40,50,
              [300,250,200,150,100,80,40],[80,100,140,160,180,220,260],
              [],[],[False,False,False,False,False,False,True],[]),
        Level ("Bad speed: Normal; Level: Dodging Bullets",
               20,20,300,300,40,20,50,
               [80,80,160,160,240,240],[150,150,150,150,150,150],
               [130,130,130],[120,180,240],
               [True,False,True,False,True,False],[True,True,True]),
        Level ("Bad speed: Normal; Level: Bullet Hell",
               20,20,300,300,40,20,50,
               [80,160,240,200,140],[60,50,70,180,240],
               [80,160,240,200,140],[60,50,70,180,240],
               [True,True,True,True,True],[True,True,True,True,True]),
        Level ("Bad speed: Normal; Level: Windows of Opportunity",
               20,20,300,300,40,20,50,
               [60,60,60,60,60,60,60,240,240,240,240,240,240,240,60,60,240,240],
               [40,80,120,160,200,240,280,40,80,120,160,200,240,280,40,80,40,80],
               [40,80,120,160,200,240,280,40,80,120,160,200,240,280,40,80,40,80],
               [60,60,60,60,60,60,60,240,240,240,240,240,240,240,60,60,240,240],
               [True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False],
               [True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False]),
        Level ("Bad speed: Normal; Level: Mirages",
               20,20,300,300,40,20,50,
               [80,80,80,220,220,220,80,80,220,220],
               [60,150,240,60,150,240,60,240,60,240],
               [],[],
               [True,True,True,True,True,True,False,False,False,False,False,False,],[]),
        Level ("Bad speed: Normal; Level: Trio of Trios",
               20,20,300,300,40,20,50,
               [],[],
               [80,80,80,180,180,180,280,280,280],[40,70,100,140,170,200,240,270,300],
               [],[True,True,True,True,True,True,True,True,True]),
        Level ("Bad speed: Normal; Level: Grids",
               20,20,300,300,40,20,50,
               [120,120,180,180,120,120,180,180],
               [120,180,120,180,120,180,120,180],
               [120,120,180,180,120,120,180,180],
               [120,180,120,180,120,180,120,180],
               [True,True,True,True,False,False,False,False],
               [True,True,True,True,False,False,False,False]),
        Level ("Bad speed: Normal; Level: Two Doors",
               20,20,300,300,40,20,50,
               [],[],
               [80,80,80,80,80,80,80,260,260,260,260,260,260,260],
               [40,70,100,130,220,250,280,40,70,100,130,160,190,280],
               [],[True,True,True,True,True,True,True,True,True,True,True,True,True,True]),
        Level("Bad speed: Slow; Level: Raindrops",
              20,20,300,300,40,20,50,
              [40,40,40,40,80,80,80,80,120,120,120,120,160,160,160,160,200,200,200,200,240,240,240,240,280,280,280,280],
              [40,60,80,100,220,240,260,280,160,180,200,220,60,80,100,120,240,260,280,300,100,120,140,160,200,220,240,260],
              [],[],[False,False,False,False,False,False,False,False,False,False,False,False,False,
                     False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],[]),
        Level ("Bad speed: Normal; Level: Confusing Pattern",
               20,20,300,300,40,40,50,
               [40,80,120,160,200,240],[40,80,120,160,200,240],
               [40,80,120,160,200,240],[40,80,120,160,200,240],
               [True,False,True,False,True,False],[True,False,True,False,True,False]),
        Level ("Bad speed: Normal; Level: ",
               20,20,300,300,40,40,50,
               [],
               [],
               [],
               [],
               [True,True,True,True,True,True,True,True,True,True,True,True],
               [True,True,True,True,True,True,True,True,True,True,True,True]),
        Level ("Bad speed: Normal; Level: Quiltmaking",
               20,20,280,500,40,40,50,
               [40,120,200,280,80,160,240],[40,40,40,40,500,500,500],
               [40,40,40,280,280],[80,160,240,120,200],
               [True,True,True,True,True,True,True],[True,True,True,True,True])
              
    ]
print(len(levels))
class nice_item():
    def __init__(self,config_list, canvas,color,bad = False):
        global h
        if color=="red": print(config_list)
        self.c = canvas
        self.config_list = config_list # x_start,y_start,x_end, y_end
        self.main_item = self.c.create_rectangle(tuple(self.config_list), fill=color)
        if bad:
            self.move_by = current.bad_move_by
        else:
            self.move_by = current.moveby
    def up(self):
        if self.config_list[1] > 0:
            self.config_list[1] -= self.move_by
            self.config_list[3] -= self.move_by
            self.update()
        
    def down(self):
        if self.config_list[3] < current.h:
            self.config_list[1] += self.move_by
            self.config_list[3] += self.move_by
            self.update()
        
    def right(self):
        if self.config_list[2] < current.w:
            self.config_list[0] += self.move_by
            self.config_list[2] += self.move_by
            self.update()
        
    def left(self):
        if self.config_list[0] > 0:
            self.config_list[0] -= self.move_by
            self.config_list[2] -= self.move_by
            self.update()
            
    def update(self):
        global current
        #print(gameover)
        check_if_collision(badhorizontal,canvas.main,goal)
        check_if_collision(badvertical,canvas.main,goal)
        #print(gameover)
        if not current.gameover:
            self.c.coords(self.main_item,tuple(self.config_list))
            if not current.started and not current.gameover:
                canvas.master.after(current.event_after,lambda: update(badhorizontal,badvertical))
                current.started = True
                canvas.f.pack_forget()
class my_canvas(Canvas):
    def __init__(self,level,description):
        self.master = Tk()
        self.master.wm_title("Level "+str(level+1)+". Press Esc to quit")
        self.c = Canvas(self.master,width=current.w,height=current.h)
        self.f = Frame(self.master,width=current.w,height=current.h/6)
        titletext = "Level "+str(level+1)+"\n"+current.description
        self.title = Label(self.f,text=titletext)
        self.title.pack()
        #self.title = self.c.create_text(current.w/2,current.h/2,text=titletext)
        x_start = 0
        y_start = current.h - current.how_big
        x_end = current.how_big
        y_end = current.h
        self.config_list = [x_start,y_start,x_end,y_end]
        self.start_config = [x_start,y_start,x_end,y_end]
        self.main = nice_item(self.config_list,self.c,"red")
        self.master.focus_force()
        self.c.focus_set()
        self.c.bind("<Right>",lambda c: self.main.right())
        self.c.bind("<Left>",lambda d: self.main.left())
        self.c.bind("<Up>",lambda a: self.main.up())
        self.c.bind("<Down>",lambda b: self.main.down())
        self.c.bind("<Escape>",lambda e: self.quitcanvas())
        self.f.pack()
        self.c.pack()
        
    def quitcanvas(self):
        global escape
        escape = True
        self.master.destroy()
class Bad(nice_item):
    def __init__(self, end_cords ,canvas, vertical,color):
        self.vertical = vertical
        self.config_list = [end_cords[0] - current.how_big_bad, end_cords[1] - current.how_big_bad]
        for i in end_cords:
            self.config_list.append(i)
        super().__init__(self.config_list, canvas,color,True)

def collision(bads,good):
    r = False
    for bad in bads:
        #[0, 430, 20, 450]
        x_overlap = (bad.config_list[2] > good.config_list[0] and bad.config_list[0] < good.config_list[2]) or (bad.config_list[2] < good.config_list[0] and bad.config_list[0] > good.config_list[2])
        y_overlap = (bad.config_list[3] < good.config_list[1] and bad.config_list[1] > good.config_list[3]) or (bad.config_list[3] > good.config_list[1] and bad.config_list[1] < good.config_list[3]) 
        if x_overlap and y_overlap:
            r = True
            break
    return r
def check_if_collision(bads,good,target):
    if collision(bads,good) and not current.gameover:
        current.gameover = True
        canvas.master.destroy()
    if collision([target],good) and not current.gameover:
        current.gameover = True
        current.victory = True
        canvas.master.destroy()

def update(badhorizontal,badvertical):
    for i in range(len(badhorizontal)):
        if current.rights[i]:
            if badhorizontal[i].config_list[0] >= current.w-current.how_big_bad:
                current.rights[i] = False
                badhorizontal[i].left()
            else:
                badhorizontal[i].right()
        else:
            if badhorizontal[i].config_list[0] <= 0:
                current.rights[i] = True
                badhorizontal[i].right()
            else:
                badhorizontal[i].left()
    for i in range(len(badvertical)):
        if current.ups[i]:
            if badvertical[i].config_list[1] <= 0:
                current.ups[i] = False
                badvertical[i].down()
            else:
                badvertical[i].up()
        else:
            if badvertical[i].config_list[1] >= current.h-current.how_big_bad:
                current.ups[i] = True
                badvertical[i].up()
            else:
                badvertical[i].down()

    if not current.gameover:
        canvas.master.after(current.event_after,lambda: update(badhorizontal,badvertical))
escape = False
while not escape and level < len(levels):
    current = copy.deepcopy(levels[level])
    #print(current.ups,levels[level].ups)
    current.gameover = False
    current.started = False
    canvas = my_canvas(level,current.description)
    badhorizontal = []
    badvertical = []
    for i in range(len(current.horizontalxs)):
        x=current.horizontalxs[i]
        y=current.horizontalys[i]
        badhorizontal.append(Bad([x,y],canvas.c,False,"blue"))
    # ENTER LOCATION (X) OF BOXES(VERTICAL TRAVELLERS)

    for i in range(len(current.verticalxs)):
        y = current.verticalys[i]
        x = current.verticalxs[i]
        badvertical.append(Bad([x,y],canvas.c,True,"cyan"))

    goal = nice_item([current.w-current.how_big,0,current.w,current.how_big],canvas.c,"green")
    canvas.master.mainloop()
    if current.victory:
        level += 1


