from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def Book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html',
                  {'books': books})

def Book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        Book.objects.create(
            title=title,
            author=author,
            price=price
        )
        return redirect('book_list')

    return render(request, 'book_form.html')

def Book_update(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.save()

        return redirect('book_list')

    return render(request, 'book_form.html',
                  {'book': book})

def Book_delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
