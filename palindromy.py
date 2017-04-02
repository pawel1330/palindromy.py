slowa = ['aaabaaa', 'aa', 'c', 'bbaa', 'baba', 'abba']

def palindrom(slowo):
    print(slowo)
    a=len(slowo)
    b=a/2
    i=0
    while i < b:
        if slowo[i] == slowo[-1-i]:
            pass
        else:
            print("to nie jest palindrom")
            return False
        i=i+1
    print("to jest palindrom")
    return True
palindrom("aaabaaa")
palindrom("aa")
palindrom("c")
palindrom("bbaa")
palindrom("baba")
palindrom("abba")
palindrom(slowa[0])


def twopal(dlugosc):
    if dlugosc== 1:
        return "b"
    elif dlugosc==2:
        return "bb"
    else:
        return "b"+(dlugosc-2)*"a"+"b"
print("WPISZ DLUGOŚC PALINDROMU:")
slowo=twopal(int(input()))
print(slowo)


def genpal(dlugosc):
    if dlugosc%2==1: #nieparzysty
        return int(dlugosc/2)*"a"+"b"+int(dlugosc/2)*"a"
    else: #parzysty
        return int(dlugosc/2-1)*"a"+"bb"+int(dlugosc/2-1)*"a"
print("Generator palindromów. Wpisz liczbę:")
slowo=genpal(int(input()))
print(slowo)

def genpal(dlugosc):
    if dlugosc%2==1: #nieparzysty
        return int(dlugosc/2)*"a"+"b"+int(dlugosc/2)*"a"
    else: #parzysty
        return int(dlugosc/2-1)*"a"+"bb"+int(dlugosc/2-1)*"a"

lista=list()
x=0
while x <=99:
    x+=1
    print("Palindromy od 0 do 99")
    print(genpal(x))
    lista.append(genpal(x))
print(lista)
print(lista[3])
print(lista[7])
print(lista[15])
print(lista[62]) #nie wiem jak wypisać z listy na raz cztery rekordy?

lista2=list()
print("Wpisz liczbę aby wygenerować palindrom (1):")
a=int(input())
print(genpal(a))
lista2.append(genpal(a))
print("Wpisz liczbę aby wygenerować palindrom (2):")
a=int(input())
print(genpal(a))
lista2.append(genpal(a))
print("Wpisz liczbę aby wygenerować palindrom (3):")
a=int(input())
print(genpal(a))
lista2.append(genpal(a))
print("Wpisz liczbę aby wygenerować palindrom (4):")
a=int(input())
print(genpal(a))
lista2.append(genpal(a))
print("Wpisz liczbę aby wygenerować palindrom (5):")
a=int(input())
print(genpal(a))
lista2.append(genpal(a))

print("lista wygenerowanych palindromów")
print(lista2)

#6
a=1
palindrom1="aaaabaaaa"
palindrom1==palindrom1[::-1]

__author__ = "Paweł Lech"