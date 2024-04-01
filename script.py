import sys
sys.set_int_max_str_digits(2147483647)

def eratosthenes_sieve(limit):
    limitn = limit+1
    primes = dict()
    for ind, val in enumerate([True] * limitn): primes[ind] = val

    primes[0] = primes[1] = False

    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False] * (((limit - ind)//ind) - 1)
    return primes

limit = pow(2, 37)
primes = eratosthenes_sieve(limit)

c = 1
z=0
T=0
mo=0
ja=0
wow=0
mom=0

while c<=limit:
    if primes[c] and primes[2*c-1]:
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
