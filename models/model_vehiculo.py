'''Esta clase permite generar el modelo para los vehiculos'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
# pylint: disable=import-error
from config.db import Base

# pylint: disable=too-few-public-methods
class Vehiculo(Base):
    '''Clase para especificar tabla vehiculos'''
    __tablename__ = "tbb_vehiculos"

    Id = Column(Integer, primary_key=True, index=True)
    cliente_Id = Column(Integer, ForeignKey("tbb_clientes.Id"))
    modelo = Column(String(10))
    matricula = Column(String(10))
    color = Column(String(60))
    tipo = Column(String(250))
    puertas = Column(Integer)
    estatus = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)