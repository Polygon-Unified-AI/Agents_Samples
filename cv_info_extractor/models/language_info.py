from pydantic import BaseModel, Field


class LanguageInfo(BaseModel):
    language: str = Field(..., description="Language spoken by the candidate")
    proficiency: str = Field(..., description="Proficiency level of the language")
