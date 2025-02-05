from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'jamal',
        'title':'Post 1',
        'content':'This is the first post',
        'date':'18 jan 1993'
    },
    {
        'author':'jinco',
        'title':'Post 2',
        'content':'This is the second post',
        'date':'19 jan 1993'
    }
]
def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})



