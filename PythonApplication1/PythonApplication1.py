def Test(a):
    if isinstance(a, str):
        return("문자 : " + a)
    elif isinstance(a, int):
        return("숫자 : " + str(a))

a = input("input : ")
try:
   b = int(a)
except ValueError:
    b = a

print(Test(b))