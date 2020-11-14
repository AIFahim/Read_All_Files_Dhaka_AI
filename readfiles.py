import glob
a = glob.glob("*.xml")
for _ in a:
	print(_[:-4]+"\n")
with open('rename.txt', 'w') as f:
    for item in a:
        f.write("%s\n" % item[:-4])
