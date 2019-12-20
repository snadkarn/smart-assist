k=int(input('enter the value of k : '))
str=input('enter the string to be encoded : ')
msg=''
for x in str:
    a=ord(x)
    a=a+k
    msg=msg+chr(a)
print('The plaintext msg is : ',str)
print('the encoded cipher is : ',msg)
