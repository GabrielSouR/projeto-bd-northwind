from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_version.config.conexao import Base

class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'northwind'}

    employeeid = Column(Integer, primary_key=True)
    lastname = Column(String(10))
    firstname = Column(String(10))
    title = Column(String(25))
    titleofcourtesy = Column(String(5))
    birthdate = Column(DateTime)
    hiredate = Column(DateTime)
    address = Column(String(50))
    city = Column(String(20))
    region = Column(String(2))
    postalcode = Column(String(9))
    country = Column(String(15))
    homephone = Column(String(14))
    extension = Column(String(4))
    reportsto = Column(Integer)
    notes = Column(String)

    pedidos = relationship("Pedido", back_populates="funcionario")
