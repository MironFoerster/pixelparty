"""
a=input("Gib deinen Text ein: ")
a=a.replace("e", "elewe")
a=a.replace("a", "alewa")
a=a.replace("i", "ilewi")
a=a.replace("o", "olewo")
a=a.replace("u", "ulewu")
a=a.replace("ä", "älewä")
a=a.replace("ö", "ölewö")
a=a.replace("ü", "ülewü")
print(a)
"""
"""
lastindex=None
index=[]
boolean=True
a=input("Gib deinen Text ein: ")
for i in letters:
    lastindex=a.rfind(i)
    while boolean:
        index.append(a.find(i))
        if lastindex in index:
            break
    
print()

letters=["ie","Ie","ei","Ei","au","Au","eu","Eu","e","E","a","A","i","I","o","O","u","U","ä","Ä","ö","Ö","ü","Ü"]
"""
"""
#Sprachausgabe
txt=input("Gib deinen Text ein: ")
for i in txt:
    if i==h:
 """
"""
#beep
import winsound
winsound.Beep(520,300)#C
winsound.Beep(550,300)#Cis
winsound.Beep(590,300)#D
winsound.Beep(620,300)#Dis
winsound.Beep(660,300)#E
winsound.Beep(700,300)#F
winsound.Beep(740,300)#Fis
winsound.Beep(780,300)#G
winsound.Beep(830,300)#Gis
winsound.Beep(880,300)#A
winsound.Beep(930,300)#Ais
winsound.Beep(990,300)#H
winsound.Beep(1050,300)#C
winsound.Beep(990,300)#H
winsound.Beep(930,300)#Ais
winsound.Beep(880,300)#A
winsound.Beep(830,300)#Gis
winsound.Beep(780,300)#G
winsound.Beep(740,300)#Fis
winsound.Beep(700,300)#F
winsound.Beep(660,300)#E
winsound.Beep(620,300)#Dis
winsound.Beep(590,300)#D
winsound.Beep(550,300)#Cis
winsound.Beep(520,300)#C
"""


#play sound
import winsound

data=open("Alarm01.wav")
winsound.PlaySound("Alarm01.wav",winsound.SND_FILENAME)

