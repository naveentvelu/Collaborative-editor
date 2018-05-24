from django.shortcuts import render

# Create your views here.
def Edit(request):
    return render(request, 'editor.html', {})
