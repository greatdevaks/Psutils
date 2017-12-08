# import psutil
# import shutil

# vec = psutil.pids()

# file_list = []

# for i in vec:
#     if(psutil.Process(i).name() == "POWERPNT.EXE" or psutil.Process(i).name() == "WINWORD.EXE" or psutil.Process(i).name() == "Acrobat.exe"):
#         file = psutil.Process(i).open_files()
#         for x in file:
#             if ("docx" in str(x) or "pptx" in str(x)):
#                 res = str(x).strip("popenfile(path='")
#                 res = res.strip("', fd=-1)")
#                 print(res)
#                 strippedRes = res.rsplit("\\", 1)[1]
#                 shutil.copyfile(res, "C:\\Users\\Anmol-Sachdeva\\PycharmProjects\\Psutils\\" + strippedRes)
#                 file_list.append(strippedRes)
#             elif ("pdf" in str(x)):
#                 res = str(x).strip("popenfile(path='")
#                 res = res.strip("', fd=-1)") + "df"
#                 strippedRes = res.rsplit("\\", 1)[1]
#                 print(res)
#                 shutil.copyfile(res, "C:\\Users\\Anmol-Sachdeva\\PycharmProjects\\Psutils\\" + strippedRes)
#                 file_list.append(strippedRes)

# print(file_list)

# for i in vec:
#     #print(psutil.Process(i).cwd())
#     # print(psutil.Process(i).pid)
#     # print(psutil.Process(i).name())
#     if(psutil.Process(i).pid == 10496):
#         print(psutil.Process(i).name())






import psutil
import shutil
import operator

vec = psutil.pids()

file_list = []
file_atime = {}
import time
import os
import datetime
import glob
for i in vec:
    if(psutil.Process(i).name() == "POWERPNT.EXE" or psutil.Process(i).name() == "WINWORD.EXE" or psutil.Process(i).name() == "Acrobat.exe"):
        file = psutil.Process(i).open_files()
        for x in file:
            if ("docx" in str(x) or "pptx" in str(x)):
                res = str(x).strip("popenfile(path='")
                res = res.strip("', fd=-1)")
                print(res)
                strippedRes = res.rsplit("\\", 1)[1]
                print(res.replace(strippedRes, ""))
                #for pushing multiple files
                #shutil.copyfile(res, "C:\\Users\\Anmol-Sachdeva\\PycharmProjects\\Psutils\\" + strippedRes)
                file_list.append(strippedRes)
                print(os.path.getatime(res))
                # getatime for getting access time of the file
                file_atime[res] = (os.path.getatime(res))
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(res)
                print(datetime.datetime.fromtimestamp(os.stat(res).st_atime))
                print("last access: %s" % time.ctime(atime))
                print("====")
            elif ("pdf" in str(x)):
                res = str(x).strip("popenfile(path='")
                res = res.strip("', fd=-1)") + "df"
                strippedRes = res.rsplit("\\", 1)[1]
                print(res)
                #for pusing multiple files
                #shutil.copyfile(res, "C:\\Users\\Anmol-Sachdeva\\PycharmProjects\\Psutils\\" + strippedRes)
                file_list.append(strippedRes)
                print(os.path.getatime(res))
                #getatime for getting access time of the file
                file_atime[res] = (os.path.getatime(res))
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(res)
                print(datetime.datetime.fromtimestamp(os.stat(res).st_atime))
                print("last access: %s" % time.ctime(atime))
                print("====")
print(file_list)
print(file_atime)
#for pushing only one file having the latest access time
file_to_upload = max(file_atime.items(), key=operator.itemgetter(1))[0]
print("The latest file accessed is: {}".format(file_to_upload))
strippedRes = file_to_upload.rsplit("\\", 1)[1]
shutil.copyfile(file_to_upload, "C:\\Users\\Anmol-Sachdeva\\PycharmProjects\\Psutils\\" + strippedRes)
