import random
import math


print("=======================================================\n\n")
print("      SELAMAT DATANG DI PERMAINAN TEBAK ANGKA\n\n")
print("=======================================================")
minimum=int(input("Masukan angka minimum : "))
maximum=int(input("Masukan angka maksimum : "))

hiddenAnswer=random.randint(minimum,maximum)

maxRoundtxt=round(math.log(maximum-minimum+1,2))

print("Anda memiliki ",maxRoundtxt," kesempatan, jangan sia-siakan")

answerCount=0
maxRound=math.log(maximum-minimum+1,2)
while answerCount<maxRound:
    answerCount+=1

    answer=int(input("Masukan jawaban anda : "))

    if hiddenAnswer<answer:
        print("Terlalu besar")
    elif hiddenAnswer>answer:
        print("Terlalu kecil")
    elif hiddenAnswer==answer:
        print("Selamat, anda benar!!")
        print("Total tebakan yang anda gunakan adalah sebesar ",answerCount)

if answerCount>=maxRound:
    print("Sayang sekali anda telah melewati batas kesempatan yang diberikan")
    print("Jawaban yang benar adalah : ",hiddenAnswer)
