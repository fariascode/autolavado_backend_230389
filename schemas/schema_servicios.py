'''
Schemas for servicios (tbc_servicios)
'''
from datetime import datetime
from pydantic import BaseModel


class ServicioBase(BaseModel):
    '''Campos base de la tabla Servicios'''
    nombre: str
    descripcion: str
    costo: float
    duracion: int
    estado: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime


# pylint: disable=too-few-public-methods, unnecessary-pass
class ServicioCreate(ServicioBase):
    '''Schema para crear un Servicio'''
    pass


class ServicioUpdate(ServicioBase):
    '''Schema para actualizar un Servicio'''
    pass


class Servicio(ServicioBase):
    '''Schema para operaciones por ID en tabla Servicios'''
    Id: int

    class Config:
        orm_mode = True
