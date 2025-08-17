from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey, String, Table, Column

#Create a base class for our models
class Base(DeclarativeBase):
    pass
    #could add your own config


#Instatiate your SQLAlchemy database:
db = SQLAlchemy(model_class = Base)


loan_books = Table(
    'loan_books',
    Base.metadata,
    Column('loan_id', ForeignKey('loans.id')),
    Column('book_id', ForeignKey('books.id'))
)


class Users(Base):
    __tablename__ = 'users' #lowercase plural form of resource

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(360), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120), nullable=False)
    DOB: Mapped[date] = mapped_column(Date, nullable=True)
    address: Mapped[str] = mapped_column(String(500), nullable=True)
    role: Mapped[str] = mapped_column(String(30), nullable=False)

    #One to Many relationship from User to Books
    loans: Mapped[list['Loans']] = relationship('Loans', back_populates='user')

  
class Loans(Base):
    __tablename__ = 'loans'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    loan_date: Mapped[date] = mapped_column(Date, nullable=True)
    deadline: Mapped[date] = mapped_column(Date, nullable=True)
    return_date: Mapped[date] = mapped_column(Date, nullable=True)

    #Relationships
    user: Mapped['Users'] = relationship('Users', back_populates='loans')
    books: Mapped[list['Books']] = relationship("Books", secondary=loan_books, back_populates='loans') #Many to Many relationship going through the loan_books table
   

class Books(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    genre: Mapped[str] = mapped_column(String(360), unique=True, nullable=False)
    age_category: Mapped[str] = mapped_column(String(120), nullable=False)
    publish_date: Mapped[date] = mapped_column(Date, nullable=True)
    author: Mapped[str] = mapped_column(String(500), nullable=True)

    #Relationship
    loans: Mapped[list['Loans']] = relationship('Loans', secondary=loan_books, back_populates='books')