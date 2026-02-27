from pydantic_settings import BaseSettings



class Setting(BaseSettings):
    app_name: str ="FastAPI Example"
    debug:bool = True
    database_url: str = "sqlite:///exp.db"
    
    secret_key: str = "your-secret-key-here-change-in-production"
    algorithm:str = "HS256"
    access_token_expire_minutes:int = 30 



    class Config:
        env_file = '.env'
        

setting = Setting()