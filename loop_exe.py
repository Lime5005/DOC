# calculate the salary, >40h is overtime
hrs = input("Enter Hours:\n")
h = float(hrs)
try:
    h = float(hrs)
except:
    h = -1
rate = input("Enter Rate:\n")
r = float(rate)
try:
    r = float(rate)
except:
    r = -1
if h <= 40:
    pay = h * r
elif h > 40:
        pay = 40 * r + (h - 40) * r * 1.5
print(pay)

# Using def:
def computepay(h,r):
    if h <= 40:
       return h * r
    elif h > 40:
       return (h - 40) * 1.5 * r + 40 * r
hrs = input('enter hours:\n')
h = float(hrs)
rate = input('enter the rate:\n')
r = float(rate)
p = computepay(h,r)
print('Pay',p)

# calculate the score of a sport
score = input("Enter Score:\n")
s = float(score)
if s >= 1.0 or s != float(score):
    print('Bad score')
    quit()
elif s >= 0.9:
    print('A')
elif s >= 0.8:
    print('B')
elif s >= 0.7:
    print('C')
elif s >= 0.6:
    print('D')
elif s < 0.6:
    print('F')

# while loop
largest = None
smallest = None

while True:  # 这里是一个无限循环
    num = input("Enter a number: ")
    if num == "done":
        break     # 这里是无限循环的开关
    try:          # 先上一个保险
        num = int(num)

        if largest == None:
            largest = num
        elif largest < num:
            largest = num
        if smallest == None:
            smallest = num
        elif smallest > num:
            smallest = num
    except:      # 保险的开关
        print("Invalid input")
    continue    # 继续无限循环

print("Maximum is",largest)
print("Minimum is",smallest)

# another way
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
    continue
for largest in [0,num]:
    if largest == None:
        largest = largest
    elif largest < num:
        largest = num
for smallest in [0,num]:
    if smallest == None:
        smallest = smallest
    elif smallest > num:
        smallest = num
print("Maximum is",largest)
print("Minimum is",smallest)
