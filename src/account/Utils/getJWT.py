import jwt, os, time
from dotenv import load_dotenv

def getJWT(payload):
    payload["exp"] = int(time.time()) + (7*24*60*60)
    load_dotenv()
    key = os.getenv("SECRET_KEY")
    encoded = jwt.encode(payload, key, algorithm="HS256")

    return encoded