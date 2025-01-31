from pydantic import BaseModel, Field


class Question(BaseModel):
    question: str = Field(..., description="The question to be asked")
    answer: str = Field(..., description="The answer to the question")
