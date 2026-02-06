''' Esta clase permite generar el modelo para los tipos de rol'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    __tablename__ = "tbc_usuarios"
    Id = Column(Integer, primary_key=True, index=True)
    Rol_id = Column(Integer, foreignKey("tbc_roles.id"))
    