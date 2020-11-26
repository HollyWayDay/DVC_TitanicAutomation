import gdown

url = 'https://drive.google.com/uc?id=1nXYZU4EafiqEjC38QHThFNvSvW3Uai_L'
output = 'titanic.csv'
gdown.download(url, output, quiet=False) 