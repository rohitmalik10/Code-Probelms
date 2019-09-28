// C Program to print a string without Quote in the program
#include<stdio.h>
#define get(x) #x  //Use of MACRO Processor(A token passed a macro can be converted to a string literal by using # before it)
int main()
{
	printf(get(rambo));
	return 0;
}