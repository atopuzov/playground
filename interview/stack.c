/*
  Determines which way does the stack grow
 */
#include <stdio.h>
#include <stdlib.h>

void ww(int *a)
{
  int b;
  if (a>&b)
    {
      printf("Grows down\n");
    }
  else if (a<&b)
    {
      printf("Grows up\n");
    }
}

int main (void)
{
  int a;
  ww(&a);
  
  return EXIT_SUCCESS;
}
