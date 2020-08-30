from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    return render(request, 'index.html')


def analyze(request):
    global analyzed
    get_text = request.POST.get('text_analzer', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('cap', 'off')
    new_line_remover = request.POST.get('new_line_rem', 'off')
    space_remover = request.POST.get('space_rem', 'off')
    char_counter = request.POST.get('char_count', 'off')
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in get_text:
            if char in punctuations:
                get_text = get_text.replace(char, "")
        # params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if capitalize == "on":
        get_text = get_text.upper()
        # params = {'purpose': 'Change to Upper', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if new_line_remover == "on":
        get_text = get_text.replace('\n', "")
        get_text = get_text.replace('\r', "")
        # params = {'purpose': 'Change to Upper', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if space_remover == "on":
        get_text = re.sub(' +', ' ', get_text)
        # params = {'purpose': 'Change to Upper', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if char_counter == "on":
        analyzed = str(len(get_text))
        get_text = get_text + " Total Characters: " + analyzed
        # params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    params = {'purpose': 'Output Text', 'analyzed_text': get_text}
    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact_us.html')