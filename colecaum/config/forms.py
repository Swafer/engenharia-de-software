from django import forms
from app.models import carro
from app.models import reparo
# inicializando um formulario para os livros
class carrinhos(forms.ModelForm):
    class Meta:
        # modelo referente: Book
        model = carro
        # atribuindo todos os campos do modelo Book ao Form
        fields = '__all__'

class reparos(forms.ModelForm):
    class Meta:
        # modelo referente: Book
        model = reparo
        # atribuindo todos os campos do modelo Book ao Form
        fields = '__all__'