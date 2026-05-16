import os
import urllib.request
# subprocess doesnt really like sudo simply, just use os.system for now
# maybe switch over later?
def startSudo():
    os.system("sudo -")
def updateArch():
    os.system(f"pacman -Syu")
    os.system(f"yay -Syu")
def yay(ypkg):
    os.system(f"sudo yay -S {ypkg}")
def pacman(ppkg):
    os.system(f"sudo pacman -S {ppkg}")
def fetchLists(plistu, ylistu):
    if not os.path.exists("sources"):
        os.mkdir("sources")
    urllib.request.urlretrieve(plistu, "sources/plist.txt")
    urllib.request.urlretrieve(ylistu, "sources/ylist.txt")