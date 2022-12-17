# Python Script Created by MRS
import pathlib

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
PROXIES={"http": "http://127.0.0.1:7890"}
ROOT_PATH = str(pathlib.Path.cwd())
DATA_PATH = ROOT_PATH + "/data/"
IMG_PATH = ROOT_PATH + "/img/"
DOMIN = "https://wiki.biligame.com"