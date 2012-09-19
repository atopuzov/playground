CC=clang
CXX=clang++
LT=libtool

%.o: %.c
	${CC} ${CFLAGS} -c $<

%.a: %.o
	${LT} -static -o $@ $<

%.dylib: %.o
	${CC} -dynamiclib -o $@ -install_name $@ $<

empty: empty.o
	$(CC) $< -o $@

hello1: main1.o libhello1.a
	${CC} $^ -o $@

hello2: main1.o libhello1.dylib
	${CC} -o $@ main1.o -L. -lhello1

hello3: main1.o libhello2.o
	${CC} -dynamiclib -o libhello2.dylib -install_name libhello2.dylib -init _my_start libhello2.o
	${CC} main1.o -L. -lhello2 -o $@

hello4: main2.o libweakfunc.dylib
	${CC} main2.o -L. -lweakfunc -o $@

interpose: libinterposers.dylib
	DYLD_INSERT_LIBRARIES=./$< cat /dev/null

interpose2: libinterposers2.dylib
	DYLD_FORCE_FLAT_NAMESPACE=1 DYLD_INSERT_LIBRARIES=./$< cat /dev/null

uname: libuname.dylib
	DYLD_INSERT_LIBRARIES=./$< uname -v
