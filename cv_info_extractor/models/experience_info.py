from pydantic import BaseModel, Field
from datetime import datetime


class ExperienceInfo(BaseModel):
    start_date: str = Field(
        ...,
        description="Start date of the experience, Should be actual date or 'Present', no something like 'First Year'",
    )
    end_date: str = Field(
        ...,
        description="End date of the experience, Should be actual date or 'Present', no something like 'First Year'",
    )
    job_title: str = Field(..., description="Job title of the experience")
    company: str = Field(..., description="Company worked for during the experience")
    location: str = Field(..., description="Location of the company")
    description: str = Field(..., description="Description of the experience")
    employment_type: str = Field(..., description="Employment type of the experience")
    is_present: bool = Field(
        ...,
        description=f"Is the candidate currently working, note that the today's date = {datetime.now().strftime('%Y-%m-%d')}",
    )
