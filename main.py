saraksts = [int(sk) for sk in input("Ievadi skaitius, atdalot tos ar atstarpi:").split()]
for i in range(len(saraksts)-1):
  if saraksts[i] == saraksts[i + 1]:
    print(saraksts[i], saraksts[i + 1])
#tests: 2 2 4 4 8 9
#izvade: 2 2; 4 4