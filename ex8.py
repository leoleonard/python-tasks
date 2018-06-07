# Klasa Book powinna zawierać pola:
# author - imię i nazwisko autora
# title - tytuł książki
# minumum_age - minimalny wiek czytelnika, domyślnie 18
# Klasa powinna zawierać metody:
# is_for_children - metoda powinna zwrócić True jeśli minimalny wiek czytalnieka jest mniejszy niż 18

class Book:
    def __init__(self, title, author, minimum_age=18):
        self.title = title
        self.author = author
        self.minimum_age = minimum_age

    def is_for_children(self):
        return self.minimum_age < 18

    def __repr__(self):
        return self.title

# Klasa powinna zawierać pola:
# owner_name - imię i nazwisko posiadacza
# book_list - lista książek wypożyczonych przez posiadacza
# limit - maksymalna ilość wypożyczonych książek, domyślnie 3
# Klasa powinna zawierać metody:
# borrow_book - "Wypożycz książkę", dodaje książkę do listy wypożyczonych
# metoda powinna sprawdzać, czy nie został przekroczony limit wypożyczonych pozycji i wyświetlić odpowiedni komunikat
class LibraryCard:
    def __init__(self, owner_name, limit=3):
        self.owner_name = owner_name
        self.limit = limit
        self.book_list = []

    def borrow_book(self, book):
        if self.limit > len(self.book_list):
            self.book_list.append(book)
        else:
            print('Przekroczono maksymalną ilość wypożyczonych książek')


# Klasa powinna dziedziczyć po LibraryCard
# Klasa oprócz pól z klasy LibraryCard powinna dodawać pole:
# parent_name - imię i nazwisko rodzica
# Klasa powinna przeciążyć metodę borrow_book i w przypadku kiedy książka nie jest przeznaczona dla 
# dzieci wypisać odpowiedni komunikat
class ChildLibraryCard(LibraryCard):
    def __init__(self, owner_name, parent_name, limit=3):
        super().__init__(owner_name, limit)
        self.parent_name = parent_name

    def borrow_book(self, book):
        if not book.is_for_children():
            print('To nie jest książka dla dzieci')
            return
        if self.limit > len(self.book_list):
            self.book_list.append(book)
        else:
            print('Przekroczono maksymalną ilość wypożyczonych książek')


# Klasa powinna dziedziczyć po LibraryCard
# Klasa powinna ustawiać w konstruktorze limit na wartość None
# Klasa powinna przeciążyć metodę borrow_book tak, aby nie uwzględniała limitu
class UnlimitedLibraryCard(LibraryCard):
    def borrow_book(self, book):
        self.book_list.append(book)


if __name__ == '__main__':
    sierotka_marysia = Book('O krasnoludkach i o sierotce Marysi', 'Maria Konopnicka', minimum_age=5)
    pan_tadeusz = Book('Pan Tadeusz, czyli Ostatni zajazd na Litwie', 'Adam Mickiewicz', minimum_age=15)
    w_pustyni = Book('W pustyni i w puszczy', 'Henryk Sienkiewicz', minimum_age=12)
    fifty_shades = Book('Fifty Shades of Grey', 'E.L. James', minimum_age=18)
    card1 = LibraryCard('Jan Kowalski')
    card1.borrow_book(w_pustyni)
    print(card1.book_list)
    print(20 * "-")
    card2 = LibraryCard('John Doe', limit=1)
    card2.borrow_book(pan_tadeusz)
    card2.borrow_book(w_pustyni)
    print(card2.book_list)
    print(20 * "-")
    child_card1 = ChildLibraryCard('Tomasz Nowak', 'Anna Nowak')
    child_card1.borrow_book(sierotka_marysia)
    child_card1.borrow_book(fifty_shades)
    print(child_card1.book_list)
    print(20 * "-")
    unlimited_card = UnlimitedLibraryCard('Jane Doe')
    for i in range(20):
        unlimited_card.borrow_book(pan_tadeusz)
    print(unlimited_card.book_list)
    print(20 * "-")
