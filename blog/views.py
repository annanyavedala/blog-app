from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug_text):
    q= Post.objects.filter(slug=slug_text)
    if q.exists():
       q= q.first()
    else:
        return HttpResponse("Page Not found")
    return render(request, 'blog/post_detail.html', {'post': q})