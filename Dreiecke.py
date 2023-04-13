"""
Gib deine Dreiecksseiten durch Kommata getrennt an(a,b,c).
Wähle danach aus den Optionen aus:
1)... längste Seiten ermitteln
2)... können die Seiten ein Dreieck bilden?
3)... ist das Dreieck rechtwinklig?
"""

import tkinter

def text():
    t=open("dreiecke.txt")
    ln=t.readline()
    while ln:
        txt.insert("end",ln)
        ln=t.readline()

def getinput():
    eingabe=e.get()
    eingabe=eingabe.split(",")
    try:
        a,b,c=eingabe
        for i in a,b,c:
            i=int(i)
        return a,b,c
    except:
        return False
        
        
    
def laengste():
    eingabe=e.get()
    eingabe=eingabe.split(",")
    try:
        a,b,c=eingabe #nur test, ob es 3 werte sind :)
        for i in eingabe:
            i=int(i)

        
    except:
        lbout["text"]="Fehler bei der Eingabe!"
    
    if getinput():
        a,b,c=getinput()
        mx=max(a,b,c)
        lbout["text"]="Die laengste Seite ist: "+str(mx)
    else:
        lbout["text"]="Fehler bei der Eingabe!"+str(getinput())

def moeglich():
    pass

def recht():
    pass

main = tkinter.Tk()

txt=tkinter.Text(main,width=60,height=5,bg="#EEEEEE")


e=tkinter.Entry(main)

lbout=tkinter.Label(main,height=1)

b1=tkinter.Button(main,text="1",command=laengste,width=10)
b2=tkinter.Button(main,text="2",command=moeglich,width=10)
b3=tkinter.Button(main,text="3",command=recht,width=10)

text()
txt.pack()
e.pack()
lbout.pack()
for i in 1,2,3:
    eval("b"+str(i)).pack()

main.mainloop()

