import configparser
from . import findAndReplace
class parse:
	def __init__(self, configfile):
		self.configfile = configfile
		self.path = self.configfile.split('/')[:2]
		self.path = f"{self.path[0]}/{self.path[1]}"

	def parseConfig(self):
		pass

	def getRepoUrl(self):
		config = configparser.ConfigParser()
		config.read(self.configfile)
		config.sections()
		urls = []
		
		for section in config:
			try:
				if config[section]['Server']:
					repoPath = config[section]['Server']
					with open(f"{self.path}/{repoPath}", 'r') as f:
						lines = f.readlines()
						for line in lines:
							string = findAndReplace.findAndReplace(line, section)
							string = string.replace()
							url = f"{string}/repo-pub.json"
							urls.append(url)
			except KeyError as err:
				continue
			
		return urls