from datetime import date
from dataclasses import dataclass
from typing import List
import csv

# Media super classe de Book, Cd, Dvd
# TVA 5.5% Book mais 20% pour le reste
# Facultatif : Cart possède plusieurs media, get_total_net_price


class Publisher:

    def __init__(self, name, address):
        self.name = name
        self.address = address

@dataclass()
class Author:

    first_name:str
    last_name: str
    id: int

class Media:

    vat = 0.2

    def __init__(self, title: str, id: int, price: float, publisher: Publisher, date: date = date(2022,11,8), category:int = 0, lang:str="fr-FR", authors:List[Author]=[]):
        self.title = title
        self.id = id
        self.price = price
        self.date = date
        self.category = category
        self.lang = lang
        self.publisher = publisher
        self.authors = authors

    def get_net_price(self):
        return self.price * (1 + Media.vat)

class Book(Media):

    vat = 0.055

    def __init__(self, title: str, id: int, price: float, publisher: Publisher = None, date: date = date(2022, 11, 8),
                 category: int = 0, lang: str = "fr-FR", authors: List[Author] = [], nb_page=0):
        super().__init__(title, id,price,publisher,date,category,lang,authors)
        self.nb_page = nb_page

    def get_net_price(self):
        return self.price * (1 + Book.vat)

class Cd(Media):

    def __init__(self, title: str, id: int, price: float, publisher: Publisher, date: date = date(2022, 11, 8),
                 category: int = 0, lang: str = "fr-FR", authors: List[Author] = [], nb_track=0):
        super().__init__(title, id,price,publisher,date,category,lang,authors)
        self.nb_track = nb_track

class Cart:

    def __init__(self, id:int, medias:List[Media] = []):
        self.id = id
        self.medias = medias

    def get_total_net_price(self):
        return sum([m.get_net_price() for m in self.medias])
        # sum = 0
        # for m in self.medias:
        #     sum += m.get_net_price()
        # return sum

    def add(self, m:Media):
        self.medias.append(m)

    def remove(self, m: Media):
        self.medias.remove(m)

class BookCsvParser:

    def __init__(self, path):
        self.path = path

    def parse(self) -> List[Book]:
        books = []
        with open(self.path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                id = int(row["id"])
                title = row["title"]
                price = float(row["price"])
                book = Book(title, id, price)
                books.append(book)
        return books



    def get_by_id(self, id) -> Book:
        pass

if __name__ == '__main__':
    p1 = Publisher("E2V", "St Egreve")
    a1 = Author("Cyril", "Vincent", 123)
    b1 = Book("Python",123,20, p1, date(2022, 11, 8))
    print(b1)
    print(b1.title)
    cd1 = Cd("Johnny",123,10, p1, date(2022, 11, 8), authors=[a1])
    cart = Cart(123)
    cart.add(b1)
    cart.add(cd1)
    print(cart.get_total_net_price())
    parser = BookCsvParser("data/book.csv")
    res = parser.parse()
    print(res)

