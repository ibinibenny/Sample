# compressing multiple files 


import tarfile
tar = tarfile.open("hasilu.tar.xz", "w:xz")
for name in ["b.py", "zip.py", "time.py"]:
    tar.add(name)
    print(name)
tar.close()