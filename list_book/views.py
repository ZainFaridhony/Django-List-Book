from django.shortcuts import render, redirect
from .forms import Bookform
from .models import Books
# Create your views here.


def book_list(request):
    context = {'list': Books.objects.all()}
    return render(request, "list_book/list.html", context)


def book_add(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = Bookform()
        else:
            book = Books.objects.get(pk=id)
            form = Bookform(instance=book)
        return render(request, "list_book/add.html", {'form': form})
    else:
        if id == 0:
            form = Bookform(request.POST)
        else:
            book = Books.objects.get(pk=id)
            form = Bookform(request.POST, instance=book)

        if form.is_valid():
            form.save()
        return redirect('/')


def book_delete(request, id):
    book = Books.objects.get(pk=id)
    book.delete()
    return redirect('/')
