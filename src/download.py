from tqdm import tqdm
import requests
import os
from typing import Optional

class Download:
	def download(url, outdir, filename: Optional[str]=None):
		buffer = 16
		response = requests.get(url, stream=True)

		downloadSize = int(response.headers.get("Content-Length", 0))

		print(url)
		
		if not filename:
			filename = os.path.join(outdir, url.split('/')[-1])
		else:
			filename = os.path.join(outdir, filename)

		progress = tqdm(response.iter_content(buffer), f"Updating the {filename.split('/')[-2]} repository", total=downloadSize, unit="B", unit_scale=True, unit_divisor=1024)
		with open(filename, "wb") as f:
			for data in progress.iterable:
				f.write(data)
				progress.update(len(data))