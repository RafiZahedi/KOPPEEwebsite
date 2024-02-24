from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

from .models import Reservation
from .forms import ReserveFrom


def home(request):
    return render(request, 'home.html')


def reservation(request):
    form = ReserveFrom()
    if request.method == 'POST':
        form = ReserveFrom(request.POST)
        print(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('success-page', pk=instance.pk)
    context = {'form': form}
    return render(request, 'reservation.html', context)


# @cache_control(max_age=0)
def success_page(request, pk):
    reserves = Reservation.objects.get(id=pk)
    context = {'reserves': reserves}
    return render(request, 'success_page.html', context)


def contact(request):
    return render(request, 'contact.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # try:
        #     user = User.objects.get(username=username)
        # except User.DoesNotExist:
        #     messages.error(request, 'Invalid username or password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin-panel')
        else:
            messages.error(request, 'Username or password is Incorrect')
    return render(request, 'admin_login.html')


def admin_logout(request):
    logout(request)
    return redirect('admin-login')


@login_required(login_url='/admin_login')
def admin_panel(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    sort_by = request.GET.get('sort_by')
    ord_by = request.GET.get('order_by')
    ordering = 'date'
    if sort_by in ['date', 'time', 'number_of_people']:
        ordering = sort_by
    if ord_by == 'dec':
        reserves = Reservation.objects.filter(
            Q(name__icontains=q) |
            Q(email__icontains=q)
        ).order_by('-' + ordering)
    else:
        reserves = Reservation.objects.filter(
            Q(name__icontains=q) |
            Q(email__icontains=q)
        ).order_by(ordering)

    context = {
        "reserves": reserves,
        'sort_by': sort_by
    }
    return render(request, 'admin_panel.html', context)
