from pydantic import BaseModel, Field

from .education_info import EducationInfo
from .experience_info import ExperienceInfo


class CvInfo(BaseModel):
    first_name: str = Field(..., description="First name of the candidate")
    last_name: str = Field(..., description="Last name of the candidate")
    email: str = Field(..., description="Email address of the candidate")
    phone_number: str = Field(..., description="Phone number of the candidate")
    birth_date: str = Field(..., description="Birth date of the candidate")
    gender: str = Field(..., description="The Gender of the candidate")
    country: str = Field(..., description="Country of residence of the candidate")
    town: str = Field(..., description="Town of residence of the candidate")
    professional_title: str = Field(
        ..., description="Professional title of the candidate"
    )
    summary: str = Field(..., description="Summary of the candidate")
    skills: list[str] = Field(..., description="List of skills of the candidate")
    # list of education information
    education: list[EducationInfo] = Field(
        ..., description="List of education information"
    )
    # list of experience information
    experience: list[ExperienceInfo] = Field(
        ..., description="List of experience information"
    )

    # linked in profile
    linkedin: str = Field(..., description="LinkedIn profile of the candidate")
    # certifications
    certifications: list[str] = Field(
        ..., description="List of certifications of the candidate"
    )
