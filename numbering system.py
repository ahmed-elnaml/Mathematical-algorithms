""" Converting to deciaml 10-base number"""

def digit_printer(x):
    if str(x).isalpha():
        return ord(str(x).upper())-55
    elif str(x).isdigit():
        return int(x)
def to_dec(s,base=2):
    user_input=str(s)[::-1]
    my_value=0
    for (i,num) in enumerate(user_input):
        my_value=my_value+digit_printer(num)*base**i
    return my_value
def back_converter(n):
    x=int(n)
    if x<10:
        return x
    else:
        return chr(x+55)
def from_dec(s,base=2):
    my_input=s
    output=[]
    while my_input>=base:
        output.append(back_converter(my_input%base))
        my_input=my_input//base
    else:
        output.append(back_converter(my_input ))
    result=""
    for i in output[::-1]:
        result+=str(i)
    return  result
"""fractional converter"""
#  convert to decimal
def f2dec(n,base):
    sum_=0
    for (i,digit) in enumerate(str(n)):
        sum_+=digit_printer(digit)*base**(-(i+1))
    return str(sum_)
# convert to base
def f4dec(n,base):
    num=float(n)
    result=[]
    counter=0
    while num>=10**(-10) and counter<31:
            num=num*base
            result.append(back_converter(num//base))
            num=num%base
            counter+=1
    result2 = ""
    for i in result[1:]:
        result2 += str(i)
    return result2

def base_converter(n,from_,to_):
    if not('.' in str(n)):
        x=to_dec(n,from_)
        return from_dec(x,to_)
    else:
        l=str(n).split('.')
        x = to_dec(l[0], from_)
        r1=from_dec(x,to_)
        f_x=f2dec(l[1],from_)
        r2=f4dec(f_x,to_)
    return r1+'.'+r2


print(base_converter('0.05', 14, 100))
