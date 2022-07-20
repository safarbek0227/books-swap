from django.shortcuts import render
from main.models import Book
from django.http import JsonResponse
from .forms import choices
from django.shortcuts import get_object_or_404
import json
# Create your views here.

def adminView(request):
    if request.user.is_staff:
        form = choices(request.POST or None)
        context ={
            'form': form
        }   
        if request.method == 'POST':
            if form['category'].value()== 'unread':
                context ={
                    'obj_list': Book.objects.select_related('author', 'genre').filter(is_checked=False, is_ban=False),
                    'can_changes':True,
                    'form': form
                }
            if form['category'].value()== 'checked':
                context ={
                    'obj_list':Book.objects.select_related('author', 'genre').filter(is_checked=True),
                    'can_changes':False,
                    'form': form
                }
            if form['category'].value()== 'ban':
                context ={
                    'obj_list': Book.objects.select_related('author', 'genre').filter(is_ban=True),
                    'can_changes':False,
                    'form': form
                }
        return render(request, 'dashboard/index.html', context)
    else:
        return render(request, '404.html')
    

def checker(request):
    if request.user.is_staff:
        if request.method == 'GET':
            obj = json.loads(request.GET['data'])
            product = Book.objects.get(id = obj['id'])
            if object:
                product.is_ban = True if obj['is_ban'] else False
                product.is_checked = True if obj['is_checked'] else False

                product.save()
                response = {'success': 'succesfuly compilted'}
            else:
                response = {'success': 'unsuccesfuly compilted'}

        return JsonResponse(response) 
    else:
        return render(request, '404.html')