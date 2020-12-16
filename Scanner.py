from re import *
class scanner :
    def __init__(self,string):
        self.file=string
        self.output_token = []
        self.tokens=""

    def set_token_type(self,lex) :
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
    def Scan(self):
        commentsregex=compile(r'{(.*?)}',DOTALL)
        tinyinput=commentsregex.sub('',self.file)
        tokens=compile(r'[a-z]+|\d+|\+|=|;|:=|\(|\)|<|\*|/|-',IGNORECASE)
        lexeme=findall(tokens,tinyinput)
        for i in lexeme:
            self.output_token.append([i,self.set_token_type(i)])
            self.tokens += self.set_token_type(i) +"\n"

    def outTokens(self):
        return (self.tokens)

