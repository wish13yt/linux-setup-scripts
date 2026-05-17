# Howdy ho, neighborino!
# This is designed for me in specific, but there is an option
import pkghelper as p
useaur = True # change me to False if you don't trust the AUR
print("These scripts, linux-setup-scripts (LSS) are licensed under the Unlicense, meaning this script has NO liablity or warrenty.")
print("arch.py also assumes you use pacman and yay, no other installers are supported")
print("I'm also assuming you use KDE and its apps were preinstalled, so those will not be included.")
if useaur == True:
    ylistu = input("If there's a specific source you want to use for your yay packages, input it now. Otherwise, I'll just use the default (Wish's ylist.txt). ") or "https://wish13yt.github.io/linux-setup-scripts/arch/ylist.txt"
else:
    ylistu = ""
plistu = input("If there's a specific source you want to use for your pacman packages, input it now. Otherwise, I'll just use the default (Wish's plist.txt). ") or "https://wish13yt.github.io/linux-setup-scripts/arch/plist.txt"
p.startSudo()
p.updateArch()
p.fetchLists(plistu, ylistu, useaur)
with open("sources/plist.txt", "r") as f:
    for i in f:
        p.pacman(ppkg=i)
with open("sources/ylist.txt", "r") as f:
    for i in f:
        p.yay(ypkg=i)