from xlwt import Workbook
import xlwt
import termcolor
import os
os.system('color')

print("\n\n")
print(termcolor.colored("      █████████   ████  ", )) 
print(termcolor.colored("     ███░░░░░███░ ░███                                       ", )) 
print(termcolor.colored("    ███     ░░░   ░███    ██████    ██████    ██████   █████ ████", )) 
print(termcolor.colored("   ░███           ░███   ███░░███  ███░░███  ███░░███ ░░███ ░███ ", )) 
print(termcolor.colored("   ░███           ░███  ░███ ░███ ░███ ░░░  ░███ ░███  ░███ ░███ ", )) 
print(termcolor.colored("   ░░███     ███  ░███  ░███ ░███ ░███  ███ ░███ ░███  ░███ ░███ ", )) 
print(termcolor.colored("    ░░█████████   █████ ░░██████  ░░██████  ░░██████   ░░████████", )) 
print(termcolor.colored("     ░░░░░░░░░   ░░░░░   ░░░░░░    ░░░░░░    ░░░░░░     ░░░░░░░░  \n\n\n", )) 

boldStyle = xlwt.easyxf('font: name Salma Alfasans Med, color-index blue, bold on ')
boldStyle2 = xlwt.easyxf('font: name Salma Alfasans Med, color-index red, bold on')

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

num = int(input(termcolor.colored("Number of people calculated ==> " , "yellow")))
if num == '0':
    exit()

for i in range(num):
    clockFinal = int()
    minFinal = int()
    name = str(input(termcolor.colored("|  Name of person " + str(i + 1) + "==> ", "green")))
    nameList.append(name)

    sheet1.write(i + 1, 0, name, boldStyle)

    monthDay = int(input(termcolor.colored("|   |   The number of days of the month is calculated for *"+ str(nameList[i]) + "* ==> " , "green" )))

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
                sheet1.write(0, h + 1, "day " + str(h + 1), boldStyle)
        else:
            x = int(monthDay - tempDay)

            for h in range(tempDay, x + 1):
                sheet1.write(0, h + 1, "day " + str(h + 1), boldStyle)
        

    while (j < monthDay):
        print(termcolor.colored("|   |   |", "cyan"))
        print(termcolor.colored("|   |   |", "cyan"))
        print(termcolor.colored("|   |   |", "cyan"))
        print(termcolor.colored("|   |   |   Information day "+ str(j + 1) + " month , for *" + str(nameList[i]) + "* :" ,"cyan"))
        
        print(termcolor.colored("|   |   |   |", "cyan"))
        print(termcolor.colored("|   |   |   |   Make sure the clock is entered as AA:AA" , "red"))

        list1 = list(input(termcolor.colored("|   |   |   |    Start time ==> " , "cyan")))
        list2 = list(input(termcolor.colored("|   |   |   |    End time ==> ", "cyan")))

        if (len(list1) > 5 or len(list2) > 5) or (len(list1) < 5 or len(list2) < 5) :
            print(termcolor.colored("\n\n***The clock entered is incorrect. Re-enter day " + str(j + 1) + " information***" , "red"))
            ex = input(termcolor.colored("Press **Enter** to continue.....Press **0** to exit", "green"))
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
            print(termcolor.colored("\n\n\n***The clock entered is incorrect. Re-enter day " + str(j + 1) + " information***" , "red"))
            ex = input(termcolor.colored("Press **Enter** to continue.....Press **0** to exit", "green"))
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
    print("\n\n\n" + str(nameList[temp]) + "'s total working Clock are equal to ==> "+ str(finalClock[i]) ,"hours and "+ str(finalClock[i + 1]) +" minutes")
    temp = temp + 1
    sheet1.write(temp , dayCount + 1, str(finalClock[i]) + ':' + str(finalClock[i + 1]))

sheet1.write(0 , dayCount + 1 , 'Total', boldStyle2)


while True:
    status = input(termcolor.colored("\n\nCreate a calculation Excel file?[Y,n] ==> ", "yellow"))
    if status == 'y' or 'Y' or 'yes' or 'Yes' :
        wb.save('Clucou.xls')
        exit()
    elif status == 'n' or 'N' or 'no' or 'No':
        status1 = input(termcolor.colored("\n\nAre you sure? In this case, the calculations are deleted.[Yes,Cancel]==> ", "yellow"))
        if status1 == 'yes' or 'Y' or 'y' or 'Yes':
            exit()
        elif status1 == 'no' or 'n' or 'N' or 'Cancel' or 'cancel' or 'c' or 'C':
            continue
        else:
            input(termcolor.colored("\n\nOnly possible items can be entered. Not anything else ", "yellow"))    
    else:
        input(termcolor.colored("\n\nOnly possible items can be entered. Not anything else ==> ", "yellow"))