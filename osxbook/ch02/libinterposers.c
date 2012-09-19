// libinterposers.c

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

#define DYLD_INTERPOSE(_replacment,_replacee) \
  __attribute__((used)) static struct{ const void* replacment; const void* replacee; } _interpose_##_replacee \
  __attribute__ ((section ("__DATA,__interpose"))) = { (const void*)(unsigned long)&_replacment, (const void*)(unsigned long)&_replacee }; 

/* typedef struct interpose_s { */
/* void *new_func; */
/* void *orig_func; */
/* } interpose_t; */

int my_open(const char *, int, mode_t);
int my_close(int);

/* static const interpose_t interposers[] __attribute__ ((section("__DATA, __interpose"))) = { */
/*   { (void *)my_open,  (void *)open  }, */
/*   { (void *)my_close, (void *)close }, */
/* }; */

DYLD_INTERPOSE(my_open, open)
DYLD_INTERPOSE(my_close, close)

int my_open(const char *path, int flags, mode_t mode)
{
int ret = open(path, flags, mode);
printf("--> %d = open(%s, %x, %x)\n", ret, path, flags, mode);
return ret;
}

int my_close(int d)
{
int ret = close(d);
printf("--> %d = close(%d)\n", ret, d);
return ret;
}
