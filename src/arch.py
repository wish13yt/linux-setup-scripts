# Howdy ho, neighborino!
# This is designed for me in specific, but there is an option
import pkghelper as p
useaur = True # change me to False if you don't trust the AUR
addwallpaper = False # change me to True if you want a wallpaper
# NOTE: Wallpaper is BUGGY!! Only works for KDE Plasma and doesn't change the wallpaper from my testing.
# Also depends on plasma-apply-wallpaperimage
print("These scripts, linux-setup-scripts (LSS) are licensed under the Unlicense, meaning this script has NO liablity or warrenty.")
print("arch.py also assumes you use pacman and yay, no other installers are supported")
print("I'm also assuming you use KDE and its apps were preinstalled, so those will not be included.")
if useaur == True:
    ylistu = input("If there's a specific source you want to use for your yay packages, input it now. Otherwise, I'll just use the default (Wish's ylist.txt). ") or "https://wish13yt.github.io/linux-setup-scripts/arch/ylist.txt"
else:
    ylistu = ""
plistu = input("If there's a specific source you want to use for your pacman packages, input it now. Otherwise, I'll just use the default (Wish's plist.txt). ") or "https://wish13yt.github.io/linux-setup-scripts/arch/plist.txt"
if addwallpaper == True:
    imgu = input("What image URL would you like to use for your background? Otherwise, I'll choose Wish's default (@5quirre1's white flowers close-up image). ") or "https://squirrelz.xyz/assets/misc/photos-i-took/2026/102_0978.JPG"
else:
    imgu = ""
p.startSudo()
p.updateArch()
p.fetchLists(plistu, ylistu, useaur)
with open("sources/plist.txt", "r") as f:
    for i in f:
        p.pacman(ppkg=i)
with open("sources/ylist.txt", "r") as f:
    for i in f:
        p.yay(ypkg=i)
p.setWallpaper(addwallpaper, imgu)