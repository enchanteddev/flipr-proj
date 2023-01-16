from sqlalchemy import Table, Column, Integer, String, MetaData, Date, create_engine, Float, select
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import csv
from pathlib import Path

import datetime

NOW = datetime.date(2023, 1, 12)

metadata_obj = MetaData()

engine = create_engine("sqlite+pysqlite:///db.sqlite3", echo=True, connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Stock(Base):
    __tablename__ = 'DB'

    date = Column(Date, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    adjclose = Column(Float)
    volume = Column(Float)
    stockname = Column(String, primary_key=True)

def to_float(n):
    if n == 'null':
        return 0
    return float(n)

def add_data():
    for csvfile in Path('data').iterdir():
        with open(csvfile) as f:
            csvreader = csv.reader(f)
            fields = next(csvreader)
            session.add_all([Stock(date=datetime.date(*map(int, row[0].split('-'))), 
                            open=to_float(row[1]), high=to_float(row[2]), low=to_float(row[3]), close=to_float(row[4]), 
                            adjclose=to_float(row[5]), volume=to_float(row[6]), stockname=csvfile.name.split('.')[0])
                            for row in csvreader])
    session.commit()


def data_init():
    Base.metadata.create_all(engine)

    
def main2():
    data_init()
    add_data()

def get_data(stockname: str, days: int = 52*3*7):
    a = select(func.max(Stock.close)).where(Stock.stockname == stockname).filter(Stock.date.between(NOW - datetime.timedelta(days=days), NOW))
    sea = session.execute(a)
    for row in sea:
        stock: Stock = row['Stock']
        yield {
            'date': datetime.date(stock.date.year, stock.date.month, stock.date.day),
            'open': float(stock.open),
            'high': float(stock.high),
            'low': float(stock.low),
            'close': float(stock.close),
            'adjclose': float(stock.adjclose),
            'volume': float(stock.volume),
            'stockname': str(stock.stockname)
        }

def get_close_data(stockname: str, days: int = 52*3*7):
    a = select(Stock).where(Stock.stockname == stockname).filter(Stock.date.between(NOW - datetime.timedelta(days=days), NOW))
    sea = session.execute(a)
    for row in sea:
        stock: Stock = row['Stock']
        yield {
            'date': datetime.date(stock.date.year, stock.date.month, stock.date.day),
            'close': float(stock.close)
        }


def get_stock_min_max(stockname: str, days: int = 0):
    a = select(func.max(Stock.high), func.min(Stock.low)).where(Stock.stockname == stockname).filter(Stock.date.between(NOW - datetime.timedelta(days=days), NOW))
    sea = session.execute(a)
    for row in sea:
        return {
            'max': row[0],
            'min': row[1],
        }

def get_stock_open_close(stockname: str, date: int = 0):
    a = select(Stock.open, Stock.close).where(Stock.stockname == stockname, Stock.date == NOW - datetime.timedelta(days = date))
    sea = session.execute(a)
    for row in sea:
        return {
            'open': row[0],
            'close': row[1],
        }

def main():
    for row in get_data('TATASTEEL', 12):
        print(row)

if __name__ == '__main__':
    #main()
    #print(get_stock_min_max('TATASTEEL', days = 7*52))
    print(get_stock_open_close('TATASTEEL', date = 1))