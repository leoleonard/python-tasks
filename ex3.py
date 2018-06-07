# Uzupełnij funkcję tak, aby zwracała słownik, którego klucze 
# są kolejnymi wartosciami z listy keys, a wartości kolejnymi elementami listy values
def map_lists(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result

# Uzupełnij funkcję tak aby zwracała słownik w którym kluczami są kody krajów
# a wartosciami marki samochodów tam produkowanych.
# Argumentem wejściowym jest lista krotek postaci (KOD_KRAJU, MARKA_SAMOCHODU)
# np. dla listy [('DE', 'Audi'), ('JP', 'Toyota'), ('IT', 'Fiat'), ('DE', 'Mercedes')]
# funkcja powinna zwrócić {'DE':['Audi', 'Mercedes'], 'IT':['Fiat'], 'JP':['Toyota']}
def map_cars_countries(cars):
    result = {}
    for country, made in cars:
        if country in result:
            result[country].append(made)
        else:
            result[country] = [made]
    return result

    # def map_cars_countries(cars):
    # result = {}
    # for country, make in cars:
    #     if country in result:
    #         if isinstance(result[country], list):
    #             result[country].append(make)
    #         else:
    #             result[country] = [result[country]]
    #             result[country].append(make)
    #     else:
    #         result[country] = make
    # return result


if __name__ == '__main__':
    keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Mapped Lists:{0}'.format(map_lists(keys, values)))
    print(20 * "-")
    cars = [('DE', 'Mercedes'), ('JP', 'Toyota'), ('JP', 'Mazda'), ('DE', 'Audi'),
            ('RO', 'Dacia'), ('IT', 'Fiat'), ('DE', 'Volkswagen'), ('FR', 'Renault'),
            ('FR', 'Citroen')]
    print('Cars mapped to countries: {0}'.format(map_cars_countries(cars)))
    print(20 * '-')
