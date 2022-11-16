skaitli = [int(skaitli) for skaitli in input("levadi skaitlus, atdalot tos ar atstarpi:") .split()]
lielIndex = 0
for i in range(1, len(skaitli)):
  if skaitli[i] > skaitli[lielIndex]:
    lielIndex = i
print("Lielakais skaitlis:", skaitli[lielIndex],
"ar indeksu", lielIndex)
#tests: 2 4 7 9
#izvade: Lielakais skaitlis: 9 ar indeksu 3