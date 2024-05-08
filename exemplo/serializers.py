from ninja import Schema

class LivroSchemaIn(Schema):    
    titulo: str
    autor: str

class LivroSchemaOut(Schema):
    id: int    
    titulo: str
    autor: str