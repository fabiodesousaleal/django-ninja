from ninja import ModelSchema
from .models import Livro

class LivroSchema(ModelSchema):
    class Meta:
        model = Livro
        fields = '__all__'
        #exclude = ['password', 'last_login', 'user_permissions']
        #fields_optional = '__all__'

