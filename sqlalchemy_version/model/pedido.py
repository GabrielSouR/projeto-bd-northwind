from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_version.config.conexao import Base

class Pedido(Base):
    __tablename__ = 'orders'
    __table_args__ = {'schema': 'northwind'}

    orderid = Column(Integer, primary_key=True)
    customerid = Column(String(5), nullable=False)
    employeeid = Column(Integer, ForeignKey('northwind.employees.employeeid'), nullable=False)
    orderdate = Column(DateTime)
    requireddate = Column(DateTime)
    shipname = Column(String(35))

    funcionario = relationship("Employee", back_populates="pedidos")
    itens = relationship("ItemPedido", back_populates="pedido")
