# Howdy ho, neighborino!
# This is designed for me in specific, but there is an option
import pkghelper as p
print("NOTICE: linux-setup-scripts (LSS) provides packages that, by default, pulls from the AUR. These scripts are licensed under the Unlicense, leaving NO liablity or warrenty.")
print("tldr: I'm not responsible for any stuff this script does to your computer")
print("AUR packages may become malicious at any moment, and you must be careful what you install.")
print("If you don't trust the AUR, press space and enter on the following question.")
ylistu = input("If there's a specific source you want to use for your yay packages, input it now. Otherwise, I'll just use the default (Wish's ylist.txt). ") or 
plistu = input("If there's a specific source you want to use for your pacman packages, input it now. Otherwise, I'll just use the default (Wish's plist.txt). ")
p.startSudo()
p.updateArch()
with open("plist.txt", "r") as f:
    for i in f:
        p.pacman(ppkg=i)