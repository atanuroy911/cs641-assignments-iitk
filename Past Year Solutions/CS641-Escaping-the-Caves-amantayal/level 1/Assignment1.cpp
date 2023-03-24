#include <stdio.h>
#include <stdlib.h>

int main(){
	FILE* cipher;
	cipher = fopen("cipher.txt","r"); //cipher.txt is the file were cipher text is stored.
	char key[1000];
	float frequency[1000];
	int keysize=0;
	char a;
	int count = 0;
	while(!feof(cipher)){
		fscanf(cipher,"%c",&a);
		fprintf(stdout,"%c",a);
		
		if (a!=' ' && a!='\n' && a!=',' && a!='.' && a!= '_'){
			count+=1;
			if (int(a)<='Z' && int(a)>='A'){  //Handling capital letters
					a = a + 'a' - 'A';
				}
			if (keysize == 0){     //Handling empty key
				key[keysize] = a;
				frequency[keysize] = 1.0;
				keysize++;
			}
			
			else{
				int truth = 1; //To check if the letter has been already seen earlier
				int i;
				for (i=0; i<keysize; i++){
					if (key[i]==a){
						truth =0;    
						frequency[i] += 1.0;
					}
				}
					if(truth){
						key[keysize] = a;
						frequency[keysize] = 1.0;
						keysize++;
					}
					
			}
			
		}
	}
	int i;
	// Calculating the relative frequencies
	for (i=0; i<keysize; i++){
		frequency[i] /= count;
		frequency[i] *=100;
	}
	 
	// Sorting the Frequencies
    int j;  
    for (i = 0; i < keysize-1; i++){  
    for (j = 0; j < keysize-i-1; j++){
        if (frequency[j] < frequency[j+1]){
			float temp1 = frequency[j];
			frequency[j] = frequency[j+1];
			frequency[j+1] = temp1;
			char temp2 = key[j];
			key[j] = key[j+1];
			key[j+1] = temp2; 
        }
    }
}	
	
	//Printing the frequencies
	for (i=0;i<keysize;i++){
		printf("\nFrequency of %c is %.3f\n",key[i],frequency[i]);
	}
	
	
	printf("\n");
	fclose(cipher);
	
	cipher = fopen("cipher.txt","r");
	while(!(feof(cipher))){
		fscanf(cipher,"%c",&a);
		if (int(a)<='Z' && int(a)>='A'){
			a = a + 'a' - 'A';
		}
		
		//The key is given below and decryption taking place simultaneously. Found the key by playing Hangman
		switch(a){
			case 'l' :			
				printf("e");
				break;
			case 'e' :			
				printf("t");
				break;
			case 'v' :			
				printf("h");
				break;
			case ' ':
				printf(" ");
				break;
			case '.':
				printf(".");
				break;
			case ',':
				printf(",");
				break;
			case '_':
				printf("_");
				break;
	
			case 'k':
				printf("i");
				break;
			case 'z':
				printf("n");
				break;
			case 'j':
				printf("s");
				break;
			case 'p':
				printf("a");
				break;
			case 'u':
				printf("r");
				break;
			case 'q':
				printf("o");
				break;
			case 'h':
				printf("g");
				break;
			case 'a':
				printf("v");
				break;
			case 'm':
				printf("d");
				break;
			case 'f':
				printf("m");
				break;
			case 't':
				printf("f");
				break;
			case 'i':
				printf("w");
				break;
			case 'g':
				printf("y");
				break;
			case 'w':
				printf("u");
				break;
			case 'd':
				printf("p");
				break;
			case 'c':
				printf("b");
				break;
			case 'r':
				printf("l");
				break;
			case 's':
				printf("c");
				break;
			case 'y':
				printf("q");
				break;
			case '\n':
				printf("\n");
				break;
			case '8':
				printf("4");
				break;
			case '4':
				printf("0");
				break;
			case '7':
				printf("3");
				break;
			default :
				printf("X");
				
		}
	}
	fclose(cipher);
}
