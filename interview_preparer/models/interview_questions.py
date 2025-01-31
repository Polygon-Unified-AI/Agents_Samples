from pydantic import BaseModel, Field

from .question import Question


class InterviewQuestions(BaseModel):
    questions: list[Question] = Field(
        ...,
        description="List of interview questions",
    )
