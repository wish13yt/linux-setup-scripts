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
def fetchLists(plistu, ylistu, useaur):
    if not os.path.exists("sources"):
        os.mkdir("sources")
    urllib.request.urlretrieve(plistu, "sources/plist.txt")
    if useaur == True:
        urllib.request.urlretrieve(ylistu, "sources/ylist.txt")
    else:
        print("yay/aur disabled, not fetching ylist")
def setWallpaper(addwallpaper, imgu):
    if not os.path.exists("wallpaper"):
        os.mkdir("wallpaper")
    if addwallpaper == False:
        print("adding a wallpaper disabled, skipping")
    else:
        print(f"Now downloading from {imgu}")
        req = urllib.request.Request(
            imgu, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
            } # cloudflare doesn't like me, try this to make it avoid 403ing
        )
        f = urllib.request.urlopen(req)
        print(f)
        with open("wallpaper/downloaded.png", "wb") as file:
            file.write(f.read())
            # urllib.request.urlopen('http://www.gunnerkrigg.com//comics/00000001.jpg').read()
            file.close()
        os.system("plasma-apply-wallpaperimage wallpaper/downloaded.png")
        print("Do NOT delete the wallpaper directory! It is still being used by your system to get the wallpaper and will be reset if missing.")