from pyexpat.errors import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo

# Create your views here.
# 메인
def index(request):
    print('메인 화면...')
    return render(request, 'index.html', {})

# 전체 출력 
def todo(request):
    print('할 일 목록 화면')
    # Todo 모델의 대기 목록 조회
    wait_list = Todo.objects.filter(is_completed=False).order_by('-created_at')
    # Todo 모델의 진행 목록 조회
    ing_list = Todo.objects.filter(is_completed=True).order_by('-created_at')

    content = {'wait_list' : wait_list,'ing_list' : ing_list}
    # render(request, 템플릿 경로, 데이터{})
    # - 데이터 {} : 템플릿에 데이터를 전달
    return render(request, 'todo.html', content)

# create
def create(request):
    print('할 일 등록')
    title = request.POST['title']
    content = request.POST.get('content', '')
    # 유효성 검사
    if not title.strip():
        messages.error(request, '제목은 필수 입력 항목입니다.')
        return HttpResponseRedirect(reverse('todo'))

    Todo.objects.create(title=title, content=content)
    return HttpResponseRedirect(reverse('todo'))

# read
def read(request, no):
    print('상세 요청')
    try:
        todo = Todo.objects.get(no=no)
    except Todo.DoesNotExist:
        print('상세 요청한 할 일이 없습니다.')
        return HttpResponseRedirect(reverse('todo'))
    
    return render(request, 'todo_read.html', {'todo': todo})


# update
def update(request):
    print('수정 요청')
    no = request.POST['no']
    try:
        todo = Todo.objects.get(no=no)
        todo.title = request.POST['title']
        todo.content = request.POST.get('content', '')
        todo.is_completed = 'is_completed' in request.POST
        todo.save()
        print('수정 완료')
    except Todo.DoesNotExist:
        print('수정할 할 일이 없습니다.')
    return HttpResponseRedirect(reverse('todo'))

# delete
def delete(request):
    print('삭제 요청')
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        todo.delete()
    except Todo.DoesNotExist:
        print('삭제할 할 일이 없습니다.')
    return HttpResponseRedirect(reverse('todo'))


# 진행 처리 (is_completed = True 설정)
def mark_ing(request):
    print('진행 상태로 변경 요청')
    no = request.POST['no']
    try:
        todo = Todo.objects.get(no=no)
        todo.is_completed = True
        todo.save()
        print(f'{no}번 항목을 진행 상태로 변경')
    except Todo.DoesNotExist:
        print('해당 항목이 없습니다.')
    return HttpResponseRedirect(reverse('todo'))


def toggle_complete(request):
    no = request.POST['no']
    try:
        todo = Todo.objects.get(no=no)
        todo.is_completed = not todo.is_completed
        todo.save()
    except Todo.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('todo'))