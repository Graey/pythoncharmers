TimesTable = int(input("Please Choose A Times Table To Be Quizzed On;\n1)One Times Tables\n2)Two Times Tables\n3)Three Times Tables\n4)Four Times Tables\n5)Five Times Tables\n6)Six Times Tables\n7)Seven Times Tables\n8)Eight Times Tables\n9)Nine Times Tables\n10)Ten Times Tables\n11)Eleven Times Tables\n12)Twelve Times Tables\nPlease Choose One To Start: "))

No1 = 1
ans = 0


for x in range (12):
    ans = No1 * TimesTable
    print("\n",No1,"x",TimesTable,"=",ans)
    No1 = No1 + 1
