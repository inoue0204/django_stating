from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .import mylibs
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.db import connection
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import ListView
import django

@login_required
def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'main/index.html', context)

@login_required
def profile(request):

    profile = None
    if hasattr(request.user, 'userprofile'):
        profile = request.user.userprofile

    context = {
        'user': request.user,
        'profile': profile
    }

    return render(request, 'main/profile.html', context)

def profile_create(request):

    form = UserProfileCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'main/profile_create.html', context)

@require_POST
def profile_save(request):

    form = UserProfileCreateForm(request.POST)

    if form.is_valid():
        userProfile = form.save(commit = False)
        userProfile.user = request.user
        userProfile.save()
        return redirect('main:profile')

    context = {
        'form': form,
    }

    return render(request, 'main/profile_create.html', context)

def regist(request):
    form = RegisterForm(request.POST or None)

    context = {
        'form': form,
    }
    return render(request, 'main/regist.html', context)


@require_POST
def regist_save(request):
    form = RegisterForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('main:index')

    context = {
        'form': form,
    }
    return render(request, 'main/regist.html', context)

class BookList(ListView):
    context_object_name = 'books'
    template_name = 'main/book_list.html'
    paginate_by = 5

    def get(self, request, *args, **kw):
        self.object_list = Book.objects.all().order_by('id')

        context = self.get_context_data(object_list = self.object_list)
        return self.render_to_response(context)

def book_edit(request, book_id=None):
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('main:book_list')
    else:
        form = BookForm(instance = book)

    return render(request, 'main/book_edit.html', dict(form = form, book_id = book_id))

def book_del(request, book_id):
    book = get_object_or_404(Book, pk = book_id)
    book.delete()
    return redirect('main:book_list')

class ImpressionList(ListView):
    context_object_name = 'impressions'
    template_name = 'main/impression_list.html'
    paginate_by = 3

    def get(self, request, *args, **kw):
        book = get_object_or_404(Book, pk = self.kwargs['book_id'])
        self.object_list = Impression.objects.filter(book_id = self.kwargs['book_id']).order_by('id')

        context = self.get_context_data(object_list = self.object_list)
        context['book'] = book
        return self.render_to_response(context)

def impression_edit(request, book_id, impression_id=None):

    book = get_object_or_404(Book, pk = book_id)

    if impression_id:
        impression = get_object_or_404(Impression, pk = impression_id)
    else:
        impression = Impression()
    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance = impression)

        if form.is_valid():
            if impression_id:
                form = ImpressionForm(request.POST, instance = impression)
                form.save()
            else:
                impression = Impression(
                    book_id = book_id,
                    comment = request.POST.get('comment')
                )
                impression.save()

            return redirect('main:impression_list', book_id = book_id)
    else:
        form = ImpressionForm(instance=impression)

    return render(request, 'main/impression_edit.html', dict(form = form, book_id = book_id, impression_id = impression_id))

def impression_del(request, book_id, impression_id):
    impression = get_object_or_404(Impression, pk = impression_id)
    impression.delete()
    return redirect('main:impression_list', book_id = book_id)
