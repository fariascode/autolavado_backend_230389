'''
Schemas for vehiculos_servicios_usuarios (tbd_vehiculos_servicios_usuarios)
'''
from datetime import datetime, date, time
from enum import Enum
from pydantic import BaseModel


class Estatus(str, Enum):
    Programado = "Programado"
    Proceso = "En proceso"
    Realizado = "Realizado"


class VehiculoServicioBase(BaseModel):
    '''Campos base de la tabla VehiculoServicio'''
    vehiculo_Id: int
    cajero_Id: int
    operador_Id: int
    servicio_Id: int
    fecha: date
    hora: time
    estatus: Estatus
    estado: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime


# pylint: disable=too-few-public-methods, unnecessary-pass
class VehiculoServicioCreate(VehiculoServicioBase):
    '''Schema para crear un VehiculoServicio'''
    pass


class VehiculoServicioUpdate(VehiculoServicioBase):
    '''Schema para actualizar un VehiculoServicio'''
    pass


class VehiculoServicio(VehiculoServicioBase):
    '''Schema para operaciones por ID en tabla VehiculoServicio'''
    Id: int

    class Config:
        orm_mode = True
