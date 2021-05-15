from rply import LexerGenerator


class WccLexer:
	def __init__(self):
		lg = LexerGenerator()

		lg.add('NUMBER', r'\d+')
		lg.add('PLUS', r'\+')
		lg.add('MINUS', r'-')
		lg.add('EXIT', r'exit')

		lg.ignore(r'\s+')

		self.lexer = lg.build()

	def lex(self, text):
		return self.lexer.lex(text)
