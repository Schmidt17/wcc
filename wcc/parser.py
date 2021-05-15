from rply import ParserGenerator
from rply.token import BaseBox


class WccParser:
	def __init__(self):
		self.token_list = ["NUMBER", "PLUS", "EXIT"]
		pg = ParserGenerator(self.token_list, cache_id='wcc')

		@pg.production("main : statement")
		def main(p):
			return p[0]

		@pg.production("statement : addition")
		@pg.production("statement : exit")
		def main(p):
			return p[0]

		@pg.production("exit : EXIT")
		def exit_prod(p):
			return ExitBox()

		@pg.production("number : NUMBER")
		def number(p):
			return IntBox(p[0])

		@pg.production("addition : PLUS number number")
		def addition0(p):
			return BinaryAddBox(p[1], p[2])

		@pg.production("addition : number PLUS number")
		def addition1(p):
			return BinaryAddBox(p[0], p[2])

		@pg.production("addition : number number PLUS")
		def addition2(p):
			return BinaryAddBox(p[0], p[1])

		self.parser = pg.build()

	def parse(self, token_generator):
		return self.parser.parse(token_generator)


class IntBox(BaseBox):
	def __init__(self, value):
		self.value = value

	def getint(self):
		return int(self.value.getstr())


class BinaryAddBox(BaseBox):
	def __init__(self, number1, number2):
		self.number1 = number1
		self.number2 = number2

	def eval(self):
		return self.number1.getint() + self.number2.getint()


class ExitBox(BaseBox):
	def __init__(self):
		pass

	def eval(self):
		exit()