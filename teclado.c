#include<stdio.h>

int main(){
	//while (getc(stdin) != '\x1b');

	printf("pulse ESC para salir\n");

	while (1){
		char d;
		d = getc(stdin);
		//printf("%c", d);
		if (d == '\x1B'){
			break;
		}else{
			printf("intente nuevamente\n");

		}
	}

}