/* recognize tokens for the calculator and print them out */

%{

#include "calc6.tab.h"
#include "routines6.h"

%}

/* float exponent */
EXP                             ([Ee][-+]?[0-9]+)

%%

"+"|"-"|"*"|"/"|"=" |
"|"|","|";"|"("|")"             { return yytext[0];                         }

 /* comparison ops, all are a CMP token */
">"                             { yylval.fn = 1; return CMP;                }
"<"                             { yylval.fn = 2; return CMP;                }
"<>"                            { yylval.fn = 3; return CMP;                }
"=="                            { yylval.fn = 4; return CMP;                }
">="                            { yylval.fn = 5; return CMP;                }
"<="                            { yylval.fn = 6; return CMP;                }

 /* keywords */
"if"                            { return IF;                                }
"then"                          { return THEN;                              }
"else"                          { return ELSE;                              }
"while"                         { return WHILE;                             }
"do"                            { return DO;                                }
"let"                           { return LET;                               }

 /* built-in functions */
"sqrt"                          { yylval.fn = B_sqrt;  return FUNC;         }
"exp"                           { yylval.fn = B_exp;   return FUNC;         }
"log"                           { yylval.fn = B_log;   return FUNC;         }
"print"                         { yylval.fn = B_print; return FUNC;         }

 /* names */
[a-zA-Z][a-zA-Z0-9]*            { yylval.s = lookup(yytext); return NAME;   }

 /* numbers */
[0-9]+"."[0-9]*{EXP}? |
"."?[0-9]+{EXP}?                { yylval.d = atof(yytext); return NUMBER;   }

\n                              { return EOL;                               }
[ \t]                           { /* ignore whitespace */                   }
"//".*                          {}
\\\n                            { printf("c> ");                            } /* ignore line continuation */
.                               { printf("Mystery character %s\n", yytext); }
%%
