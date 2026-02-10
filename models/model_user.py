''' Esta clase permite generar el modelo para los tipos de rol'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    __tablename__ = "tbc_usuarios"
    Id = Column(Integer, primary_key=True, index=True)
    rol_id = Column(Integer, ForeignKey("tbc_roles.id"))
    nombre = Column(String(60))
    primer_apellido = Column(String(60))
    segundo_apellido = Column(String(60))
    direccion = Column(String(200))
    correo_electronico = Column(String(100))
    numero_telefono = Column(String(20))
    contrasena = Column(String(40))
    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)