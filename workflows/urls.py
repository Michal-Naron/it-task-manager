from operator import index

from django.urls import path

url_patterns = [
    path('', index, name="index")
]

app_name = 'workflows'