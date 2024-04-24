from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print_hello(request):
    movie_data= {'movies': [
        {
       'title':'Godfather',
       'year':1990,
       'summary':'Story of an Family',
       'sucess':True
        },
        {
       'title':'LEO',
       'year':2023,
       'summary':'Story of an Man',
       'sucess':True
        },
        {
       'title':'Kannur Squad',
       'year':2023,
       'summary':'Story of an Police officer',
       'sucess':True
        },
        {
       'title':'Titanic',
       'year':1990,
       'summary':'Story of an Ship',
       'sucess':True
        }
    ]
    }
    
    return render(request,'hello2.html',movie_data)

def print_hello1(request):
    movie_data= {'movies': [
        {
       'title':'Godfather',
       'year':1990,
       'summary':'Story of an Family',
       'sucess':True
        },
        {
       'title':'LEO',
       'year':2023,
       'summary':'Story of an Man',
       'sucess':True
        },
        {
       'title':'Kannur Squad',
       'year':2023,
       'summary':'Story of an Police officer',
       'sucess':True
        },
        {
       'title':'Titanic',
       'year':1990,
       'summary':'Story of an Ship',
       'sucess':True
        }
    ]
    }
    
    return render(request,'hello2.html',movie_data)