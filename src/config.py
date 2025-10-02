from pydantic_settings import BaseSettings, SettingsConfigDict

TEMPLATES_PATH: str = '../jinja2/templates'

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    
    SCHEME: str
    SERVER_HOST: str
    SERVER_PORT: str
    
    TEMPLATES_PATH: str
    
    @property
    def DATABASE_URL_pymysql(self) -> str:
        # "mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4"
        return f'mysql+pymysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?charset=utf8mb4'        
    
    @property
    def DATABASE_URL_sqlite() -> str:
        return 'sqlite:///test.db'
    
    model_config = SettingsConfigDict(env_file=".env")
    
    @property
    def TEMPLATES_PATH(self) -> str:
        return self.TEMPLATES_PATH
    

settings = Settings()
