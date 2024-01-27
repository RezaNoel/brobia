from django.shortcuts import render

# Create your views here.
def blog_list(request):
    return render(request, 'blog/blog-list.html')

def blog_single(request,slug):
    return render(request, 'blog/blog-single.html')
