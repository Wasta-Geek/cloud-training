import os
from dotenv import load_dotenv

load_dotenv()


def get_environment_variable(key: str) -> str:
    """

    :rtype: object
    """
    env_var = os.getenv(key)
    if not env_var:
        raise ValueError("Key: '{}' not found in environment".format(key))
    return env_var
