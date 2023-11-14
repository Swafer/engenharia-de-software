from django.contrib import admin
from app.models import *
from config.forms import *

class pocoio(admin.TabularInline): 

    model = carro
    form = carrinhos
    extra = 1 

class marcaAdmin(admin.ModelAdmin):
    inlines = [pocoio]
admin.site.register(marca, marcaAdmin)

class mikey(admin.TabularInline): 

    model = reparo
    form = reparos
    extra = 1 

class carroaAdmin(admin.ModelAdmin):
    inlines = [mikey]
admin.site.register(carro, carroaAdmin)

admin.site.register(vagas)
admin.site.register(modelo)
admin.site.register(categoria)
