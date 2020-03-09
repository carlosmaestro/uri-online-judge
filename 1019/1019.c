#include <stdio.h>

int main(){
	int sec = 0;
	
	scanf("%d", &sec);
	
	convertSeconds(sec);
	
	return 0;
}

void convertSeconds(int sec){
	int min_sec = 60;
	int hour_sec = 60 * min_sec;

	int hours = 0;
	int mins = 0;
	
	
	if(sec >= hour_sec){
		hours = sec / hour_sec;
		sec = sec - (hours * hour_sec);
	}
	if(sec >= min_sec){
		mins = sec / min_sec;
		sec = sec - (mins * min_sec);
	}
	
	printf("%d:%d:%d\n" , hours, mins, sec);
}