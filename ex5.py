import string
PICTURES = ['scrambled_pic1.jpg', 'scrambled_pic2.jpg', 'scrambled_pic3.jpg']
TEXT_FILE = 'text_sample.txt' 

# Uzupełnij funkcję word_stats w taki sposób, aby zwracała
# ilość wystąpień słów z listy words w pliku o nazwie przekazanej 
# w parametrze filename
# Wynikiem powinien być słownik o nas†epującej strukturze:
# {'słowo1': ilość wystąpień, 'słowo2': ilość_wystąpień}
def word_stats(filename, words):
    """
    Args:
        filename: nazwa pliku
        words: lista słów do wyszukiwania
    Returns:
        dict
    """
    stats = {}
    for word in words:
        stats[word] = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line_words = line.split(' ')
            for line_word in line_words:
                if len(line_word) == 0:
                    continue
                if line_word[-1] in string.punctuation:
                    line_word = line_word[:-1]
                line_word = line_word.strip()
                if line_word in stats:
                    stats[line_word] += 1
    return stats


# 1) Uzupełnij funkcję word_stats_all w taki sposób, aby zwracała
# ilość wystąpień słów w pliku o nazwie przekazanej 
# w parametrze filename
# Wynikiem powinien być słownik o nas†epującej strukturze:
# {'słowo1': ilość wystąpień, 'słowo2': ilość_wystąpień}
#
# 2) Po wykonaniu punktu 1) zmień funkcję tak, aby porównywała słowa niezależnie
# od wielkości liter. Funkcja powinna też zadbać o usunięcie znaków przestankowych z
# końcówek wyrazów.
def word_stats_all(filename):
    """
    Args:
        filename: nazwa pliku
    Returns:
        dict: statystyki wyrazów
    """
    stats = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line_words = line.split(' ')
            for line_word in line_words:
                if len(line_word) == 0:
                    continue
                if line_word[-1] in string.punctuation:
                    line_word = line_word[:-1]
                line_word = line_word.strip()
                line_word = line_word.lower()
                if line_word in stats:
                    stats[line_word] += 1
                else:
                    stats[line_word] = 1
    return stats


# Uzupełnij funkcję unscramble tak, aby zmieniła strukturę plików
# binarnych z listy filenames wg. następującego algorytmu:
# 1. Odczytać 100 bajtów pliku.
# 2. Jeśli udało się odczytać 100 bajtów to do pliku wyjściowego zapisujemy 
#   najpierw ostatnie 50 bajtów z odczytanego bufora, następnie pierwsze 50 bajtów.
# 3. Jeśli odczytaliśmy mniej niż 100 bajtów (nie ma więcej danych w pliku) to
#   zapisujemy do pliku wyjściowego odczytane dane bez zmian.
# punkty 1-3 należy powtórzyć dla całego pliku.
# 
# Funkcja nie powinna zwracać żadnej wartości, ale powinna tworzyć plik wyjściowy, 
# dla każdego pliku wejściowego. Nazwa pliku wyjściowego powinna być taka sama jak wejściowego
# z usuniętym prefiksem "scrambled_"
#
# Pliki wyjściowe powinny być obrazami w formacie JPG. Na którym z nich znajduje się zwierzę?
def unscramble(filenames):
    for pic in filenames:
        with open(pic, 'rb') as in_file:
            out_filename = pic.split('_')[1]
            with open(out_filename, 'wb') as out_file:
                bytes_read = in_file.read(100)
                while len(bytes_read) > 0:
                    if len(bytes_read) == 100:
                        out_file.write(bytes_read[50:])
                        out_file.write(bytes_read[:50])
                    else:
                        out_file.write(bytes_read)
                    bytes_read = in_file.read(100)

if __name__ == '__main__':
    print('Statystyki dla wyrazów "the" i "whose"')
    print(word_stats(TEXT_FILE, ['the', 'whose']))
    print('=' * 20)
    print('Statystyki wystąpień dla wszystkich słów')
    print(word_stats_all(TEXT_FILE))
    print('=' * 20)
    print('Zmiana struktury plików...')
    unscramble(PICTURES)
    print('=' * 20)
