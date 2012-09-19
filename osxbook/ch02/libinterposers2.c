#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <dlfcn.h>

int open(const char *path, int arg, ... )
{
  int  (*original)(const char *, int, ...) = NULL;
  void *handle = dlopen("libc.dylib", RTLD_NOW);
  original = (void *)dlsym(handle, __func__);

  int ret = original(path, arg);
  printf("--> %d = open(%s)\n", ret, path);
  return ret;
}

int close(int d)
{
  int (*original)(int) = NULL;
  void *handle = dlopen("libc.dylib", RTLD_NOW);
  original = (void *)dlsym(handle, __func__);

  int ret = original(d);
  printf("--> %d = close(%d)\n", ret, d);
  return ret;
}
