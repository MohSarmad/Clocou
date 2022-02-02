from xlwt import Workbook
import xlwt
import termcolor
import os
os.system('color')

print("\n \n")
print(termcolor.colored("      .g8'''bgd '7MM                                             ", )) 
print(termcolor.colored("    .dP'     `M   MM                                             ", )) 
print(termcolor.colored("    dM'       `   MM   ,pW'Wq.    ~p6'bo   ,pW'Wq.  '7MM  `7MM   ", )) 
print(termcolor.colored("    MM            MM  6W'   `Wb  6M'  OO  6W'   `Wb   MM    MM   ", )) 
print(termcolor.colored("    MM.           MM  8M     M8  8M       8M     M8   MM    MM   ", )) 
print(termcolor.colored("    `Mb.     ,'   MM  YA.   ,A9  YM.    , YA.   ,A9   MM    MM   ", )) 
print(termcolor.colored("      `'bmmmd'  .JMML. `Ybmd9'    YMbmd'   `Ybmd9'    `Mbod'YML.  \n \n \n", ))   
print(termcolor.colored("rahnam : salam! dar ebtada saate shoro' ro vared nomaieed\n. deghghat konid ke saat be sorate AA:AA vared shavad na shekle dige ie\n. ba'd saate payan ra vared konid v sabr konid ta mohasebe anjam shavad \n\n\n" , "red"))

boldStyle =  xlwt.easyxf('font: name Salma Alfasans Med, color-index blue, bold on ')
boldStyle2 =  xlwt.easyxf('font: name Salma Alfasans Med, color-index red, bold on')

wb = Workbook()
sheet1 = wb.add_sheet('sheet1')
sheet1.col(0).width = 7000

y = int()
tempDay = 0
clockFinal = int()
minFinal = int()
finalClock = list()
nameList = list()
dayCount = int()

num = int(input(termcolor.colored("tedad afrad morede nazar baraye mohasebe ==> " , "yellow")))
if num == '0':
    exit()

for i in range(num):
    clockFinal = int()
    minFinal = int()
    name = str(input(termcolor.colored("|  esme farde " + str(i + 1) + "==> ", "green")))
    nameList.append(name)

    sheet1.write(i + 1, 0, name, boldStyle)

    monthDay = int(input(termcolor.colored("|   |   tedad rooz haye mahe morede mohasebe baraye *"+ str(nameList[i]) + "* ==> " , "green" )))

    if name == 0:
        exit()

    j = 0

    if monthDay > dayCount:
        dayCount = monthDay

    if monthDay > tempDay :
        y += 1
        if y <= 1:
            tempDay = monthDay

            for h in range(monthDay):
                sheet1.write(0, h + 1, "rooz " + str(h + 1), boldStyle)
        else:
            x = int(monthDay - tempDay)

            for h in range(tempDay, x + 1):
                sheet1.write(0, h + 1, "rooz " + str(h + 1), boldStyle)
        

    while (j < monthDay):
        print(termcolor.colored("|   |   |", "cyan"))
        print(termcolor.colored("|   |   |", "cyan"))
        print(termcolor.colored("|   |   |", "cyan"))
        print(termcolor.colored("|   |   |   ettelaate rooz "+ str(j + 1) + " mah , baraye *" + str(nameList[i]) + "* :" ,"cyan"))
        
        print(termcolor.colored("|   |   |   |", "cyan"))
        list1 = list(input(termcolor.colored("|   |   |   |    saat shoro ra vared nomaieed ==> " , "cyan")))
        list2 = list(input(termcolor.colored("|   |   |   |    saat payan ra vared nomaieed ==> ", "cyan")))

        if (len(list1) > 5 or len(list2) > 5) or (len(list1) < 5 or len(list2) < 5) :
            print(termcolor.colored("\n\n***saate vared shode eshtebah ast. ettelaate rooz" + str(j + 1) + " ra dobare vared konid***" , "red"))
            ex = input(termcolor.colored("baraye edame Enter bezanid...baraye khoroj 0 bezanid", "green"))
            if ex == '0':
                exit()
            continue



        one1 = int(list1[0])
        one2 = int(list2[0])
        three1 = int(list1[3])
        three2 = int(list2[3])

        saat1 = (one1 * 10) + int(list1[1])
        saat2 = (one2 * 10) + int(list2[1])
        min1 = (three1 * 10) + int(list1[4])
        min2 = (three2 * 10) + int(list2[4])

        if saat1 > 23 or saat2 > 23 or min1 > 59 or min2 > 59 :
            print(termcolor.colored("\n\n\nsaate vared shode eshtebah ast. dobare talash konid" , "red"))
            ex = input(termcolor.colored("baraye edame Enter bezanid...baraye khoroj 0 bezanid", "green"))
            if ex == '0':
                exit()
            continue


        temp1 = saat1
        sum1 = int()

        temp2 = min1
        sum2 = int()

        if min1 > min2 :
            while temp2 <= 59 :
                temp2 += 1
                sum2 += 1
            sum2 = sum2 + min2
            temp1 += 1
            
        if min2 > min1 :
            while temp2 < min2 :
                temp2 += 1
                sum2 += 1              

        if saat1 > saat2 :
            while temp1 < 24:
                temp1 += 1
                sum1 += 1
            temp1 = 1
            
            while temp1 <= saat2:
                temp1 += 1
                sum1 += 1
        if saat2 > saat1 :
            while temp1 < saat2:
                temp1 += 1
                sum1 += 1 

        clockFinalExcel = int(sum1)
        minFinalExcel = int(sum2)

        clockFinal = clockFinal + sum1
        minFinal = minFinal + sum2

        clockFinal = clockFinal + (minFinal // 60)
        minFinal = minFinal % 60

        strClock = str(clockFinalExcel)
        strMin = str(minFinalExcel)

        sheet1.write(i + 1 , j + 1 , strClock + ':' + strMin)

        j += 1
    
    clockFinal = clockFinal + (minFinal // 60)
    minFinal = minFinal % 60

    finalClock.append(clockFinal)
    finalClock.append(minFinal)

temp = 0

for i in range(0 , len(finalClock) , 2):
    print("\n\n\nmajmo saate kare *"+ str(nameList[temp]) + "* barabar ast ba ==> "+ str(finalClock[i]) ,"saat v "+ str(finalClock[i + 1]) +" daghighe")
    temp = temp + 1
    sheet1.write(temp , dayCount + 1, str(finalClock[i]) + ':' + str(finalClock[i + 1]))

sheet1.write(0 , dayCount + 1 , 'majmoo', boldStyle2)


while True:
    status = input(termcolor.colored("\n\nfile Excel mohasebat tashkil shavad?(yes, no)==> ", "yellow"))
    if status == 'yes' :
        wb.save('Clucou.xls')
        exit()
    elif status == 'no':
        status1 = input(termcolor.colored("\n\naya motmaennid? dar insoorat mohasebate shoma pak mishavad...(yes, no)==> ", "yellow"))
        if status1 == 'yes':
            exit()
        elif status1 == 'no':
            continue
        else:
            input(termcolor.colored("\n\ntanha 'yes' ya 'no' zade shavad ==> ", "yellow"))    
    else:
        input(termcolor.colored("\n\ntanha 'yes' ya 'no' zade shavad ==> ", "yellow"))