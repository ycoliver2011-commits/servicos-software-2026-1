import os
import sqlites
from fastapi import FastAPI , UplooadFile, File, From

app = FatAPI()

DIRETORIO_DADOS = "/dados"
DB_PATH = f"{DIRETORIO_DADOS}/banco.db"

