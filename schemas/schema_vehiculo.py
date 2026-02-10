'''
Schemas for vehiculos (tbb_vehiculos)
'''
from datetime import datetime
from pydantic import BaseModel


class VehiculoBase(BaseModel):
    '''Campos base de la tabla Vehiculo'''
    cliente_Id: int
    modelo: str
    matricula: str
    color: str
    tipo: str
    puertas: int
    estatus: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime


# pylint: disable=too-few-public-methods, unnecessary-pass
class VehiculoCreate(VehiculoBase):
    '''Schema para crear un Vehiculo'''
    pass


class VehiculoUpdate(VehiculoBase):
    '''Schema para actualizar un Vehiculo'''
    pass


class Vehiculo(VehiculoBase):
    '''Schema para operaciones por ID en tabla Vehiculo'''
    Id: int

    class Config:
        orm_mode = True
