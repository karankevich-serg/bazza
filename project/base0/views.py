from django.shortcuts import render
from .models import BsInTsm
from .models import *

# Create your views here.
# def index(request):
#     table1 = LeftSide.objects.all()
#     return render(request,'base0/index.html', {'title': 'ТАБЛИЦА BS', 'bs' : table1 })


def index(request):
    table0 = AggregatorsType.objects.all()
    table1 = Aggregator.objects.all()
    table2 = Matrix.objects.all()
    table3 = Direction.objects.all()
    table4 = Stream.objects.all()
    return render(request,'base0/index.html', {'title': 'ТАБЛИЦЫ ТЕСТОВЫЕ', 't0': table0, 't1': table1, 't2': table2, 't3': table3, 't4': table4})


# Приведенный   код вернет список, содержащий все имена полей.
# my_model_fields = [field.name for field in MyModel._meta.get_fields()]