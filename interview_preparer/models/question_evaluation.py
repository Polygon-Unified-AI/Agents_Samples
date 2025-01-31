from pydantic import BaseModel, Field


class QuestionEvaluation(BaseModel):
    questionNumber: int = Field(..., description="The question number")
    score: float = Field(
        ..., description="The score of the answer given by the candidate (0-5)"
    )
    evaluation: str = Field(
        ..., description="The evaluation of the answer given by the candidate"
    )
