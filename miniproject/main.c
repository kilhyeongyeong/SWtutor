#include <stdio.h>
#include <wiringPi.h>

#define LED_RED 28 //BCM 20
#define LED_GREEN 25 //BCM 26
#define LED_YELLOW 27

#define BUTTON01 0 //BCM 17 -> GREEN
#define BUTTON02 1 //BCM 18 -> YELLOW
#define BUTTON03 2 //BCM 27 -> RED
#define BUTTON04 7 //BCM 4 -> POWER

void interrupt();

int count_r = 0;
int count_g = 0;
int count_y = 0;
int check = 0;
int pprev_r = 0;
int speed = 0;
	
int main(int argc, char **argv){
	int prev_r = 0;
	int prev_g=0;
	int prev_y = 0;
	int prev_e = 0;
	int count_yy = 0;

	
	if(wiringPiSetup()==-1) return -1;
	
	pinMode(LED_RED, OUTPUT); //gpio -g mode 20 output
	pinMode(LED_GREEN, OUTPUT); //gpio -g mode 26 output
	pinMode(LED_YELLOW, OUTPUT); //gpio -g mode 16 output
	
	pinMode(BUTTON01, INPUT);
	pinMode(BUTTON02, INPUT);
	pinMode(BUTTON03, INPUT);
	pinMode(BUTTON04, INPUT);
	
	while(1){
		printf("speed : %dkm\n", speed);
		int b01 = digitalRead(BUTTON01);
		int b02 = digitalRead(BUTTON02);
		int b03 = digitalRead(BUTTON03);
		int b04 = digitalRead(BUTTON04);
		
		if(b01 == 1){
			if(prev_g == 0){
				prev_g = 1;
				prev_y = 0;
				prev_r = 0;
			}else{
				prev_g = 0;
			}
		}else if(b02 == 1){
			if(prev_y == 0){
				prev_y = 1;
				prev_r = 0;
				prev_g = 0;
			}else{
				prev_y = 0;
			}
		}else if(b03 == 1){
			if(prev_r == 0){
				prev_r = 1;
				prev_y = 0;
				prev_g = 0;
			}else{
				prev_r = 0;
			}
		}else if(b04 == 1){
			prev_e = 1;
		}
		
		if (prev_e == 1){
			if(speed > 10)
				speed-=3;
			else if(speed > 0)
				speed--;
			else{
				printf("speed : %dkm\n", speed);
				printf("End.\n");
				break;
			}
		}else{
						if(prev_g == 1){
				prev_y = 0;
				prev_r = 0;
				pprev_r = 0;
				digitalWrite(LED_GREEN,1);
				if(speed >= 110){
					speed = 110;
				}else speed+=5;
				digitalWrite(LED_YELLOW,0);
				digitalWrite(LED_RED,0);
				count_r = 0;
				count_g = 0;
				count_y = 0;
				check = 0;
			}else if(prev_y == 1){
				prev_g = 0;
				prev_r = 0;
				pprev_r = 0;
				digitalWrite(LED_GREEN,0);
				digitalWrite(LED_YELLOW,1);
				if(speed > 50)
					speed-=3;
				else if(speed == 50)
					speed = 50;
				else
					speed++;
				digitalWrite(LED_RED,0);
				count_yy++;
				if(count_yy >= 5){
					digitalWrite(LED_YELLOW,0);
					count_yy = 0;
				}
				count_r = 0;
				count_g = 0;
				count_y = 0;
				check = 1;
			}else if(prev_r == 1){
				prev_g = 0;
				prev_y = 0;
				if(pprev_r == 0){
					digitalWrite(LED_GREEN,0);
					digitalWrite(LED_YELLOW,1);
					for(int i=0; i<15; i++){
						printf("speed : %dkm\n", speed);
						if(speed > 0)
							speed-=7;
						else
							speed = 0;
						delay(175);
					}
					digitalWrite(LED_RED,0);
					delay(2000);
					pprev_r = 1;
				}
				digitalWrite(LED_GREEN,0);
				digitalWrite(LED_YELLOW,0);
				digitalWrite(LED_RED,1);
				if(speed > 0)
					speed-=2;
				else
					speed = 0;
				count_r = 0;
				count_g = 0;
				count_y = 0;
				check = 2;
			}else if(prev_g == 0 || prev_y == 0 || prev_r == 0){
				pprev_r = 0;
				interrupt();
			}
		}
		delay(175);
	}
	
	return 0;
}

void interrupt(){
	pinMode(LED_RED, OUTPUT); //gpio -g mode 20 output
	pinMode(LED_GREEN, OUTPUT); //gpio -g mode 26 output
	pinMode(LED_YELLOW, OUTPUT); //gpio -g mode 16 output
	
	
	if(check == 0){
		digitalWrite(LED_GREEN,1);
		if(speed >= 110)
			speed = 110;
		else
			speed+=5;
		digitalWrite(LED_RED,0);
		digitalWrite(LED_YELLOW,0);
		count_g++;
		if(count_g >= 100){
			count_g = 0;
			check = 1;
		}
	}else if(check == 1){
		digitalWrite(LED_YELLOW,1);
		if(speed > 50)
			speed -=7;
		else if(speed > 0)
			speed--;
		else
			speed = 0;
		digitalWrite(LED_GREEN,0);
		digitalWrite(LED_RED,0);
		count_y++;
		if(count_y >= 20){
			count_y = 0;
			check = 2;
		}
	}else if (check == 2){
		pprev_r = 1;
		digitalWrite(LED_RED,1);
		if(speed > 10)
			speed-=3;
		else if(speed > 0)
			speed--;
		else
			speed = 0;
		digitalWrite(LED_GREEN,0);
		digitalWrite(LED_YELLOW,0);
		count_r++;
		if(count_r >= 100){
			count_r = 0;
			check = 0;
		}
	}
}
