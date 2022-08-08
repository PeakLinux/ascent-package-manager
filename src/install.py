from . import parseConfig
import hashlib
import wget

class Packages:
	def __init__(self, packages, config):
		self.packages = packages
		self.config = parseConfig.parse(config)

	def search(self):
		print(f"Searching for: {self.packages}")

	def install(self):
		print("Checking if cached repos are up to date")
		repos = parseConfig.parse
		wget.download()