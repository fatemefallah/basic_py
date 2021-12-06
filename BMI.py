w = int(input())
h = float(input())
BMI = w / (h * h)
if BMI < 18.5:
    body = "Underweight"
elif 18.5 <= BMI < 25:
    body = "Normal"
elif 25 <= BMI < 30:
    body = "Overweight"
else:
    body = "Obese"
print("%.2f"%BMI)
#print(format(BMI, '.2f'))
print(body)