#include <stdio.h>
#include <wiringPi.h>

//pi@raspberrypi:~/cPro $ gpio readall
//pi@raspberrypi:~/cPro $ gpio -g mode 23 output
//pi@raspberrypi:~/cPro $ gpio -g write 23 1 => BCM 23 = V 1
//pi@raspberrypi:~/cPro $ sudo apt install fritzing

#define GPIO4 7 //BCM 4
#define GPIO23 4 //BCM 23

int main(int argc, char **argv){
	printf("Hello C...\n");
	
	if(wiringPiSetup()==-1) return -1;
	
	pinMode(GPIO4, OUTPUT); //gpio -g mode 4 output
	pinMode(GPIO23, OUTPUT); //gpio -g mode 23 output
	
	int i;
	for(i=0; i<10; i++){
		digitalWrite(GPIO4,1);
		digitalWrite(GPIO23,0);
		delay(1000); //1s
		digitalWrite(GPIO4,0);
		digitalWrite(GPIO23,1);
		delay(1000);
	}
	digitalWrite(GPIO4,0);
	digitalWrite(GPIO23,0);
	
	printf("End main...\n");
}
