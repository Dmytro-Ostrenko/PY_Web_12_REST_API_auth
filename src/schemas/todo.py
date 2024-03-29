from pydantic import BaseModel, EmailStr, Field
#import pydantic
from typing import Optional
import datetime 



class ContactSchema(BaseModel):
    first_name: str = Field(min_length=2, max_length=20)
    last_name: str = Field(min_length=2, max_length=20)
    #email: EmailStr
    email: str
    phone_number: str = Field(min_length=8, max_length=13)
    birthday: datetime.date
    additional_info: str = Field(max_length=200)





class ContactUpdateSchema(ContactSchema):
    pass


class ContactResponse(BaseModel):
    id: int = 1
    first_name: str
    last_name: str
    #email: EmailStr
    email: str
    phone_number: str
    birthday: datetime.date
    additional_info: str

    class Config:
        from_attributes = True