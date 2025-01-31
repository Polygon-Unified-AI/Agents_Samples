from pydantic import BaseModel, Field

from .question_evaluation import QuestionEvaluation


class AnswersEvaluation(BaseModel):
    answers: list[QuestionEvaluation] = Field(
        ...,
        description="List of answers evaluation",
    )
