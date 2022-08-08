from tqdm import tqdm
import requests
import os

class Download:
	def download(url, outdir):
		buffer = 1024
		response = requests.get(url, stream=True)

		downloadSize = int(response.headers.get("Content-Length", 0))
		filename = os.path.join(outdir, url.split('/')[-1])

		progress = tqdm(response.iter_content(buffer), f"Updating the {filename.split('/')[-2]} repository", total=downloadSize, unit="B", unit_scale=True, unit_divisor=1024)
		with open(filename, "wb") as f:
			for data in progress.iterable:
				f.write(data)
				progress.update(len(data))