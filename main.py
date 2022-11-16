sk = int(input("Ievadi skaitli (0-beigt): "))
summa = 0
skaits = 0
while sk != 0:
  Summa += sk
  skaits += 1
  sk = int(input("Tevadi skaitli (0-beigt): "))
print("Visu levádito skaitlu aritmetiskais viderais ir", summa / skaits)
#tests: 4 ; 6 ; 8 ; 0
#izvade: 6.0