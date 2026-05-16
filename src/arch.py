# Howdy ho, neighborino!
# This is designed for me in specific, but there is an option
import pkghelper as p
plistu = input("If there's a specific source you want to use for your pacman packages, input it now. Otherwise, I'll just use the default (Wish's plist.txt). ")
ylistu = input("If there's a specific source you want to use for your yay packages, input it now. Otherwise, I'll just use the default (Wish's ylist.txt). ")
p.startSudo()
p.updateArch()
with open("plist.txt", "r") as f:
    for i in f:
        p.pacman(ppkg=i)