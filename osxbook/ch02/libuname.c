#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/utsname.h>

#define DYLD_INTERPOSE(_replacment,_replacee) \
  __attribute__((used)) static struct{ const void* replacment; const void* replacee; } _interpose_##_replacee \
  __attribute__ ((section ("__DATA,__interpose"))) = { (const void*)(unsigned long)&_replacment, (const void*)(unsigned long)&_replacee }; 

int my_uname(struct utsname *name);

DYLD_INTERPOSE(my_uname, uname)

int my_uname(struct utsname *name)
{
  int ret = uname(name);
  printf("--> %d = uname() [%s]\n", ret, name->version );
  strncpy(name->version, "Johnny 5", sizeof(name->version));

  return ret;
}

