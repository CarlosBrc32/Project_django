from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from app_family.models import familiar

def main_instruction(self):

    template = loader.get_template('templates.html')

    context = {'now' : datetime.now(),}

    document = template.render(context)

    return HttpResponse(document)

def create_family(
        self, name:str='name', last_name: str='last_name', age: int=0, birth: str='birth', tipo: str='tipo'
):
    template = loader.get_template('templates_familiar.html')

    pariente = familiar(
        name = name,
        last_name = last_name,
        age = age,
        birth = birth,
        tipo = tipo
    )
    pariente.save()

    context = {
        'pariente' : pariente,
    }

    render = template.render(context)

    return HttpResponse(render)

def mostrar (self):

    template = loader.get_template("templates_mostrar.html")

    context = {
        'mostrar' : familiar,
    }

    render = template.render(context)

    return HttpResponse(render)
