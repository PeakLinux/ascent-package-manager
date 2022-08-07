import configparser

class parse:
	def __init__(self, configfile):
		self.configfile = configfile
		self.parseConfig()
	
	def parseConfig(self):
		config = configparser.ConfigParser()
		config.read(self.configfile)