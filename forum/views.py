# forum/views.py
from django.shortcuts import render, get_object_or_404
from .models import Thread, Post

def thread_list(request):
    """Главная страница - список всех тем"""
    threads = Thread.objects.all()
    return render(request, 'forum/thread_list.html', {'threads': threads})

def thread_detail(request, thread_id):
    """Страница одной темы со всеми сообщениями"""
    thread = get_object_or_404(Thread, id=thread_id)
    posts = thread.posts.all()
    return render(request, 'forum/thread_detail.html', {
        'thread': thread,
        'posts': posts
    })
# Create your views here.
