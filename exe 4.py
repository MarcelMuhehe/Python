Maths = int(input("Maths: "))
if Maths <0 or Maths > 100:
    print("Invalid input")
Physics = int(input("Physics: "))
if Physics <0 or Physics > 39:
    print("Invalid input")
English = int(input("English: "))
if English <0 or English > 100:
    print("Invalid input")
History = int(input("History: "))
if History <0 or History > 100:
    print("Invalid input")
Chemistry = int(input("Chemistry: "))
if Chemistry <0 or Chemistry > 100:
    print("Invalid input")
Avg = (Maths + Physics + English + History + Chemistry)/5

if Avg >=0 and Avg <= 39:
    print("E")
elif Avg >= 40 and Avg <= 50:
    print("D")
elif Avg >= 51 and Avg <= 60:
    print("C")
elif Avg >= 61 and Avg <= 70:
    print("B")
elif Avg >= 71 and Avg <= 100:
    print("A")
else:
    print("Error")

