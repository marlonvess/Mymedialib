from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import MediaItem


# Create your views here.

def post_list(request):
    media_items = MediaItem.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'medialib/post_list.html', {'media_items': media_items})

def post_detail(request, pk):
    post = get_object_or_404(MediaItem, pk=pk)
    return render(request, 'medialib/post_detail.html', {'post': post})