from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import argparse
import json
import os
import generator
from .sample import sample

# Create your views here.

@login_required
def process(request):
    if not request.user.is_authenticated:
        return render('error.html')
    else:
        return render(request, 'process.html')

@login_required
def user_list(request):
    return render(request, 'user_list.html')

@login_required
def maker(request):
    return render(request, 'maker.html')

@login_required
def tech(request):
    return render(request, 'tech.html')

@login_required
def logout(request):

    request.session.clear()
    return redirect('/')

@login_required
def run(request):
    msg="Error"
    if request.method == 'POST':
        content = request.POST['dahyun']
        sentense_generator = sample(100, header = content, num_chars = 200)
        context = {
            'content' : content,
            'result' : sentense_generator
        }

        return render(request, 'process.html', context)
    else:
        return render(request, 'process.html',msg)
