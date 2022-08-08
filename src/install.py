from . import parseConfig
import hashlib
import wget
import os
from . import download

class Packages:
	def __init__(self, packages, config):
		self.packages = packages
		# self.config = parseConfig.parse(config)
		# self.config = ""

	def search(self):
		print(f"Searching for: {self.packages}")

	def install(self):
		print("Checking if cached repos are up to date")
		repos = parseConfig.parse('etc/ascent/ascent.conf')
		repos = repos.getRepoUrl()
		# print(repos)

		for url in repos:
			foldername = url.split('/')[-2]
			if os.path.isdir(f'etc/ascent/repos/cache/{foldername}'):
				pass
			else:
				os.mkdir(f'etc/ascent/repos/cache/{foldername}')
			# if os.path.isfile('etc/ascent/repos/cache/{foldername}/repo-pub.json') and os.path.isfile('etc/ascent/repos/cache/{foldername}/repo-pub.json.sha256'):
			# 	download.Download.download(f"{url}.sha256", f'etc/ascent/repos/cache/{foldername}')
			if os.path.isfile(f'etc/ascent/repos/cache/{foldername}/repo-pub.json') and os.path.isfile(f'etc/ascent/repos/cache/{foldername}/repo-pub.json.sha256'):
				url = url.split('/')
				download.Download.download(f"{url}.sha256", f'etc/ascent/repos/cache/{foldername}/{url[-1]}.sha256.tmp')
				sha256sum = hashlib.sha256()
				with open(f"etc/ascent/repos/cache/{foldername}/{url[-1]}", "rb") as f:
					for chunk in iter(lambda: f.read(4096), b""):
						sha256sum.update(chunk)
				with open(f"etc/ascent/repos/cache/{foldername}/{url[-1]}.sha256", "w") as f:
					f.write(sha256sum.hexdigest())
				# print(hashlib.sha256(f"etc/ascent/repos/cache/{foldername}/{url[:-1]}"))
			else:
				download.Download.download(f"{url}", f'etc/ascent/repos/cache/{foldername}')
				download.Download.download(f"{url}.sha256", f'etc/ascent/repos/cache/{foldername}')