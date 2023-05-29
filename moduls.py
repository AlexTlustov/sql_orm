import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publishers'

    id = sq.Column(sq.BigInteger, primary_key=True)
    name = sq.Column(sq.String(70), unique=True)

    def __str__(self):
        return f'Автор. {self.id}: {self.name}'
                          
    pass

class Shop(Base):
    __tablename__ = 'shops'

    id = sq.Column(sq.BigInteger, primary_key=True)
    name = sq.Column(sq.String(70), unique=True)

    def __str__(self):
        return f'Магазин. {self.id}: {self.name}'
    
    pass

class Book(Base):
    __tablename__ = 'books'

    id = sq.Column(sq.BigInteger, primary_key=True)
    tittle = sq.Column(sq.String(70), unique=True)
    id_publisher = sq.Column(sq.BigInteger, sq.ForeignKey('publishers.id', ondelete='CASCADE'))

    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f'Книга. {self.id}: {self.tittle}, ID автора: {self.id_publisher}'
    
    pass

class Stock(Base):
    __tablename__ = 'stocks'

    id = sq.Column(sq.BigInteger, primary_key=True)
    id_book = sq.Column(sq.BigInteger, sq.ForeignKey('books.id', ondelete='CASCADE'))
    id_shop = sq.Column(sq.BigInteger, sq.ForeignKey('shops.id', ondelete='CASCADE'))
    count = sq.Column(sq.BigInteger)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

    def __str__(self):
        return f'Транзакция. {self.id}: ID книги: {self.id_book}, ID магазина: {self.id_shop}'
    
    pass

class Sale(Base):
    __tablename__ = 'sales'

    id = sq.Column(sq.BigInteger, primary_key=True)
    price = sq.Column(sq.BigInteger)
    date_sale = sq.Column(sq.DateTime)
    id_stock = sq.Column(sq.BigInteger, sq.ForeignKey('stocks.id', ondelete='CASCADE'))
    count = sq.Column(sq.BigInteger)

    stock = relationship(Stock, backref="sale")

    def __str__(self):
        return f'Продажа. {self.id}: ID транзакции: {self.id_stock}, Дата продажи: {self.date_sale}, Цена: {self.price}, Количество продаж: {self.count}'
    
    pass

def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)





















