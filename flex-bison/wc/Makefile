wc:	wc.flex
	flex $<
	gcc -g -o $@ lex.yy.c -lfl

clean:
    rm -rf wc lex.yy.c