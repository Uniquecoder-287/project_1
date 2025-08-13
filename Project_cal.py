def sum(a,b):
    return a + b

def sub(a, b):
    return a - b

def mult(a,b):
    return a * b

def div(a, b):
    return (a / b)

def avg(a, b):
    return (a + b) / 2


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print('select operation')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('5. Average')

choice= input("Enter choice: ")

if choice == '1':
    print("Sum of two elements is",sum(a,b))
elif choice== '2':
    print("Sub of the two elements is ",sub(a,b))
elif choice == '3':
    print("Multi of the two numers are ",mult(a,b))
elif choice == '4':
    print("div of the two numers are ",div(a,b))
elif choice == '5':
    print("avg of the two numers are ",avg(a,b))
else:
    print("Invalid choice")