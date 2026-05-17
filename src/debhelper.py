import os
import urllib.request
# this is mostly a copy paste of archhelper.py to work with debian
def startSudo():
    os.system("sudo -")
def fetchList(dlistu):
    if not os.path.exists("sources"):
        os.mkdir("sources")
    urllib.request.urlretrieve(dlistu, "sources/dlist.txt")
def apt(apkg):
    os.system(f"sudo apt install {apkg}")
def update():
    os.system(f"sudo apt update")
def clearJunk():
    os.system(f"sudo apt autoremove")