# import zipfile library
import zipfile
 
# import os library
import os
 
cwd = os.getcwd()
 
# changing to current working directory
os.chdir(cwd)
 
zfile = zipfile.ZipFile('new_archive_file.zip', 'w')
 
for file in cwd:
        # archiving only py files
        if file.endswith("py"):
            zfile.write(file, compress_type=zipfile.ZIP_DEFLATED)
 
zfile.close()