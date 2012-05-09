CC     = clang
CXX    = clang++
SRCS   = main.o quartz_utils.m MyWindow.o MyView.o WindowDelegate.o AppDelegate.o MyApp.o
MAIN   = prog
CFLAGS = -Wall -O0 -g
ARC    = -fobjc-arc

default: ${MAIN}

.m.o:
	${CC} -c ${CFLAGS} -o $@ $<

.c.o:
	${CC} -c ${CFLAGS} -o $@ $<


${MAIN}: ${SRCS}
	${CC} -Wall -o ${MAIN} ${SRCS} -framework Foundation -framework Cocoa

clean:
	rm *.o ${MAIN}

all: default
