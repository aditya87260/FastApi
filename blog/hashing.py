from passlib.context import CryptContext


pwd_cxt=CryptContext(schemes=['bcrypt'], deprecated='auto') # for getting encrypted password in response not the actual password


class Hash():
    def bcrypt(password:str):
        return pwd_cxt.hash(password)
