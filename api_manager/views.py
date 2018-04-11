from django.http import HttpResponse
from rest_framework.decorators import api_view

from api_manager.drivers.stack_driver import *


def index():
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['POST'])
def stack(request):
    if request.method == 'POST':
#        parameters = DataSerializer(request.data)
        create_stack(request.data)
        return HttpResponse("OK!")
