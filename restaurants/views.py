from django.shortcuts import render

context = {
    'msg':'Hello World!'}

def home(request):
    return render(request,'home_page.html', context)

