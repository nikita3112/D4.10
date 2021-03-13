from django.shortcuts import render, redirect
from p_library.models import Book, Author, PublishingHouse
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        'title': 'мою библиотеку',
        'books': books,
        'range': range(101),
        }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def publish_house_list(request):
    template = loader.get_template('publish.html')
    Pub = PublishingHouse.objects.all()
    data = {
        'pub':Pub,
    }
    return HttpResponse(template.render(data, request))