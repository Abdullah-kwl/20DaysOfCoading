from dataclasses import dataclass
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load from .env
class Secrets(BaseSettings):
    data_path: str

    # in .env please add DATA_PATH="data/students.json"
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

# Static config (no env)
@dataclass
class Config:
    model: str = "Gemini"
    temperature: float = 0.7
    max_tokens: int = 1000


secrets = Secrets()
config = Config()

# if __name__ == "__main__":
#     print(secrets.data_path)
#     print(config.model)