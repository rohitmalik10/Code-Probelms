// Execute both if and else statements in C/C++ simultaneously
#include <stdio.h> 
int main() 
{ 
  if (1) //Replace 1 with 0 and see the magic 
  { 
    label_1: printf("RM"); 
      
    // Jump to the else statement after  
    // executing the above statement 
    goto label_2; 
  } 
  else
  { 
    // Jump to 'if block statement' if  
    // the Boolean condition becomes false 
    goto label_1; 
  
    label_2: printf("Ramboo"); 
  } 
  return 0; 
} 