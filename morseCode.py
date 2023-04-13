import winsound as ws
import time as t

lttrs={".":".-.-.- ",",":"--..-- ","?":"..--.. ","!":"-.-.-- ",":":"---... ","=":"-...- ","+":".-.-. ","-":"-....- ","1":".---- ","2":"..--- ","3":"...-- ","4":"....- ","5":"..... ","6":"-.... ","7":"--... ","8":"---.. ","9":"----. ","0":"----- ","a":".- ","b":"-... ","c":"-.-. ","d":"-.. ","e":". ","f":"..-. ","g":"--. ","h":".... ","i":".. ","j":".--- ","k":"-.- ","l":".-.. ","m":"-- ","n":"-. ","o":"--- ","p":".--. ","q":"--.- ","r":".-. ","s":"... ","t":"- ","u":"..- ","v":"...- ","w":".-- ","x":"-..- ","y":"-.-- ","z":"--.. ","z":"--.. ","z":"--.. ","z":"--.. ","z":"--.. ","A":".- ","B":"-... ","C":"-.-. ","D":"-.. ","E":". ","F":"..-. ","G":"--. ","H":".... ","I":".. ","J":".--- ","K":"-.- ","L":".-.. ","M":"-- ","N":"-. ","O":"--- ","P":".--. ","Q":"--.- ","R":".-. ","S":"... ","T":"- ","U":"..- ","V":"...- ","W":".-- ","X":"-..- ","Y":"-.-- ","Z":"--.. "," ":"\n"}
beeps={".":100,"-":300}
waits={" ":0.3,"\n":0.6}

def schrift(cd):
    for i in txt:
        cd+=lttrs[i]
    print(cd)

def ton(cd):
    for i in txt:
        cd+=lttrs[i]
    for i in cd:
        if i=="."or i=="-":
            ws.Beep(1000,beeps[i])
        elif i==" "or i=="\n":
            t.sleep(waits[i])
"""
def beide(cd):
    for i in txt:
        cd+=lttrs[i]
    for i in range(len(cd)):
        print(cd[i])
        if cd[i]=="."or i=="-":
            ws.Beep(1000,beeps[cd[i]])
        elif cd[i]==" "or i=="\n":
            t.sleep(waits[cd[i]])
"""
while True:
    code=""
    txt=input("Gib den, in den Morsecode\nzu übersetzenden, Text ein: ")
    art=input("\nSoll der Code akustisch, schriftlich\noder auf beide Arten ausgegeben werden?(a/s/b) ")
    art=art.lower()

    if art.startswith("a"):
        ton(code)
    elif art.startswith("s"):
        schrift(code)
    elif art.startswith("b"):
        schrift(code)
        ton(code)
    else:
        print("Du hast keine Ausgabeart angegeben.")
    
    
