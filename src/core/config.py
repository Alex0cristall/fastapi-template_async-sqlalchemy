from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel



class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = '/api'


class DatabaseConfig(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10
    

    model_config = SettingsConfigDict(
        env_file=('src/.env.template', 'src/.env'),
        case_sensitive=False,
    )

    @property
    def GET_DATABASE_url(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'



class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()

    # model_config = SettingsConfigDict(
    #     case_sensitive=False,
    #     env_nested_delimiter='__',
    #     env_prefix='APP_CONFIG__',
    #     env_file='.env'
    # )


settings = Settings()
