/* recognize tokens for the calculator and print them out */

%{

#include "calc.tab.h"

%}

%%

"+"     { return ADD; }
"-"     { return SUB; }
"*"     { return MUL; }
"/"     { return DIV; }
"|"     { return ABS; }
[0-9]+  { yylval = atoi(yytext); return NUMBER; }
"("     { return OP; }
")"     { return CP; }
\n      { return EOL; }
[ \t]   {}
"//".*  {}
.       { printf("Mystery character %s\n", yytext); }

%%
