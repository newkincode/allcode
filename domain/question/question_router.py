from fastapi import APIRouter

from database import SessionLocal
from models import Question

from database import get_db

router = APIRouter(
    prefix="/api/question",
)


@router.get("/list")
def question_list():
    with get_db() as db:
        _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list