from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_version.config.conexao import Base

class ItemPedido(Base):
    __tablename__ = 'order_details'
    __table_args__ = {'schema': 'northwind'}

    orderid = Column(Integer, ForeignKey('northwind.orders.orderid'), primary_key=True)
    productid = Column(Integer, primary_key=True)
    unitprice = Column(Numeric)
    quantity = Column(Integer)
    discount = Column(Numeric)

    pedido = relationship("Pedido", back_populates="itens")
