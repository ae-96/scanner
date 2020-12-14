from re import *
def set_token_type(lex) :
    if (lex==';'): return 'SEMICOLON '
    if (lex=='if'): return 'IF'
    if (lex=='then'): return 'THEN '
    if (lex=='end'): return 'END '
    if (lex=='repeat'): return 'REPEAT'
    if (lex=='until'): return 'UNTIL '
    if (lex==':='): return 'ASSIGN'
    if (lex=='read'): return 'READ'
    if (lex=='write'): return 'WRITE'
    if (lex=='<'): return 'LESSTHAN'
    if (lex=='='): return 'EQUAL'
    if (lex=='+'): return 'PLUS '
    if (lex=='-'): return 'MINUS'
    if (lex=='*'): return 'MULT'
    if (lex=='/'): return 'DIV'
    if (lex=='('): return 'OPENBRACKET'
    if (lex==')'): return 'CLOSEDBRACKET'
    if (lex.isalpha()): return 'IDENTIFIER'
    if (lex.isalnum()): return 'NUMBER'
tinyinput='''read x; 
if 0 < x then 
fact := 1;
repeat
fact := fact * x;
x := x - 1
until x = 0;
write fact 
end'''
tokens=compile(r'[a-z]+|[A-Z]+|\d+|\+|=|;|:=|\(|\)|<|\*|/|-')
lexeme=findall(tokens,tinyinput)
output_token=[]
for i in lexeme:
    output_token.append([i,set_token_type(i)])
print(output_token)


