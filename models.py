import db
from sqlalchemy import Column, Integer, String, Boolean

class Noticia (db.Base):
    __tablename__ = "Noticias"
    id = Column(Integer, primary_key=True) # Automaticamente esta PK se convertirá en SERIAL (AUTOINCREMENT)
    contenido = Column(String(200), nullable=False)
    deportiva = Column(Boolean)
    internacional = Column(Boolean)

    def __init__(self, contenido, deportiva, internacional):
        self.contenido = contenido
        self.deportiva = deportiva
        self.internacional = internacional

    def __str__(self):
        return "Tarea({}: {}, {}, {})".format(self.id, self.contenido, self.deportiva, self.internacional)