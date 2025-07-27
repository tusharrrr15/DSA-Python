def extract_digit(n):
    num = n
    while num>0:
        ld = num%10
        print(ld)
        num = num//10
n = 5873
extract_digit(n)