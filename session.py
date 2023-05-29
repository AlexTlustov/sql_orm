import json
import flask_sqlalchemy
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from moduls import create_tables, Publisher, Book, Sale, Stock, Shop

DSN = "postgresql://postgres:7753191qq@localhost:5432/dataclients"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()

    # Заполнение таблиц тестовыми данным из JSON
    with open('fixtures/tests_data.json', 'r', encoding='utf-8') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

    # Запросы к SQL базе
    for i in session.query(Book.tittle, Shop.name, Sale.price, Sale.date_sale)\
        .join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == 'Пушкин').all():
        name_book, name_shop, i_price, i_data = i
        print(f'{name_book} | {name_shop} | {i_price} | {i_data}')

    session.close()
