class Author:
    all=[]
    def __init__(self,name:str):
        self.name=name
        Author.all.append(self)


    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self,book, date, royalties):
        contract=Contract(self,book,date,royalties)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all=[]
    def __init__(self,title:str):
        self.title=title
        Book.all.append(self)


    def contracts(self):
        return[contract for contract in Contract.all if contract.book==self]


    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    all=[]
    def __init__(self,author,book,date,royalties):
        self.author=author
        self.book=book
        self.date=date
        self.royalties=royalties
       
        

        if not isinstance(date,str):
            raise TypeError("Date should be an string!")
        
        if not isinstance(royalties,int):
            raise TypeError("Royalties should be an integer!")
        
        if not isinstance(author,Author):
            raise TypeError("author should be an instance of the Author object!")
        
        if not isinstance(book,Book):
            raise TypeError("book should be an instance of the Book object!")
        
        Contract.all.append(self)


    @classmethod
    def contracts_by_date(cls, date):
            return [contract for contract in cls.all if contract.date==date]