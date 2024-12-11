class Settings:
    DB_URL = 'postgresql+asyncpg://db:db@localhost:5432/db'
    DB_ECHO = False
    STORAGE_URL = 'images'
    SECRET_KEY_USERS = 'kjfsdklfj28972398789237592ysdhfkjsaf'


settings = Settings()