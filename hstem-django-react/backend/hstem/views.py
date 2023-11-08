from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .services import get_all_rows

def hstem(request):
  names = get_all_rows("hstem test")
  return render(request, 'hstem.html', {'names': names})

