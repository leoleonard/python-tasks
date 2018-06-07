import string
words = ['Początek', 'traktatu', 'czasu', 'być', 'wstrzemięźliwym', 'Tak',
         'może', 'być', 'uważana', 'jako', 'najwyższy', 'stopień', 'moralności',
         'z', 'części', 'Ale', 'się', 'od', 'Stworzyciela', 'niebył',
         'nadany', 'Jakże', 'to', 'mogło', 'być', 'moralna', 'a', 'jednak',
         'złą', 'sprawę', 'będzie', 'znowu', 'się', 'uczynkiem', 'ale', 'każdy',
         'będzie', 'znowu', 'się', 'łaskawego', 'przyjęcia', 'żegnam', 'się',
         'on', 'nieraz', 'zgryzot', 'sumienia', 'które', 'przybieramy', 'z',
         'czystego', 'serca', 'lub', 'obowiąski', 'które', 'człowiek', 'jako',
         'najwyższy', 'stopień', 'przyjaźni', 'świadczyć', 'lecz', 'tylko',
         'robakiem', 'tedy', 'jej', 'człowiek', 'w', 'Królewcu', 'szanowny',
         'Imanuel', 'Kant', 'Professor', 'filozofii', 'który', 'się', 'musiał',
         'od', 'Stworzyciela', 'niebył', 'nadany']


# 1) Uzupełnij ciało funkcji longest_word tak, aby zwracało najdłuższe słowo
# z listy words
# 2) Zamień wszystkie litery słowa na wielkie
def longest_word(words):
    longest_word = None
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    word.upper()
    return longest_word


# Funkcja append_underscores powinna zwrócić listę zawierającą wszystkie słowa
# z listy words, taką że każde słowo ma taką samą długość równą długości 
# najdłuższego słowa z listy words. Jeśli słowo z listy words jest krótsze 
# od najdłuższego to powinno zostać uzupełnione odpowiednią ilością znaków '_' na końcu.
# Przykład:
# words = ['Ala', 'ma', 'kota']
# out_list = ['Ala_', 'ma__', 'kota']
def append_underscores(words):
    out_list = []
    longest_word = None
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    for word in words:
        if len(word) < max_length:
            suffix = '_' * (max_length - len(word))
            out_list.append(word + suffix)
        else:
            out_list.append(word)
    return out_list

# Funkcja powinna działać podobnie do funkcji append_underscores
# Z tą różnicą, że znaki '_' powinny być równomiernie rozłożone przed i za słowem.
# Jeśli wymagane jest dodanie nieparzystej liczby znaków '_' to większa ich ilość
# powinna znajdować się za słowem.
# Przykład:
# words = ['Ala', 'ma', 'kota']
# out_list = ['Ala_', '_ma_', 'kota']
def add_underscores(words):
    out_list = []
    longest_word = None
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    for word in words:
        if len(word) < max_length:
            underscores_num = max_length - len(word)
            if underscores_num % 2 == 0:
                underscores = '_' * int((underscores_num / 2))
                out_list.append(underscores + word + underscores)
            else:
                prefix = '_' * int(((underscores_num - 1) / 2))
                suffix = prefix + '_'
                out_list.append(prefix + word + suffix)
        else:
            out_list.append(word)
    return out_list

if __name__ == '__main__':
    print(longest_word(words))
    print('=' * 20)
    print(append_underscores(words))
    print('=' * 20)
    print(add_underscores(words))
