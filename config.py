from pydantic_settings import BaseSettings



class Setting(BaseSettings):
    app_name: str ="FastAPI Example"
    debug:bool = True
    database_url: str = "sqlite:///exp.db"

    class Config:
        env_file = '.env'
        

setting = Setting()