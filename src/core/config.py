from pydantic_settings import BaseSettings
from pydantic import BaseModel



class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000
    

class ApiPrefix(BaseModel):
    prefix: str = '/api'

    
class DataBase(BaseModel):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    
    
settings = Settings()
