from pydantic import BaseModel, SecretStr



class UserDTO(BaseModel):
    username: str
    password: str
    

class UserCreate(UserDTO):
    pass
    

class UserRead(UserDTO):
    id: int
