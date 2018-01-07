import os
i = 0

s = int(input('Введите количество файлов'))
while(i <= s)://all files cycle
    i=i+1
    navFiles = []
    files = []//files array creating

    files = os.listdir(os.curdir)//making list of files in dir
    print(files)

    prevName = files[1]
//working dir set
    dir_work = os.listdir(os.curdir)
    a = len (dir_work)
    print (a)
    if (prevName[-3:-1] == 'na')://searching nav-file
            secondName = 'sampleFolder/' + prevName[0:-4] + '.N'
            os.rename(prevName,secondName)//rename nav-file

    if (prevName[-3:-1] == 'ob')://searching obs-file
            secondName = 'sampleFolder/' + prevName[0:-4] + '.O'
            os.rename(prevName,secondName)//rename obs-file

#Можно будет добавить ещё другие информационные сообщения (.R - глонасс и .G)


