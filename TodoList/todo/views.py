from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Todo

def index(request):
    return render(request, 'index.html')

def todo(request):
    wait_list = Todo.objects.filter(status='wait').order_by('-created_at')
    ing_list = Todo.objects.filter(status='ing').order_by('-created_at')
    done_list = Todo.objects.filter(status='done').order_by('-created_at')

    context = {
        'wait_list': wait_list,
        'ing_list': ing_list,
        'done_list': done_list,
    }
    return render(request, 'todo.html', context)

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content', '')
    if not title.strip():
        messages.error(request, '제목은 필수 입력 항목입니다.')
        return HttpResponseRedirect(reverse('todo'))

    Todo.objects.create(title=title, content=content)
    return HttpResponseRedirect(reverse('todo'))

def read(request, no):
    try:
        todo = Todo.objects.get(no=no)
    except Todo.DoesNotExist:
        return HttpResponseRedirect(reverse('todo'))
    
    return render(request, 'todo_read.html', {'todo': todo})


def update(request):
    no = request.POST.get('no')
    try:
        todo = Todo.objects.get(no=no)
        todo.title = request.POST['title']
        todo.content = request.POST.get('content', '')
        todo.status = request.POST['status']  # 상태도 업데이트
        todo.save()
    except Todo.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('todo'))


def delete(request):
    no = request.POST.get('no')
    try:
        todo = Todo.objects.get(no=no)
        todo.delete()
    except Todo.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('todo'))

# 상태 변경
def mark_ing(request):
    no = request.POST.get('no')
    try:
        todo = Todo.objects.get(no=no)
        todo.status = 'ing'
        todo.save()
    except Todo.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('todo'))

def toggle_complete(request):
    no = request.POST.get('no')
    try:
        todo = Todo.objects.get(no=no)
        if todo.status == 'done':
            todo.status = 'ing'
        else:
            todo.status = 'done'
        todo.save()
    except Todo.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('todo'))

def mark_wait(request):
    no = request.POST.get('no')
    try:
        todo = Todo.objects.get(no=no)
        todo.status = 'wait'
        todo.save()
    except Todo.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('todo'))
