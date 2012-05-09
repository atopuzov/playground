

calc1: calc1.flex
	flex $<
	gcc -o $@ lex.yy.c -lfl

calc2: calc2.flex
	flex $<
	gcc -o $@ lex.yy.c -lfl


calc3:	calc3.flex calc.y
	bison -d calc.y
	flex calc3.flex
	gcc -o $@ calc.tab.c lex.yy.c -lfl

clean:
	rm -rf calc1 calc2 calc3 lex.yy.c calc.tab.c calc.tab.h
