import os
import dotenv

from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

dotenv.load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


class DB(BaseModel):
    url: str = os.getenv("PSQL_URL")


class JWT(BaseModel):
    algorithm: str = "RS256"
    private_key: str = Path(
        BASE_DIR / "src" / "users" / "certs" / "private.pem"
    ).read_text()
    public_key: str = Path(
        BASE_DIR / "src" / "users" / "certs" / "public.pem"
    ).read_text()
    access_token_minutes_expire: int = 15
    refresh_token_days_expire: int = 30


class Settings(BaseSettings):
    db: DB = DB()
    jwt: JWT = JWT()
