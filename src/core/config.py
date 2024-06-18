from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn



class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000
    

class ApiPrefix(BaseModel):
    prefix: str = '/api'


class DatabaseConfig(BaseSettings):
    url: PostgresDsn
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10



class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()
    
    
settings = Settings()
