from . import parseConfig

class Packages:
	def __init__(self, packages, config):
		self.packages = packages
		self.config = parseConfig.parse(config)

	def install(self):
		print(self.packages)