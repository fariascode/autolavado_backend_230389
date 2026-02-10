'''
Schemas for usuarios (tbc_usuarios)
'''
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class UsuarioBase(BaseModel):
    '''Campos base de la tabla Usuario'''
    rol_id: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    direccion: str
    correo_electronico: str
    numero_telefono: str
    contrasena: str
    estatus: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime


# pylint: disable=too-few-public-methods, unnecessary-pass
class UsuarioCreate(UsuarioBase):
    '''Schema para crear un Usuario'''
    pass


class UsuarioUpdate(UsuarioBase):
    '''Schema para actualizar un Usuario'''
    pass


class Usuario(UsuarioBase):
    '''Schema para operaciones por ID en tabla Usuario'''
    Id: int

    class Config:
        orm_mode = True

class UsuarioLogin(BaseModel):
    '''Schema para login de Usuario'''
    numero_telefono: Optional[str] = None
    correo_electronico: Optional[str] = None
    contrasena: str
    
