'''
Schemas for roles (tbc_roles)
'''
from datetime import datetime
from pydantic import BaseModel


class RolBase(BaseModel):
    '''Campos base de la tabla Rol'''
    nombreRol: str
    estado: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime


# pylint: disable=too-few-public-methods, unnecessary-pass
class RolCreate(RolBase):
    '''Schema para crear un Rol'''
    pass


class RolUpdate(RolBase):
    '''Schema para actualizar un Rol'''
    pass


class Rol(RolBase):
    '''Schema para operaciones por ID en tabla Rol'''
    id: int

    class Config:
        orm_mode = True
