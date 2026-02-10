from sqlalchemy.orm import Session

from models.model_vehiculo import Vehiculo
import schemas.schema_vehiculo as schema_vehiculo


def get_vehiculos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vehiculo).offset(skip).limit(limit).all()


def get_vehiculo(db: Session, vehiculo_id: int):
    return db.query(Vehiculo).filter(Vehiculo.Id == vehiculo_id).first()


def create_vehiculo(db: Session, vehiculo: schema_vehiculo.VehiculoCreate):
    db_vehiculo = Vehiculo(**vehiculo.dict())
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo


def update_vehiculo(db: Session, vehiculo_id: int, vehiculo: schema_vehiculo.VehiculoUpdate):
    db_vehiculo = get_vehiculo(db, vehiculo_id)
    if not db_vehiculo:
        return None
    for key, value in vehiculo.dict(exclude_unset=True).items():
        setattr(db_vehiculo, key, value)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo


def delete_vehiculo(db: Session, vehiculo_id: int):
    db_vehiculo = get_vehiculo(db, vehiculo_id)
    if not db_vehiculo:
        return None
    db.delete(db_vehiculo)
    db.commit()
    return db_vehiculo
