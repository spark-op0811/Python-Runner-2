import sys
sys.set_int_max_str_digits(2147483647)

c = 1
z=0
T=0
mo=0
ja=0
wow=0
mom=0
def is_prime(number):
    if number < 2:
        return 0
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 0
    return 1


while c<=pow(2,37):
    if is_prime(c)==1 and is_prime(2*c-1) == 1 :
        m=(pow(3,c-1)-1)%(2*c-1)
        n=(pow(3,c-1)+1)%(2*c-1)
        
        if m==0:
            mo=mo+1
            mom=mom+n
        if n==0:
            ja=ja+1
            wow=wow+m
        if c>=7 and mom==0:
            print(c)
            break
        
    c=c+1
c=0
print(ja/mo)
print(f"{mom} {wow}")
