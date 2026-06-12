from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from pydantic import BaseModel

from app.database import engine, get_db, Base
from app.models import Student


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="DevOps Student API", version="1.0.0", lifespan=lifespan)


class StudentCreate(BaseModel):
    reg_no: str
    name: str
    course: str | None = None


class StudentResponse(BaseModel):
    id: int
    reg_no: str
    name: str
    course: str | None = None

    class Config:
        from_attributes = True


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    """Health check — verifies DB connection is alive."""
    try:
        db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception:
        db_status = "disconnected"
    return {"status": "ok", "db": db_status, "student": "2312102"}


@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """Create a new student record."""
    db_student = Student(
        reg_no=student.reg_no,
        name=student.name,
        course=student.course,
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    """Return all student records."""
    return db.query(Student).all()


@app.get("/students/{reg_no}", response_model=StudentResponse)
def get_student(reg_no: str, db: Session = Depends(get_db)):
    """Return a single student by registration number."""
    student = db.query(Student).filter(Student.reg_no == reg_no).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
