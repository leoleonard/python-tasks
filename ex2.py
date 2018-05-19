# Uzupełnij funkcję remove_duplicates w taki sposób, aby zwracała nową listę
# nie zawierającą zduplikowanych wartości
def remove_duplicates(list_):
    out = []
    for value in list_:
        if value not in out:
            out.append(value)
    return out


# Uzupełnij funkcję double_values w następujący sposób
# Jeśli element w wejściowej liście jest mniejszy lub równy 10 to powinien pozostać niezmieniony
# Jeśli element w liście wejściowej jest większy niż 10 to powinien zostać zamieniony na element
# dwa razy większy
# Funkcja nie powinna zwracać wartości, powinna modyfikować przekazaną listę.
# Przykład:
# PRZED: in_list = [1, 4, 5, 17, 9, 10]
# PO: in_list = [1, 4, 5, 34, 9, 10]
def double_values(in_list):
        for i, item in enumerate(in_list):
            if item > 10:
                in_list[i] = 2 * item

# Uzupełnij funkcję divisible_3_5_15 tak, aby z tworzyła nową listę na podstawie listy wejściowej.
# W liście wyjściowej powinny znaleźć się tylko te elementy z listy wejściowej, które są
# podzielne bez reszty przez 3, 5 lub 15
def divisible_3_5_15(in_list):
    out_list = []
    for item in in_list:
        if item % 3 == 0 or item % 5 == 0:
            out_list.append(item)
    return out_list


if __name__ == '__main__':
    print("remove_duplicates")
    in_list1 = [1, 3, 5, 7, 1, 4, 9, 10, 67, 20, 10, 5]
    print("Lista wejściowa: {0}".format(in_list1))
    print("Lista wyjściowa: {0}".format(remove_duplicates(in_list1)))
    print("=" * 20)
    print("double_values")
    in_list2 = [1, 4, 5, 17, 9, 10, 99, 1, 4, 99, 11, 7]
    print("Lista wejściowa: {0}".format(in_list2))
    double_values(in_list2)
    print("Lista po działaniu funkcji double_values: {0}".format(in_list2))
    print("=" * 20)
    print("divisible_3_5_15")
    in_list3 = [1, 2, 3, 4, 5, 10, 9, 7, 30, 15, 44, 21, 33, 55, 1005, 225]
    print("Lista wejściowa: {0}".format(in_list3))
    print("Lista wyjściowa: {0}".format(divisible_3_5_15(in_list3)))
    print("=" * 20)
