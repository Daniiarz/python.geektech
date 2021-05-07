#задание 1
# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print(x+y)
#         elif s == '-':
#             print(x-y)
#         elif s == '*':
#             print(x*y)
#         elif s == '/':
#             if y != 0:
#                 print(x/y)
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")


#задание 2
a = 10
b = 2
a, b = b, a
print(b, a)