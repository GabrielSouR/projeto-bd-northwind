from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_version.config.conexao import Base

class Pedido(Base):
    __tablename__ = 'orders'
    __table_args__ = {'schema': 'northwind'}

    orderid = Column(Integer, primary_key=True)
    customerid = Column(String(5), nullable=False)
    employeeid = Column(Integer, nullable=False)
    orderdate = Column(DateTime)
    requireddate = Column(DateTime)
    shipname = Column(String(35))

    itens = relationship("ItemPedido", back_populates="pedido")
