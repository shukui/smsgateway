from pydantic import BaseModel

class Sms(BaseModel):
    from_num : str
    to_num :str
    msg :str