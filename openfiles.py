import psutil
import shutil

vec = psutil.pids()

file_list = []

for i in vec:
    if(psutil.Process(i).name() == "POWERPNT.EXE" or psutil.Process(i).name() == "WINWORD.EXE" or psutil.Process(i).name() == "Acrobat.exe"):
        file = psutil.Process(i).open_files()
        for x in file:
            if ("docx" in str(x) or "pptx" in str(x)):
                res = str(x).strip("popenfile(path='")
                res = res.strip("', fd=-1)")
                print(res)
                strippedRes = res.rsplit("\\", 1)[1]
                shutil.copyfile(res, "C:\\Users\\Anmol-Sachdeva\\PycharmProjects\\Psutils\\" + strippedRes)
                file_list.append(strippedRes)
            elif ("pdf" in str(x)):
                res = str(x).strip("popenfile(path='")
                res = res.strip("', fd=-1)") + "df"
                strippedRes = res.rsplit("\\", 1)[1]
                print(res)
                shutil.copyfile(res, "C:\\Users\\Anmol-Sachdeva\\PycharmProjects\\Psutils\\" + strippedRes)
                file_list.append(strippedRes)

print(file_list)




