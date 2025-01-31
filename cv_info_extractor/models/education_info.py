from pydantic import BaseModel, Field
from datetime import datetime


class EducationInfo(BaseModel):
    start_date: str = Field(
        ...,
        description="Start date of the education, Should be actual date or 'Present', no something like 'First Year'",
    )
    end_date: str = Field(
        ...,
        description="End date of the education, Should be actual date or 'Present', no something like 'First Year'",
    )
    degree: str = Field(..., description="Degree obtained during the education")
    institution: str = Field(..., description="Institution attended for the education")
    subject: str = Field(..., description="Subject studied during the education")
    is_present: bool = Field(
        ...,
        description=f"Is the candidate currently studying, note that the today's date = {datetime.now().strftime('%Y-%m-%d')}",
    )
