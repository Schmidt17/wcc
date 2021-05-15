from rply import ParserGenerator

from lexer import WccLexer
from parser import WccParser


lexer = WccLexer()
parser = WccParser()

while True:
	text = input("wc> ")

	# Lexer debugging
	# for token in lexer.lex(text):
	# 	print(token)

	parse_result = parser.parse(lexer.lex(text))

	print(parse_result.eval())