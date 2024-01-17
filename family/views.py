from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def main_instruction(self):

    template = loader.get_template('templates.html')

    context = {'now' : datetime.now(),}

    document = template.render(context)

    return HttpResponse(document)
