/* simplest version of calculator */
%{
#include <stdio.h>
#include <stdlib.h>
#include "routines.h"
%}


%union {
    struct ast *a;
    double d;
}

/* declare tokens */
%token NUM
%token <d> NUMBER
%token EOL

%left '+' '-'
%left '*' '/'
%nonassoc '|' UMINUS

%type <a> exp

%%

calclist: /* nothing */
 | calclist exp EOL { 
     printf("= %4.4g\n", eval($2));     /* evaluate and print the AST */
     treefree($2);                      /* free up the AST */
     printf("> ");
    }
 | calclist EOL     { printf("> "); }   /* blank line or a comment */
 ;

exp: exp '+' exp        { $$ = newast('+', $1,$3);      }
 | exp '-' exp          { $$ = newast('-', $1,$3);      }
 | exp '*' exp          { $$ = newast('*', $1,$3);      }
 | exp '/' exp          { $$ = newast('/', $1,$3);      }
 | '|' exp              { $$ = newast('|', $2, NULL);   }
 | '(' exp ')'          { $$ = $2;                      }
 | '-' exp %prec UMINUS { $$ = newast('M', $2, NULL);   }
 | NUMBER               { $$ = newnum($1);              }
 ;

%%
