from tkinter import Button, Frame, Listbox, Tk, Listbox, Radiobutton
from tkinter.constants import MULTIPLE
from os import mkdir, system

try:
    from clipboard import copy
except:
    system("pip install clipboard")
    from clipboard import copy

from datetime import datetime as dtm

try:
    from discord_webhook import DiscordWebhook
except:
    system("pip install discord-webhook")
    from discord_webhook import DiscordWebhook

phy = []
math = []
eng = []
chem = []
comp = []

# A section
with open(r"physicsa.txt", "r") as f:
    stud = f.readlines()

phy.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"chemistrya.txt", "r") as f:
    stud = f.readlines()

chem.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"mathsa.txt", "r") as f:
    stud = f.readlines()

math.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"englisha.txt", "r") as f:
    stud = f.readlines()

eng.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"pythona.txt", "r") as f:
    stud = f.readlines()

comp.append(list(map(lambda ppl: ppl.strip(), stud)))

# B section
with open(r"physicsb.txt", "r") as f:
    stud = f.readlines()

phy.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"chemistryb.txt", "r") as f:
    stud = f.readlines()

chem.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"mathsb.txt", "r") as f:
    stud = f.readlines()

math.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"englishb.txt", "r") as f:
    stud = f.readlines()

eng.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"pythonb.txt", "r") as f:
    stud = f.readlines()

comp.append(list(map(lambda ppl: ppl.strip(), stud)))

# C section
with open(r"physicsc.txt", "r") as f:
    stud = f.readlines()

phy.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"chemistryc.txt", "r") as f:
    stud = f.readlines()

chem.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"mathsc.txt", "r") as f:
    stud = f.readlines()

math.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"englishc.txt", "r") as f:
    stud = f.readlines()

eng.append(list(map(lambda ppl: ppl.strip(), stud)))

with open(r"pythonc.txt", "r") as f:
    stud = f.readlines()

comp.append(list(map(lambda ppl: ppl.strip(), stud)))


def disc(cont):
    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/841270336166428672/sQa-KwKDMw6-eRoG9FBd5-o4CG5_EQd0CVeOMtPQpCwYHU3ghYfEW_dJmWlF_yzjy9S_', content=cont)
    webhook.execute()


root = Tk()
root.title("Basic Attendance Helper")
root.geometry("860x610+200+50")


radf = Frame(root).grid(column=0,row=0)


var = ""


attf = Frame(root).grid(column=0,row=5)

peoplea = Listbox(attf,selectmode=MULTIPLE,width=30,height=30,exportselection=0)  #,yscrollcommand=scrollbar.set)
peopleb = Listbox(attf,selectmode=MULTIPLE,width=30,height=30,exportselection=0)  #,yscrollcommand=scrollbar.set)
peoplec = Listbox(attf,selectmode=MULTIPLE,width=30,height=30,exportselection=0)  #,yscrollcommand=scrollbar.set)
peopleabs = Listbox(attf,width=30,height=30)

def lst1():
    peoplea.delete(0,"end")
    peopleb.delete(0,"end")
    peoplec.delete(0,"end")
    global var
    var = "eng"
    c = 0
    for i in range(3):
        for ppl in eng[i]:
            if i == 0:
                peoplea.insert(c,str(c+1)+">"+ppl)
            if i == 1:
                peopleb.insert(c,str(c+1)+">"+ppl)
            if i == 2:
                peoplec.insert(c,str(c+1)+">"+ppl)
            c += 1
    peoplea.grid(column=0,row=3)
    peopleb.grid(column=1,row=3)
    peoplec.grid(column=2,row=3)

def lst2():
    peoplea.delete(0,"end")
    peopleb.delete(0,"end")
    peoplec.delete(0,"end")
    global var
    var = "math"
    c = 0
    for i in range(3):
        for ppl in math[i]:
            if i == 0:
                peoplea.insert(c,str(c+1)+">"+ppl)
            if i == 1:
                peopleb.insert(c,str(c+1)+">"+ppl)
            if i == 2:
                peoplec.insert(c,str(c+1)+">"+ppl)
            c += 1
    peoplea.grid(column=0,row=3)
    peopleb.grid(column=1,row=3)
    peoplec.grid(column=2,row=3)

