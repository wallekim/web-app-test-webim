from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from schedule import every, repeat, run_pending
import time
import random


def HomeView(request):
    return render(request, 'home.html')




# @repeat(every(5).seconds)
# def job(self):
#     return random.random()
#
#
# while True:
#     run_pending()
#     time.sleep(1)



