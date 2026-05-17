import debhelper as d
print("These scripts, linux-setup-scripts (LSS) are licensed under the Unlicense, meaning this script has NO liablity or warrenty.")
print("deb.py also assumes you use apt, no other installers are supported")
print("Also is untested for now as im not running debian")
dlistu = input("If there's a specific source you want to use for your apt packages, input it now. Otherwise, I'll just use the default (Wish's dlist.txt). ") or "https://wish13yt.github.io/linux-setup-scripts/debian/dlist.txt"
d.startSudo()
d.fetchList(dlistu)
d.update()
with open("sources/dlist.txt", "r") as f:
    for i in f:
        d.apt(apkg=i)