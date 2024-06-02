class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.__class__.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self.__class__.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        total = sum(contract.royalties for contract in self.contracts())
        return total

from datetime import datetime

class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.members.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        contracts = [contract for contract in cls.members if contract.date == date]
        contracts.sort(key=lambda x: datetime.strptime(x.date, "%d/%m/%Y"))
        return contracts
