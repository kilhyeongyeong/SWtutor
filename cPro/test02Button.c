#include <stdio.h>
#include <wiringPi.h>

//pi@raspberrypi:~/cPro $ gpio readall
//pi@raspberrypi:~/cPro $ gpio -g mode 23 output
//pi@raspberrypi:~/cPro $ gpio -g write 23 1 => BCM 23 = V 1
//pi@raspberrypi:~/cPro $ sudo apt install fritzing

#define BUTTON01 2

int main(int argc, char **argv){
	printf("Hello C...\n");
	
	if(wiringPiSetup()==-1) return -1;
	
	pinMode(BUTTON01, INPUT); //gpio -g mode 4 output

	while(1){
		int b01 = digitalRead(BUTTON01);
		printf("digitalRead :%d\n", b01);
		delay(500);
	}
	
	printf("End main...\n");
}
