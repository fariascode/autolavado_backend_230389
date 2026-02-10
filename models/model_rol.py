''' Esta clase permite generar el modelo para los tipos de rol'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class Rol(Base):
    __tablename__ = "tbc_roles"
    id = Column(Integer, primary_key=True, index=True)
    nombreRol = Column(String(20))
    estado = Column(Boolean, default=True)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
    