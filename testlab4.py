def citire_lista():
    l = []
    given_string = input("Dati lista, cu elementele separate prin virgula:")
    numbers_as_string = given_string.split(",")
    for x in numbers_as_string:
        l.append(int(x))
    return l

def print_menu():
    print("1. Citire lista")
    print("2. Afișarea numărului obținut prin concatenarea tuturor numerelor pozitive din listă")
    print("3. Să se afișeze suma dintre cel mai mare număr din listă și cel mai mic număr din listă")
    print("4. Afișarea tuturor numerelor care au suma cifrelor mai mare sau egală decat un număr n citit de"
"la tastatură.")

def concatenare_lista(l):
    '''
    concateneaza valorile pozitive din lista
    :param l: lista de nr. intregi
    :return: rezultatul concatenarii nr. pozitive din lista
    '''
    for x in l:
        new_x = x
        new_x = int(new_x)
        if new_x > 0:
            x = str(x)
            x = x + x
    return x

def test_concatenare_lista():
    assert concatenare_lista([7,8]) == "78"
    assert concatenare_lista([1,2,3]) == "123"
    assert concatenare_lista([-1,2,3]) == "23"

def cel_mai_mic_nr(l):
    '''
    determina cel mai mic nr. dintr-o lista
    :param l: lista de nr. intregi
    :return: cel mai mic nr. din lista
    '''
    min = l[0]
    for x in l:
        if x < min:
            min = x
    return min

def test_cel_mai_mic_nr():
    assert cel_mai_mic_nr([4,3,2]) == 2
    assert cel_mai_mic_nr([7,9,0]) == 0
    assert cel_mai_mic_nr([8,3,1]) == 1

def cel_mai_mare_nr(l):
    '''
    determina cel mai mare nr. din lista
    :param l: lista de nr. intregi
    :return: cel mai mare nr. din lista
    '''
    max = l[0]
    for x in l:
        if x > max:
            max = x
    return max

def test_cel_mai_mare_nr():
    assert cel_mai_mare_nr([8,9,10]) == 10
    assert cel_mai_mare_nr([9,10,45]) == 45
    assert cel_mai_mare_nr([81,23,3]) == 81

def suma_cel_mai_mare_si_cel_mai_mic(l):
    '''
    determina suma dintre cel mai mare si cel mai mic nr. din lista data
    :param l: lista de nr. intregi
    :return: suma dintre cel mai mic si cel mai mare nr. din lista
    '''
    S = cel_mai_mic_nr(l) + cel_mai_mare_nr(l)
    return S

def suma_cifrelor_mai_mare(l,n):
    '''
    determina numerele dintr-o lista care au suma cifrelor mai mare sau egala decat un nr. dat
    :param l: lista nr. intregi
    :param n: nr. intreg
    :return: determina numerele dintr-o lista care au suma cifrelor mai mare sau egala decat un nr. dat
    '''
    rezultat = []
    for x in l:
        y = x
        S = 0
        if x != 0:
            c = x % 10
            S = S + c
            x = x//10
            if (S >= n):
                rezultat.append(y)
    return rezultat

def test_suma_cifrelor_mai_mare():
    assert suma_cifrelor_mai_mare([10,20,30], 2) == [20,30]
    assert suma_cifrelor_mai_mare([33,44,55], 7) == [44,55]
    assert suma_cifrelor_mai_mare([12,13,14], 6) == []

def main():
    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea:")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(concatenare_lista(l))
        elif optiune == "3":
            print(suma_cel_mai_mare_si_cel_mai_mic(l))
        elif optiune == "4":
            n = int(input("Introduceti n"))
            print(suma_cifrelor_mai_mare(l,n))
        else:
            break
main()