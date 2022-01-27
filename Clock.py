import termcolor
import os
os.system('color')

print("\n \n")
print(termcolor.colored("      .g8'''bgd '7MM                                             ", "yellow")) 
print(termcolor.colored("    .dP'     `M   MM                                             ", "yellow")) 
print(termcolor.colored("    dM'       `   MM   ,pW'Wq.    ~p6'bo   ,pW'Wq.  '7MM  `7MM   ", "yellow")) 
print(termcolor.colored("    MM            MM  6W'   `Wb  6M'  OO  6W'   `Wb   MM    MM   ", "yellow")) 
print(termcolor.colored("    MM.           MM  8M     M8  8M       8M     M8   MM    MM   ", "yellow")) 
print(termcolor.colored("    `Mb.     ,'   MM  YA.   ,A9  YM.    , YA.   ,A9   MM    MM   ", "yellow")) 
print(termcolor.colored("      `'bmmmd'  .JMML. `Ybmd9'    YMbmd'   `Ybmd9'    `Mbod'YML.  \n \n \n", "yellow"))   
print(termcolor.colored("rahnam : salam! dar ebtada saate shoro' ro vared nomaieed. deghghat konid ke saat be sorate AA:AA vared shavad na shekle dige ie. ba'd saate payan ra vared konid v sabr konid ta mohasebe anjam shavad \n\n\n" , "red"))

clockFinal = int()
minFinal = int()
finalClock = list()
nameList = list()
num = int(input(termcolor.colored("tedad afrad morede nazar baraye mohasebe ==> " , "green")))
if num == '0':
    exit()

for i in range(num):
    name = input(termcolor.colored("|  esme farde " + str(i + 1) + "==> ", "green"))
    nameList.append(name)
    monthDay = int(input(termcolor.colored("|   |   tedad rooz haye mahe morede mohasebe baraye *"+ str(nameList[i]) + "* ==> " , "green" )))

    if name == 0:
        exit()

    j = 0

    while (j < monthDay):
        print(termcolor.colored("|   |   |", "blue"))
        print(termcolor.colored("|   |   |", "blue"))
        print(termcolor.colored("|   |   |", "blue"))
        print(termcolor.colored("|   |   |   ettelaate rooz "+ str(j + 1) + " mah , baraye *" + str(nameList[i]) + "* :" ,"blue"))
        
        print(termcolor.colored("|   |   |   |", "blue"))
        list1 = list(input(termcolor.colored("|   |   |   |    saat shoro ra vared nomaieed ==> " , "blue")))
        list2 = list(input(termcolor.colored("|   |   |   |    saat payan ra vared nomaieed ==> ", "blue")))

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

        clockFinal = clockFinal + sum1
        minFinal = minFinal + sum2

        j += 1
    
    clockFinal = clockFinal + (minFinal // 60)
    minFinal = minFinal % 60

    finalClock.append(clockFinal)
    finalClock.append(minFinal)

temp = 0

for i in range(0 , len(finalClock) , 2):
    print("\n\n\nmajmo saate kare *"+ str(nameList[temp]) + "* barabar ast ba ==> "+ str(finalClock[i]) ,"saat v "+ str(finalClock[i + 1]) +" daghighe")
    temp = temp + 1

input(termcolor.colored("\n\nbaraye khoroj Enter bezanid", "blue"))
exit()