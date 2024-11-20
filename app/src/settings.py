class Settings:
    DB_URL = 'postgresql+asyncpg://db:db@localhost:5432/db'
    DB_ECHO = True
    STORAGE_URL = '../app/images'


settings = Settings()