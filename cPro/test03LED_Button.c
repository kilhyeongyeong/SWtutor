#include <stdio.h>
#include <wiringPi.h>

//pi@raspberrypi:~/cPro $ gpio readall
//pi@raspberrypi:~/cPro $ gpio -g mode 23 output
//pi@raspberrypi:~/cPro $ gpio -g write 23 1 => BCM 23 = V 1
//pi@raspberrypi:~/cPro $ sudo apt install fritzing

#define BUTTON01 2 
#define LED 7

int main(int argc, char **argv){
	printf("Hello C...\n");
	
	if(wiringPiSetup()==-1) return -1;
	
	pinMode(LED, OUTPUT); //gpio -g mode 4 output
	pinMode(BUTTON01, INPUT); //gpio -g mode 23 output
	
	while(1){
		if(digitalRead(BUTTON01)==1){
			digitalWrite(LED, 1);
		}else{
			digitalWrite(LED, 0);
		}
	}
	
	printf("End main...\n");
}
