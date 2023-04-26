from turtle import *
import numpy as np
import time

t = Turtle()
screen = Screen()


def Limit(num):
    screen.setup(500, 500)
    t.dot(400, "red")
    t.dot(330, "white")
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.write(num, align="center", font=("Verdana", 130, "bold"))
    t.ht()



def SchoolZone(speed):
    screen.setup(450, 350)
    t.speed(0)
    t.penup(); t.goto(-200, 150); t.pendown(); t.color("yellow")
    t.begin_fill(); t.goto(-200, -150); t.goto(200, -150); t.goto(200, 150); t.goto(-200, 150); t.end_fill()

    t.penup(); t.goto(-185, 135);t.pendown(); t.color("black"); t.pensize(5)
    t.goto(-185, -135); t.goto(185, -135); t.goto(185, 135); t.goto(-185, 135)

    t.penup(); t.goto(0, 60); t.pendown()
    t.write("School Zone", align="center", font=("Verdana", 30, "bold"))

    t.penup(); t.goto(-100, -10); t.pendown(); t.dot(120, "red"); t.dot(90, "white")
    t.penup(); t.goto(-95, -40); t.pendown()
    t.write("30", align="center", font=("Verdana", 40, "bold"))

    t.penup(); t.goto(-20, 40); t.pendown(); t.color("black")
    t.begin_fill(); t.goto(-20, -60); t.goto(150, -60); t.goto(150, 40); t.goto(-20, 40); t.end_fill()

    t.penup(); t.goto(150, -55); t.pendown(); t.color("white")
    t.write(speed, align="right", font=("Verdana", 60, "bold"))

    t.penup(); t.goto(0, -120); t.pendown(); t.color("black")
    t.write("Slow down", align="center", font=("Verdana", 20, "normal"))
    t.ht()


def TWrite(distance, num):
    screen.setup(1000, 400)
    if num == 0:
        txt = "GO"
    elif num == 1:
        txt = "m Traffic Light"
    elif num == 2:
        txt = "m Turn Right"
    elif num == 3:
        txt = "m Entering The HighWay"
    elif num == 6:
        txt = "Soon SchoolZone"
    else:
        txt = "m Out The HighWay"
    if num == 0 or num == 6:
        t.write(txt, align="center", font=("Verdana", 40, "bold"))
    else:
        t.write(str(distance) + txt, align="center", font=("Verdana", 40, "bold"))
    t.ht()

def main(args):
    l_lst = [0, 1, 2, 3, 4, 5]
    h_lst = [0, 1, 2]
    LH_st = 0

    while True:
        prev = 1000
        frt = open('/home/pi/miniproject/trafst.txt', 'r')
        f = open('/home/pi/miniproject/signst.txt', 'w')
        st = int(frt.readline())
        print(st)
        
        if st == 4:
            if LH_st == 1:
                f.write("124")
                f.close()
                ontimer(TWrite(300, 4), 1500)
                while True:
                    t.reset()
                    with open('/home/pi/miniproject/distance.txt', 'r') as frd:
                        distance = int(frd.readline())
                        if prev < distance or distance < 0:
                            ontimer(TWrite(0, 4), 1500)
                            with open('/home/pi/miniproject/signst.txt', 'w') as f:
                                f.write("125")
                                break
                        prev = distance
                        ontimer(TWrite(distance, 4), 1500) 
            else:
                f.write("111")
                f.close()
            screen.bye()
            break
        else:
            if LH_st == 0:
                res = np.random.choice(l_lst, 1, p=[0.2, 0.2, 0.3, 0.1, 0.1, 0.1])
                print("res[0] :", res[0])
                if res[0] == 0:
                    f.write("00")
                    f.close()
                    ontimer(TWrite(0, 0), 5000)
                elif res[0] == 1:
                    f.write("01")
                    f.close()
                    ontimer(Limit(50), 5000)
                elif res[0] == 2:
                    f.write("02")
                    f.close()
                    ontimer(TWrite(0, 6), 4000)
                    t.reset()
                    with open('/home/pi/miniproject/speed.txt', 'r') as frs:
                        speed = int(frs.readline())
                        ontimer(SchoolZone(speed), 4000)
                elif res[0] == 3:
                    f.write("03")
                    f.close()                    
                    ontimer(TWrite(300, 1), 1500)                   
                    while True:
                        t.reset()
                        with open('/home/pi/miniproject/distance.txt', 'r') as frd:
                            distance = int(frd.readline())
                            if prev < distance or distance <= 0:
                                ontimer(TWrite(0, 1), 1500)
                                break
                            prev = distance
                            ontimer(TWrite(distance, 1), 1500) 
                elif res[0] == 4:
                    f.write("04")
                    f.close()                    
                    ontimer(TWrite(300, 2), 1500)
                    while True:
                        t.reset()
                        with open('/home/pi/miniproject/distance.txt', 'r') as frd:
                            distance = frd.readline()
                            if not distance:
                                distance = prevd
                            else:
                                distance = int(distance)
                                prevd = distance
                            if prev < distance or distance < 0:
                                ontimer(TWrite(0, 2), 1500)
                                break
                            prev = distance
                            ontimer(TWrite(distance, 2), 1500) 
                elif res[0] == 5:
                    f.write("05")
                    f.close()
                    LH_st = 1
                    ontimer(TWrite(300, 3), 1500)
                    while True:
                        t.reset()
                        with open('/home/pi/miniproject/distance.txt', 'r') as frd:
                            distance = int(frd.readline())
                            if prev < distance or distance < 0:
                                ontimer(TWrite(0, 3), 1500)
                                break
                            prev = distance
                            ontimer(TWrite(distance, 3), 1500)                        
            else:
                res = np.random.choice(h_lst, 1, p=[0.6, 0.3, 0.1])
                if res[0] == 0:
                    f.write("10")
                    f.close()
                    ontimer(TWrite(0, 0), 5000)
                elif res[0] == 1:
                    f.write("11")
                    f.close()
                    ontimer(Limit(100), 5000)
                elif res[0] == 2:
                    f.write("12")
                    f.close()
                    LH_st = 0                        
                    ontimer(TWrite(300, 4), 1500)
                    while True:
                        t.reset()
                        with open('/home/pi/miniproject/distance.txt', 'r') as frd:
                            distance = int(frd.readline())
                            if prev < distance or distance < 0:
                                ontimer(TWrite(0, 4), 1500)
                                break
                            prev = distance
                            ontimer(TWrite(distance, 4), 1500)
        t.reset()
        frt.close()
        f.close()
    with open('/home/pi/miniproject/signst.txt', 'w') as f:
        f.write("000")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
