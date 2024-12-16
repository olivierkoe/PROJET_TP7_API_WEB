from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from services.departements_services import (
    get_all,
    get_by_id,
    create_departement,
    delete_departement,
    update_departement,
)
from schemas.departement import DepartementCreate, Departement  # Correction des imports

router_departement = APIRouter()

@router_departement.get("/", status_code=status.HTTP_200_OK, response_model=list[Departement], tags=["Départements"])
def get_departements(db: Session = Depends(get_db)):
    try:
        departements = get_all(db)
        return departements
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router_departement.get("/{code_dept}", status_code=status.HTTP_200_OK, response_model=Departement, tags=["Départements"])
def get_departement(code_dept: str, db: Session = Depends(get_db)):
    try:
        departement = get_by_id(db, code_dept)
        if not departement:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Département non trouvé")
        return departement
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router_departement.post("/", status_code=status.HTTP_201_CREATED, response_model=Departement, tags=["Départements"])
def add_departement(departement_data: DepartementCreate, db: Session = Depends(get_db)):
    try:
        return create_departement(db, departement_data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router_departement.put("/{code_dept}", status_code=status.HTTP_200_OK, response_model=Departement, tags=["Départements"])
def modify_departement(code_dept: str, updated_data: DepartementCreate, db: Session = Depends(get_db)):
    try:
        return update_departement(db, code_dept, updated_data.dict())
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router_departement.delete("/{code_dept}", status_code=status.HTTP_204_NO_CONTENT, tags=["Départements"])
def remove_departement(code_dept: str, db: Session = Depends(get_db)):
    try:
        delete_departement(db, code_dept)
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