def lst3():
    peoplea.delete(0,"end")
    peopleb.delete(0,"end")
    peoplec.delete(0,"end")
    global var
    var = "phy"
    c = 0
    for i in range(3):
        for ppl in phy[i]:
            if i == 0:
                peoplea.insert(c,str(c+1)+">"+ppl)
            if i == 1:
                peopleb.insert(c,str(c+1)+">"+ppl)
            if i == 2:
                peoplec.insert(c,str(c+1)+">"+ppl)
            c += 1
    peoplea.grid(column=0,row=3)
    peopleb.grid(column=1,row=3)
    peoplec.grid(column=2,row=3)

def lst4():
    peoplea.delete(0,"end")
    peopleb.delete(0,"end")
    peoplec.delete(0,"end")
    global var
    var = "chem"
    c = 0
    for i in range(3):
        for ppl in chem[i]:
            if i == 0:
                peoplea.insert(c,str(c+1)+">"+ppl)
            if i == 1:
                peopleb.insert(c,str(c+1)+">"+ppl)
            if i == 2:
                peoplec.insert(c,str(c+1)+">"+ppl)
            c += 1
    peoplea.grid(column=0,row=3)
    peopleb.grid(column=1,row=3)
    peoplec.grid(column=2,row=3)

def lst5():
    peoplea.delete(0,"end")
    peopleb.delete(0,"end")
    peoplec.delete(0,"end")
    global var
    var = "comp"
    c = 0
    for i in range(3):
        for ppl in comp[i]:
            if i == 0:
                peoplea.insert(c,str(c+1)+">"+ppl)
            if i == 1:
                peopleb.insert(c,str(c+1)+">"+ppl)
            if i == 2:
                peoplec.insert(c,str(c+1)+">"+ppl)
            c += 1
    peoplea.grid(column=0,row=3)
    peopleb.grid(column=1,row=3)
    peoplec.grid(column=2,row=3)

R1 = Radiobutton(radf, text="English", variable=var, value=1, command=lst1)
R1.grid(column=0,row=0)

R2 = Radiobutton(radf, text="Math", variable=var, value=2, command=lst2)
R2.grid(column=1,row=0)

R3 = Radiobutton(radf, text="Physics", variable=var, value=3, command=lst3)
R3.grid(column=0,row=1)

R4 = Radiobutton(radf, text="Chemistry", variable=var, value=4, command=lst4)
R4.grid(column=1,row=1)

R5 = Radiobutton(radf, text="Computer", variable=var, value=5, command=lst5)
R5.grid(column=2,row=0)

pa = tuple()
pb = tuple()
pc = tuple()

def absentees():
    global var
    pna = peoplea.curselection() # -> disp in abs listb -> clipboard copy
    pa = []
    for i in pna:
        pa.append(peoplea.get(i).partition(">")[2])
    pnb = peopleb.curselection()
    pb = []
    for i in pnb:
        pb.append(peopleb.get(i).partition(">")[2])
    pnc = peoplec.curselection()
    pc = []
    for i in pnc:
        pc.append(peoplec.get(i).partition(">")[2]) 

        """ use seperate function to get the name
            adjust size of window
            solve multiple list selection problem """

    la = eval(f"{var}[0]")
    lb = eval(f"{var}[1]")
    lc = eval(f"{var}[2]")

    cnt = 0
    peopleabs.delete(0,"end")
    for n in la:
        if n not in pa:
            peopleabs.insert(cnt,f"{cnt}>{n} -> Sec-A")
            cnt += 1
    for n in lb:
        if n not in pb:
            peopleabs.insert(cnt,f"{cnt}>{n} -> Sec-B")
            cnt += 1
    for n in lc:
        if n not in pc:
            peopleabs.insert(cnt,f"{cnt}>{n} -> Sec-C")
            cnt += 1
    peopleabs.grid(column=3,row=3)
    absts = peopleabs.get(0,"end")
    abstes = ""
    ctn = len(absts)
    abstes += f"{ctn} people absent! \n"
    for ab in absts:
        abb = ab.partition(">")[2]
        abstes += f"{abb} \n"
    copy(abstes)

    dt = dtm.now().strftime("%d%m%Y")
    eman = dt+"."+var
    try:
        mkdir("c:\\basicattd")
    except:
        pass

    ## Abslist in text
    with open(f"c:\\basicattd\\{eman}.txt","w") as f:
        f.write(abstes)
    
    cont = eman+"\n"+abstes
    disc(cont)

    
lstb = Button(radf, text="Get Absentees", command=absentees)
lstb.grid(column=2,row=1)

root.mainloop()