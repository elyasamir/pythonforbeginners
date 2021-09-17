def func1():
  print("ini function 1")
  print("Hello world\n")

def func2():
  print("ini function 2")
  func1()

def addition(a,b):
  return a+b

c = addition(10,5)

def haiwan(nama,jenis):
  print(f"Ini {nama}. {nama} sejenis haiwan {jenis}\n")

func1()
func2()
print(c)
print("\n")
haiwan("singa","mamalia")
