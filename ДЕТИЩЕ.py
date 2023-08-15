import tkinter as tk
from textwrap import wrap
from tkinter import messagebox
import winsound
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
window = tk.Tk()
#splash_win= tk.Tk()
#splash_win.attributes('-topmost',True)

#splash_win.title("Splash Screen Example")
#w = 1200 # width for the Tk root
#h = 770 # height for the Tk root

# get screen width and height
#ws = splash_win.winfo_screenwidth() # width of the screen
#hs = splash_win.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
#x = (ws/2) - (w/2)
#y = (hs/2) - (h/2)
"""
# set the dimensions of the screen 
# and where it is placed
splash_win.geometry('%dx%d+%d+%d' % (w, h, x, y))
def spah():
    splash_win.destroy()
splash_win.overrideredirect(True)
splash_label= tk.Label(splash_win, text= "КАЛЬКУЛЯТОР ЛЫСИ", fg= "green",bg="black", font= ('Times New Roman', 40)).grid(pady=300, padx=300)
splash_win.after(6000, spah)






pygame.mixer.init()
song_1 = pygame.mixer.Sound('music.wav')
song_1.play()
music=1
    
"""
window.title("Калькулятор ВИЛСОНА")
skcount=0
k=0


lbl = tk.Label(text="0",font=("Times New Roman", 25, "bold"))

