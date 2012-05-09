

TARGETS=calc1 calc2 calc3 calc4 calc5
calc1: calc1.flex
	flex -o calc1.yy.c $<
	gcc -o $@ calc1.yy.c -lfl

calc2: calc2.flex
	flex -o calc2.yy.c $<
	gcc -o $@ calc2.yy.c -lfl

calc3: calc3.flex calc3.y
	bison -d calc3.y
	flex -o calc3.yy.c calc3.flex
	gcc -o $@ calc3.tab.c calc3.yy.c -lfl

calc4: calc4.flex calc4.y routines.h routines.c
	bison -d calc4.y
	flex -o calc4.yy.c calc4.flex
	gcc -o $@ calc4.tab.c calc4.yy.c routines.c -lfl

calc5: calc5.flex calc5.y routines.h routines.c
	bison -d calc5.y
	flex -o calc5.yy.c calc5.flex
	gcc -o $@ calc5.tab.c calc5.yy.c routines.c -lfl


all: ${TARGETS}
	

clean:
	rm -rf ${TARGETS} *.yy.c *.tab.c *.tab.h
