import time
    
def main(args):
    prev = 0
    speed = 0
    print("start")
    
    while True:
        frt = open('/home/pi/miniproject/trafst.txt', 'r')
        time.sleep(0.1)
        st = frt.readline()
        if not st:
            st = prevst
        else:
            st = int(st)
            prevst = st
        frs = open('/home/pi/miniproject/signst.txt', 'r')
        sign = str(frs.readline())
        if st == 4:
            if prev == 0:
                prev = 1
                distance = 300
            if sign == "124":
                if speed >= 50:
                    speed = 50
                    distance = distance - ((speed * 1000)/60/60/10*2)
                    fwd = open('/home/pi/miniproject/distance.txt', 'w')
                    distance = round(distance)
                    fwd.write(str(distance))
                    fwd.close()
                    print("distance :", distance)
                else:
                    speed -= 7
                    if speed <= 0:
                        speed = 0
                        print(speed)
                        break
                    
            elif sign == "000":
                speed -= 2
                if speed <= 0:
                    speed = 0
                    print(speed)
                    break
            else:
                if speed < 20:
                    speed += 1
                speed = speed
                distance = distance - ((speed * 1000)/60/60/10*2)
                fwd = open('/home/pi/miniproject/distance.txt', 'w')
                distance = round(distance)
                fwd.write(str(distance))
                fwd.close()
                print("distance :", distance)
        else:
            if sign == "03" or sign == "04" or sign == "12" or sign == "05":
                if prev == 0:
                    distance = 300
                    prev = 1
                    
            if sign == "00": #go
                speed += 1
                if speed >= 80:
                    speed -= 1
            elif sign == "01": #50km
                if speed > 50:
                    speed -= 2
                else:
                    speed += 1
            elif sign == "02": #school
                if speed > 30:
                    speed -= 3
                else:
                    speed += 1
            elif sign == "03": #light
                if st == 1: #green
                    if speed >= 80:
                        speed -= 1
                    else:
                        speed += 2
                elif st == 2: #yellow
                    if speed > 50:
                        speed -= 2
                    elif speed > 30:
                        speed -= 1
                    else:
                        speed += 1
                elif st == 3: #red
                    if speed > 10:
                        speed -= 3
                    elif speed > 0:
                        speed -= 1
                    elif speed <= 0:
                        speed = 0
                distance = distance - ((speed * 1000)/60/60/10*2)
                fwd = open('/home/pi/miniproject/distance.txt', 'w')
                distance = round(distance)
                if st == 3:
                    if distance < 10 and speed > 0:
                        speed = 0
                        print("speed :", speed)
                fwd.write(str(distance))
                fwd.close()
                print("distance :", distance)
                if distance <= 0:
                    prev = 0
            elif sign == "04": #turn
                if distance > 50:
                    speed = speed
                else:
                    if speed > 40:
                        speed -= 2
                    else:
                        speed += 1
                distance = distance - ((speed * 1000)/60/60/10*2)
                fwd = open('/home/pi/miniproject/distance.txt', 'w')
                distance = round(distance)
                fwd.write(str(distance))
                fwd.close()
                print("distance :", distance)
                if distance <= 0:
                    prev = 0
            elif sign == "05":
                speed += 1
                distance = distance - ((speed * 1000)/60/60/10*2)
                distance = round(distance)
                print("distance :", distance)
                fwd = open('/home/pi/miniproject/distance.txt', 'w')
                fwd.write(str(distance))
                fwd.close()
                if distance <= 0:
                    prev = 0
            elif sign == "10":
                if speed >= 120:
                    speed = 120
                else:
                    speed += 5
            elif sign == "11":
                if speed > 100:
                    speed -= 2
                else:
                    speed += 1
            elif sign == "12":
                distance = distance - ((speed * 1000)/60/60/10*2)
                distance = round(distance)
                if distance > 100:
                    speed = speed
                else:
                    if speed < 50:
                        speed = speed
                    else:
                        speed -= 3                    
                fwd = open('/home/pi/miniproject/distance.txt', 'w')
                fwd.write(str(distance))
                fwd.close()
                print("distance :", distance)
                if distance <= 0:
                    prev = 0
            else:
                print("error")
                break
        
        print("speed :", speed)
        with open('/home/pi/miniproject/speed.txt', 'w') as fws:
            fws.write(str(speed))
        frt.close()
        frs.close()
        time.sleep(0.1)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
