n = int(input('Enter an intiger number : '))
st = ""
while n!=0:
    q=n//8
    r=n%8
    n=q
    st=str(r)+st
print('Octal value is : '+ st)
