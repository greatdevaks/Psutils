import psutil

vec = psutil.pids()

for i in vec:
    if(psutil.Process(i).name() == "POWERPNT.EXE" or psutil.Process(i).name() == "WINWORD.EXE" or psutil.Process(i).name() == "Acrobat.exe"):
        file = psutil.Process(i).open_files()
        for x in file:
            if ("docx" in str(x) or "pptx" in str(x)):
                res = str(x).strip("popenfile(path='")
                res = res.strip("', fd=-1)")
                print(res)
            elif ("pdf" in str(x)):
                res = str(x).strip("popenfile(path='")
                res = res.strip("', fd=-1)") + "df"
                print(res)

