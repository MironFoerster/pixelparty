import pygame,time
print("wurfsimulator")
window=pygame.display.set_mode((500,500))

while True:
    h=int(input("Höhe(in px):"))
    g=10
    vx=int(input("Geschwindigkeit(in px/s):"))

    for t in range(int(((2*h)/g)**0.5)):        
        x=int(vx*t)
        y=int((g*(t**2))/2+(500-h))
        pygame.draw.circle(window,(255,0,0),(x,y),3)
        pygame.display.update()
        time.sleep(1)
    print("-"*50)
    if input("Clear Display?(1/0)")==1:
        window.fill((0,0,0))
        pygame.display.update()
