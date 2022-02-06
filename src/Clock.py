from defs import banner;

class Clocuo:

    def __init__(self) -> None:
        pass

    def start():
        print(banner)
        print("rahnam : salam! dar ebtada saate shoro' ro vared nomaieed. "\
            "deghghat konid ke saat be sorate AA:AA vared shavad na shekle dige ie. "\
            "ba'd saate payan ra vared konid v sabr konid ta mohasebe anjam shavad\n\n"
        )                                                                                                                                                                       

        clockFinal = int()
        minFinal = int()
        finalClock = list()
        nameList = list()
        num = int(input("tedad afrad morede nazar baraye mohasebe ==>"))

        for i in range(num):
            name = input("esme farde " + str(i + 1) + "==>")
            nameList.append(name)
            monthDay = int(input("tedad rooz haye mahe morede mohasebe baraye *" + str(nameList[i]) + "* ==>"))

            j = 0
            while (j < monthDay):
                print("")
                print("")
                print("ettelaate rooz", j + 1, "mah , baraye *" , nameList[i] , "*")
                
                list1 = list(input("saat shoro ra vared nomaieed ==>"))
                list2 = list(input("saat payan ra vared nomaieed ==>"))

                if (len(list1) > 5 or len(list2) > 5) or (len(list1) < 5 or len(list2) < 5):
                    print("\n\n***saate vared shode eshtebah ast. ettelaate rooz" + str(j + 1) + " ra dobare vared konid***" )
                    input("baraye edame Enter bezanid")
                    j = j - 1
                    continue


                one1 = int(list1[0])
                one2 = int(list2[0])
                three1 = int(list1[3])
                three2 = int(list2[3])

                saat1 = (one1 * 10) + int(list1[1])
                saat2 = (one2 * 10) + int(list2[1])
                min1 = (three1 * 10) + int(list1[4])
                min2 = (three2 * 10) + int(list2[4])

                if saat1 > 23 or saat2 > 23 or min1 > 59 or min2 > 59:
                    print("\n\n\nsaate vared shode eshtebah ast. dobare talash konid")
                    input("\n\n\nbaraye khoroj Enter bezanid")
                    exit()

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
            print("")
            print("")
            print("majmo saate kare *",nameList[temp] , "* barabar ast ba ==>", finalClock[i] ,"saat v", finalClock[i + 1] ," daghighe")
            temp = temp + 1

        input("\n\nbaraye khoroj Enter bezanid")
        return;