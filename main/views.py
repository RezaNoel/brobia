from django.shortcuts import render


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)

