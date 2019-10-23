from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def inde(request):
    return HttpResponse("Home")


def analyze(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''][!"#$%&'()*+,./:;<=>?@\^_`|{}~-]'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose': 'Remove Punctuation', 'analyzed_text':
                 analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        param = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char

        param = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":

        count = 0
        for i in djtext:
            if not i == " ":
                count += 1
        param = {'purpose': 'Character Counter', 'analyzed_text': count}

    if removepunc != 'on' and fullcaps != "on" and newlineremover != "on" and charcount != "on":
        return HttpResponse("Please Select any operation")

    return render(request, 'analyzed.html', param)


