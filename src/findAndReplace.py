class findAndReplace:
	def __init__(self, string, replace):
		self.string = string
		self.stringReplace = replace

	def replace(self):
		self.string = self.string.split('{{ ')
		self.string = [
			self.string[0],
			self.string[1].split(' }}')[0]
		]
		self.string[1] = self.stringReplace
		self.string = f"{self.string[0]}{self.string[1]}"
		return self.string