print("masukan nilai");

baris = input("")
baris = int (baris)
for i in range (0, baris):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("")

for i in range (baris, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("")
