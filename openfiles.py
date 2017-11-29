import psutil
import shutil
import operator

vec = psutil.pids()

file_list = []
file_atime = {}
import time
import os
import datetime
for i in vec:
    if(psutil.Process(i).name() == "POWERPNT.EXE" or psutil.Process(i).name() == "WINWORD.EXE" or psutil.Process(i).name() == "Acrobat.exe"):
        file = psutil.Process(i).open_files()
        for x in file:
            if ("docx" in str(x) or "pptx" in str(x)):
                res = str(x).strip("popenfile(path='")
                res = res.strip("', fd=-1)")
                print(res)
                strippedRes = res.rsplit("\\", 1)[1]
                shutil.copyfile(res, "directory_path" + strippedRes)
                file_list.append(strippedRes)
                print(os.path.getatime(strippedRes))
                file_atime[strippedRes] = (os.path.getatime(strippedRes))
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(strippedRes)
                print(datetime.datetime.fromtimestamp(os.stat(strippedRes).st_atime))
                print("last access: %s" % time.ctime(atime))
                print("====")
            elif ("pdf" in str(x)):
                res = str(x).strip("popenfile(path='")
                res = res.strip("', fd=-1)") + "df"
                strippedRes = res.rsplit("\\", 1)[1]
                print(res)
                shutil.copyfile(res, "file_directory_path" + strippedRes)
                file_list.append(strippedRes)
                print(os.path.getatime(strippedRes))
                file_atime[strippedRes] = (os.path.getatime(strippedRes))
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(strippedRes)
                print(datetime.datetime.fromtimestamp(os.stat(strippedRes).st_atime))
                print("last access: %s" % time.ctime(atime))
                print("====")
print(file_list)
print(file_atime)
print("The latest file accessed is: {}".format(max(file_atime.items(), key=operator.itemgetter(1))[0]))
