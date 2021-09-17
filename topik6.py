# Topik 6 : For loop

for _ in range(5):
  print("hello")

for i in range(3):
  print(i)

for number in range(7):
    if number == 4:
        continue
    print('Number is ' + str(number))
print('The end')

for number in range(7):
    if number == 4:
        break
    print('Number is ' + str(number))
print('The end')

for number in range(7):
    if number == 4:
        pass
    print('Number is ' + str(number))
print('The end')