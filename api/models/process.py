from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Table,
    Text,
)
from sqlalchemy.orm import relationship

from .meta import Base

association_table = Table('company_process', Base.metadata,
                          Column('company_id', Integer, ForeignKey('company.id')),
                          Column('process_id', Integer, ForeignKey('process.id')))

class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

class Process(Base):
    __tablename__ = 'process'
    id = Column(Integer, primary_key=True)
    status = Column(Text)
    company = relationship('Company', secondary=association_table)
