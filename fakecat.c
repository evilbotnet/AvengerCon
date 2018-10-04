#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>

char *pick(void) {

    const char* words[4];
    words[0] = "meow\n";
    words[1] = "I cAn HaZ Tr3aT?\n";
    words[2] = "try -treat\n";
    words[3] = "Cats need treats.\n";

    static char* random; 
    srand(time(NULL));
    random = words[rand() % 3];
    //printf(random); // 4
    return random;
}

int main(int argc, char *argv[])
{
char treat[] = "-treat";
if( argc == 3 ) {
	if (!strcmp(argv[2], "-treat")){
		printf("Mmmmm\n");
		char buf[32];
		sprintf(buf, "/bin/cat %s", argv[1]);
		system(buf);

 	}
	else {
		printf(pick());
	}
	//char buf[32];
	//sprintf(buf, "/bin/cat %s", argv[1]);
      //printf("The argument supplied is %s\n", argv[1]);
	//system(buf);

   }
   else if( argc == 2 ) {
      printf(pick());
   }
   else if( argc > 3 ){
      printf("wut\n");
   }
   else {
      //printf("One argument expected.\n");
	system("/bin/cat");
   }

//	setuid(geteuid());
	return 0;
}
