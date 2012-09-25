CC=clang
CXX=clang++
LT=libtool

%.o: %.c
	${CC} ${CFLAGS} -c $<

%.s: %.c
	${CC} ${CFLAGS} -S $<

%.a: %.o
	${LT} -static -o $@ $<

%.dylib: %.o
	${CC} -dynamiclib -o $@ -install_name $@ $<

function: function.s
	cat $^

stacktrace: stacktrace.o
	${CC} $^ -o $@


