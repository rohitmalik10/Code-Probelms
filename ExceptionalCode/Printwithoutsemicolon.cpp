// printf(function): int printf(const char*format,...)
// Parameter 1) format: string that contains a text to be written to stdout.
// Additional arguments:(three dots are called ellipses) which indicates the variable number of arguments depending upon the formal string
// Procedure
// 1)
#include<stdio.h>
int main()
{
	if(printf("ramboo"))
	{

	}
	return 0;
}
// 2)
 #include<stdio.h>
 int main()
 {
 	while(!printf("ramboo"))
 	{

 	}
 	return 0;
 }
// 3)
#include<stdio.h>
int main()
{
	swtich(printf("rambo"))
	{

	}

}
 // 4)
#include<stdio.h>
#define PRINT printf("rambo")
int main()
{

	if(PRINT)
	{

	}
}