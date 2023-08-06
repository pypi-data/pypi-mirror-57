import os
from typing import Optional

from dotenv import load_dotenv


class Settings(object):
    def __init__(self):
        load_dotenv()

    def get(self, key: str) -> Optional[str]:
        return os.getenv(key)
