import configparser
import findAndReplace

PATH = '../etc/ascent'
class parse:
	def __init__(self, configfile):
		self.configfile = configfile
		self.parseConfig()

	def parseConfig(self):
		config = configparser.ConfigParser()
		config.read(self.configfile)
		config.sections()
		urls = []
		
		for section in config:
			try:
				if config[section]['Server']:
					repoPath = config[section]['Server']
					with open(f"{PATH}/{repoPath}", 'r') as f:
						lines = f.readlines()
						for line in lines:
							string = findAndReplace.findAndReplace(line, section)
							string = string.replace()
							url = f"{string}/repo-pub.json"
							urls.append(url)
			except KeyError as err:
				continue
			
			return urls

	def getRepoUrl(self):
		config = configparser.ConfigParser()
		config.read(self.configfile)
		config.sections()
		urls = []
		
		for section in config:
			try:
				if config[section]['Server']:
					repoPath = config[section]['Server']
					with open(f"{PATH}/{repoPath}", 'r') as f:
						lines = f.readlines()
						for line in lines:
							string = findAndReplace.findAndReplace(line, section)
							string = string.replace()
							url = f"{string}/repo-pub.json"
							urls.append(url)
			except KeyError as err:
				continue
			
			return urls

parse(f"{PATH}/ascent.conf")