lbl.grid(row=0, column=0,columnspan=5)
zn=["+", "-", "*", "/","^","("]
#функции кнопок
def com1():
    bproc["state"] = "normal"
    b0["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    bstep["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "1"
    elif len(lbl["text"])<54:
        lbl["text"] = lbl["text"]+"1"
         
        window.update()
        width = lbl.winfo_width()
         
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
    if sound==1: winsound.PlaySound('sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
def com2():
    bproc["state"] = "normal"
    b0["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    bstep["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "2"
    elif len(lbl["text"])<54:
        lbl["text"] = lbl["text"]+"2"
         
        window.update()
        width = lbl.winfo_width()
         
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
    #if sound==1: winsound.PlaySound('sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
def com3():
    #if sound==1: winsound.PlaySound('sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    bproc["state"] = "normal"
    b0["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    bstep["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "3"
    elif len(lbl["text"])<54:
        lbl["text"] = lbl["text"]+"3"
         
        window.update()
        width = lbl.winfo_width()
         
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
def com4():
    #if sound==1: winsound.PlaySound('sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    bproc["state"] = "normal"
    b0["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    bstep["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "4"
    elif len(lbl["text"])<54:
        lbl["text"] = lbl["text"]+"4"
         
        window.update()
        width = lbl.winfo_width()
         
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
def com5():
    #if sound==1: winsound.PlaySound('sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    bproc["state"] = "normal"
    b0["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    bstep["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "5"
    elif len(lbl["text"])<54:
        lbl["text"] = lbl["text"]+"5"
         
        window.update()
        width = lbl.winfo_width()
         
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
def com6():
    #if sound==1: winsound.PlaySound('sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    bproc["state"] = "normal"
    b0["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    bstep["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "6"
    elif len(lbl["text"])<54:
        lbl["text"] = lbl["text"]+"6"
         
        window.update()
        width = lbl.winfo_width()
         
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
def com7():
    #if sound==1: winsound.PlaySound('sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    bproc["state"] = "normal"
    b0["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    bstep["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "7"
    elif len(lbl["text"])<54:
        lbl["text"] = lbl["text"]+"7"
         
        window.update()
        width = lbl.winfo_width()
         
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
def com8():
    #if sound==1: winsound.PlaySound('sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    bproc["state"] = "normal"
    b0["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    bstep["state"] = "normal"

    
    if lbl["text"] =="0":
        lbl["text"] = "8"
    elif len(lbl["text"])<54:
        lbl["text"] = lbl["text"]+"8"
        
         
        window.update()
        width = lbl.winfo_width()
         
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!") 

def com9():
    #if sound==1: winsound.PlaySound('sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    bproc["state"] = "normal"
    b0["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    bstep["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "9"
    elif len(lbl["text"])<54:
        lbl["text"] = lbl["text"]+"9"
         
        window.update()
        k=0
        width = lbl.winfo_width()
         
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")


def com0():
    #if sound==1: winsound.PlaySound('sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    bproc["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    bstep["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "0"
    elif len(lbl["text"])<54:
        lbl["text"] = lbl["text"]+"0"
         
        window.update()
        width = lbl.winfo_width()
        
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
    if lbl["text"][-2] in zn:
            b0["state"] = "disable"
            b9["state"] = "disable"
            b8["state"] = "disable"
            b7["state"] = "disable"
            b6["state"] = "disable"
            b5["state"] = "disable"
            b4["state"] = "disable"
            b3["state"] = "disable"
            b2["state"] = "disable"
            b1["state"] = "disable"
        

def comdelet():
    
    b0["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    bproc["state"] = "normal"
    bstep["state"] = "disabled"
    b9["state"] = "normal"
    b8["state"] = "normal"
    b7["state"] = "normal"
    b6["state"] = "normal"
    b5["state"] = "normal"
    b4["state"] = "normal"
    b3["state"] = "normal"
    b2["state"] = "normal"
    b1["state"] = "normal"
    
    if len(lbl["text"]) ==1:
        lbl["text"] = "0"
    else:
       lbl["text"] = lbl["text"][0:-1]
    

def compl():
    bpl["state"] = "disabled"
    bmin["state"] = "disabled"
    bumn["state"] = "disabled"
    bdel["state"] = "disabled"
    bans["state"] = "disabled"
    bproc["state"] = "disabled"
    bstep["state"] = "disabled"
    b0["state"] = "normal"
    b9["state"] = "normal"
    b8["state"] = "normal"
    b7["state"] = "normal"
    b6["state"] = "normal"
    b5["state"] = "normal"
    b4["state"] = "normal"
    b3["state"] = "normal"
    b2["state"] = "normal"
    b1["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "0"
    elif len(lbl["text"])<54:
        if lbl["text"][-1] not in zn:
            lbl["text"] = lbl["text"]+"+"
            window.update()
            width = lbl.winfo_width()
            if width > 450:
                char_width = width / len(lbl['text'])
                wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
                lbl['text'] = wrapped_text
        else:
            tk.messagebox.showerror(title="Ошибка!", message="Недопустимый формат")
            
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
def commin():
    bpl["state"] = "disabled"
    bmin["state"] = "disabled"
    bumn["state"] = "disabled"
    bans["state"] = "disabled"
    bdel["state"] = "disabled"
    bproc["state"] = "disabled"
    bstep["state"] = "disabled"
    b0["state"] = "normal"
    b9["state"] = "normal"
    b8["state"] = "normal"
    b7["state"] = "normal"
    b6["state"] = "normal"
    b5["state"] = "normal"
    b4["state"] = "normal"
    b3["state"] = "normal"
    b2["state"] = "normal"
    b1["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "0"
    elif len(lbl["text"])<54:
        if lbl["text"][-1] not in zn:
            lbl["text"] = lbl["text"]+"-"
            window.update()
            width = lbl.winfo_width()
            if width > 450:
                char_width = width / len(lbl['text'])
                wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
                lbl['text'] = wrapped_text
        else:
            tk.messagebox.showerror(title="Ошибка!", message="Недопустимый формат")
            
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
def comumn():
    bpl["state"] = "disabled"
    bmin["state"] = "disabled"
    bumn["state"] = "disabled"
    bans["state"] = "disabled"
    bdel["state"] = "disabled"
    bproc["state"] = "disabled"
    bstep["state"] = "disabled"
    b9["state"] = "normal"
    b8["state"] = "normal"
    b7["state"] = "normal"
    b6["state"] = "normal"
    b5["state"] = "normal"
    b4["state"] = "normal"
    b3["state"] = "normal"
    b2["state"] = "normal"
    b1["state"] = "normal"
    if lbl["text"] =="0":
        lbl["text"] = "0"
    elif len(lbl["text"])<54:
        if lbl["text"][-1] not in zn:
            lbl["text"] = lbl["text"]+"*"
            window.update()
            width = lbl.winfo_width()
            if width > 450:
                char_width = width / len(lbl['text'])
                wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
                lbl['text'] = wrapped_text
        else:
            tk.messagebox.showerror(title="Ошибка!", message="Недопустимый формат")
            
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
def comdel():
    bpl["state"] = "disabled"
    bmin["state"] = "disabled"
    bumn["state"] = "disabled"
    bans["state"] = "disabled"
    bdel["state"] = "disabled"
    bproc["state"] = "disabled"
    bstep["state"] = "disabled"
    b9["state"] = "normal"
    b8["state"] = "normal"
    b7["state"] = "normal"
    b6["state"] = "normal"
    b5["state"] = "normal"
    b4["state"] = "normal"
    b3["state"] = "normal"
    b2["state"] = "normal"
    b1["state"] = "normal"

    
    if lbl["text"] =="0":
        lbl["text"] = "0"
    elif len(lbl["text"])<54:
        if lbl["text"][-1] not in zn:
            lbl["text"] = lbl["text"]+"/"
            b0["state"] = "disabled"
            window.update()
            width = lbl.winfo_width()
            if width > 450:
                char_width = width / len(lbl['text'])
                wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
                lbl['text'] = wrapped_text
        else:
            tk.messagebox.showerror(title="Ошибка!", message="Недопустимый формат")
            
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
def comproc():
    bproc["state"] = "disabled"
    if lbl["text"] =="0":
        lbl["text"] = "0"
    elif len(lbl["text"])<54:
        if lbl["text"][-1] not in zn:
            lbl["text"] = lbl["text"]+"%"
            ct=1
            window.update()
            width = lbl.winfo_width()
            if width > 450:
                char_width = width / len(lbl['text'])
                wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
                lbl['text'] = wrapped_text
        else:
            tk.messagebox.showerror(title="Ошибка!", message="Недопустимый формат")
            
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
def comans():
    anns=lbl["text"].replace('%','*0.01')
    anns=anns.replace('^','**')
    anns=anns.replace('1(','1*(')
    anns=anns.replace('2(','2*(')
    anns=anns.replace('3(','3*(')
    anns=anns.replace('4(','4*(')
    anns=anns.replace('5(','5*(')
    anns=anns.replace('6(','6*(')
    anns=anns.replace('7(','7*(')
    anns=anns.replace('8(','8*(')
    anns=anns.replace('9(','9*(')
    anns=anns.replace('0(','0*(')

    anns=anns.replace(')(',')*(')
    anns=anns.replace(')1',')*1')
    anns=anns.replace(')2',')*2')
    anns=anns.replace(')3',')*3')
    anns=anns.replace(')4',')*4')
    anns=anns.replace(')5',')*5')
    anns=anns.replace(')6',')*6')
    anns=anns.replace(')7',')*7')
    anns=anns.replace(')8',')*8')
    anns=anns.replace(')9',')*9')
    anns=anns.replace(')0',')*0')
    try:eval(anns)
    except Exception as e:
        tk.messagebox.showerror(title="Ошибка!", message=e)
        global k
        k=1
    if (k!=1) and (skcount==0):
            lbl['text'] = str(int(eval(anns)))
    k=0

def comcan():
    #if sound==1: winsound.PlaySound('cancel.txt', winsound.SND_ALIAS | winsound.SND_ASYNC)
    lbl["text"] ="0"
    skcount=0
    b0["state"] = "normal"
    b9["state"] = "normal"
    b8["state"] = "normal"
    b7["state"] = "normal"
    b6["state"] = "normal"
    b5["state"] = "normal"
    b4["state"] = "normal"
    b3["state"] = "normal"
    b2["state"] = "normal"
    b1["state"] = "normal"

def comstep():
    bproc["state"] = "disable"
    
    bstep["state"] = "disabled"
    bpl["state"] = "disable"
    
    bumn["state"] = "disable"
    bans["state"] = "disable"
    bdel["state"] = "disable"
    if lbl["text"] =="0":
        lbl["text"] = "0"
    elif len(lbl["text"])<54:
        lbl["text"] = lbl["text"]+"^"
        
         
        window.update()
        width = lbl.winfo_width()
         
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
    


def comskob():
    global skcount
    bproc["state"] = "normal"
    b0["state"] = "normal"
    bpl["state"] = "normal"
    bmin["state"] = "normal"
    bumn["state"] = "normal"
    bans["state"] = "normal"
    bdel["state"] = "normal"
    
    if lbl["text"] =="0":
        lbl["text"] = "("
        skcount=skcount+1
    elif len(lbl["text"])<54:
        if (lbl["text"][-1] in zn) or (skcount==0) :
            lbl["text"] = lbl["text"]+"("
            skcount=skcount+1
            bstep["state"] = "disabled"
            bproc["state"] = "disabled"
            bpl["state"] = "disabled"
            bmin["state"] = "disabled"
            bumn["state"] = "disabled"
            bans["state"] = "disabled"
            bdel["state"] = "disabled"
        else:
            
            lbl["text"] = lbl["text"]+")"
            skcount=skcount-1
            
        
         
        window.update()
        width = lbl.winfo_width()
         
        if width > 450:
            char_width = width / len(lbl['text'])
            wrapped_text = '\n'.join(wrap(lbl['text'], int(450 / char_width)))
            lbl['text'] = wrapped_text
    else:
        tk.messagebox.showerror(title="Ошибка!", message="Слишком много текста!")
#задаем кнопки
       
b1 = tk.Button(text="1",width=25,height=5,bg="black",fg="white",font=("Times New Roman", 13),command = com1)
b1.grid( row=4, column=0)

b2 = tk.Button(text="2",width=25,height=5,bg="black",fg="white",font=("Times New Roman", 13),command = com2)
b2.grid(row=4, column=1)

b3 = tk.Button(text="3",width=25,height=5,bg="black",fg="white",font=("Times New Roman", 13),command = com3)
b3.grid( row=4, column=2)

b4 = tk.Button(text="4",width=25,height=5,bg="black",fg="white",font=("Times New Roman", 13),command = com4)
b4.grid(row=3, column=0)
b5 = tk.Button(text="5",width=25,height=5,bg="black",fg="white",font=("Times New Roman", 13),command = com5)
b5.grid( row=3, column=1)

b6 = tk.Button(text="6",width=25,height=5,bg="black",fg="white",font=("Times New Roman", 13),command = com6)
b6.grid(row=3, column=2)

b7 = tk.Button(text="7",width=25,height=5,bg="black",fg="white",font=("Times New Roman", 13),command = com7)
b7.grid( row=2, column=0)

b8 = tk.Button(text="8",width=25,height=5,bg="black",fg="white",font=("Times New Roman", 13),command = com8)
b8.grid(row=2, column=1)

b9 = tk.Button(text="9",width=25,height=5,bg="black",fg="white",font=("Times New Roman", 13),command = com9)
b9.grid(row=2, column=2)

b0 = tk.Button(text="0",width=25,height=5,bg="black",fg="white",font=("Times New Roman", 13),command = com0)
b0.grid(row=5, column=1)



bdelet = tk.Button(text="⌫",width=25,height=5,bg="black",fg="green2",font=("Times New Roman", 13),command = comdelet)
bdelet.grid( row=1, column=1)

bpl = tk.Button(text="+",width=25,height=5,bg="black",fg="green2",font=("Times New Roman", 13),command = compl)
bpl.grid( row=4, column=3)

bmin = tk.Button(text="-",width=25,height=5,bg="black",fg="green2",font=("Times New Roman", 13),command = commin)
bmin.grid( row=3, column=3)

bumn = tk.Button(text="x",width=25,height=5,bg="black",fg="green2",font=("Times New Roman", 13),command = comumn)
bumn.grid( row=2, column=3)

bdel = tk.Button(text=":",width=25,height=5,bg="black",fg="green2",font=("Times New Roman", 13),command = comdel)
bdel.grid( row=1, column=3)

bproc= tk.Button(text="%",width=25,height=5,bg="black",fg="green2",font=("Times New Roman", 13),command = comproc)
bproc.grid( row=1, column=2)

bans = tk.Button(text="=",width=25,height=5,bg="green",fg="white",font=("Times New Roman", 13),command = comans)
bans.grid( row=5, column=3)

bcan = tk.Button(text="C",width=25,height=5,bg="black",fg="red",font=("Times New Roman", 13),command = comcan)
bcan.grid( row=1, column=0)



bstep = tk.Button(text="^",width=25,height=5,bg="black",fg="green2",font=("Times New Roman", 13),command = comstep)
bstep.grid( row=5, column=0)

bskob = tk.Button(text="( )",width=25,height=5,bg="black",fg="green2",font=("Times New Roman", 13),command = comskob)
bskob.grid( row=5, column=2)




"""
#####
def comsound():
    global sound
    
    if sound==1:
        
        bsound.configure(image=click_btn1)
        sound=0
    else:
        bsound.configure(image=click_btn)
        sound=1
        
        
click_btn= tk.PhotoImage(file='clickme.png')
click_btn1= tk.PhotoImage(file='clickme1.png')
sound=1
img_label= tk.Label(image=click_btn)
img_label1= tk.Label(image=click_btn1)
bsound = tk.Button(image=click_btn,command= comsound, borderwidth=0)
bsound.grid( row=0, column=3)
#####
def commusic():
    global music
    
    if music==1:
        song_1.stop()
        bmusic.configure(image=click_btn3)
        music=0
        
    else:
        bmusic.configure(image=click_btn2)
        music=1
        song_1.play(0)
        
        
        
        
click_btn2= tk.PhotoImage(file='musicon.png')
click_btn3= tk.PhotoImage(file='musicoff.png')

img_label= tk.Label(image=click_btn2)
img_label1= tk.Label(image=click_btn3)
bmusic = tk.Button(image=click_btn2,command= commusic, borderwidth=0)
bmusic.grid( row=0, column=0)

"""


###############



window.mainloop()

