from . import parseConfig
import hashlib
import wget
import os
from . import download
import sys

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
				file = url.split('/')[-1]
				download.Download.download(f"{url}.sha256", f'etc/ascent/repos/cache/{foldername}', f"{file}.sha256.tmp")
				sha256sum = hashlib.sha256()
				with open(f"etc/ascent/repos/cache/{foldername}/{file}", "rb") as f:
					for chunk in iter(lambda: f.read(4096), b""):
						sha256sum.update(chunk)
				with open(f"etc/ascent/repos/cache/{foldername}/{file}.sha256", "w") as f:
					localchecksum = sha256sum.hexdigest()
					f.write(localchecksum)
				
				with open(f'etc/ascent/repos/cache/{foldername}/{file}.sha256.tmp', 'r') as f:
					line = f.read()
					if line.rstrip() == localchecksum:
						continue
					else:
						updateRepos = str(input("Checksums do not match. Would you like me to update the local repositories for you? (Y/n) "))
						if updateRepos == '' or updateRepos == 'Y' or updateRepos == 'y':
							download.Download.download(f"{url}", f'etc/ascent/repos/cache/{foldername}')
							download.Download.download(f"{url}.sha256", f'etc/ascent/repos/cache/{foldername}')
						else:
							print("User chose to not update mirrors. Aborting now.")
							sys.exit(1)

			else:
				download.Download.download(f"{url}", f'etc/ascent/repos/cache/{foldername}')
				download.Download.download(f"{url}.sha256", f'etc/ascent/repos/cache/{foldername}')