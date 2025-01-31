from pydantic import BaseModel, Field


class QuestionAndAnswer(BaseModel):
    question: str = Field(..., description="The question asked")
    optimal_answer: str = Field(..., description="The optimal answer")
    answer: str = Field(..., description="The answer given by the candidate")
