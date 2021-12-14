from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from schedule import every, run_pending
from threading import *
import time
from random import randint


def job():
    global random_value
    random_value = randint(0, 9999)


def timer():
    every(5).seconds.do(job)
    while True:
        run_pending()
        time.sleep(1)


random_value = 0
t1 = Thread(target=timer, daemon=True)
t1.start()


def HomeView(request):
    if request.user.is_authenticated:
        return redirect('randomizer/')
    return render(request, 'home.html')


@login_required
def ValueView(request):
    data = {'random_value': random_value}
    return render(request, 'randomizer.html', context=data)
