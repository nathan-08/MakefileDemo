''' decToOct '''
import sys
def f(n: int, base: int) -> str:

    symbols = '0123456789abcdefghijklmnopqrstuvxyz'
    symbols +='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols +='!@#$%^&*-=+?'
    assert base < len(symbols), "program not configured for base of this size"
    word = ''
    while n > 0:
        r = n % base
        n = n // base
        word += symbols[r]
    return word[::-1]

if __name__ == "__main__":
    assert len(sys.argv)==3, "args: number, base"
    n = int(sys.argv[1])
    base = int(sys.argv[2])
    r = f(n,base)
    print(f'{n} in base {base}: {r}')

