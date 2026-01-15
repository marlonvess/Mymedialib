from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import MediaItem
from .forms import MediaItemForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def post_list(request):
    media_items = MediaItem.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'medialib/post_list.html', {'media_items': media_items})

def post_detail(request, pk):
    media_item = get_object_or_404(MediaItem, pk=pk)
    return render(request, 'medialib/post_detail.html', {'media_item': media_item})

@login_required
def post_edit(request, pk):
    media_item = get_object_or_404(MediaItem, pk=pk)
    if request.method == "POST":
        form = MediaItemForm(request.POST, instance=media_item)
        if form.is_valid():
            media_item = form.save(commit=False)
            media_item.user = request.user
            media_item.save()
            return redirect('medialib:post_detail', pk=media_item.pk)
    else:
        form = MediaItemForm(instance=media_item)
    return render(request, 'medialib/post_edit.html', {'form': form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = MediaItemForm(request.POST)
        if form.is_valid():
            media_item = form.save(commit=False)
            media_item.user = request.user
            media_item.save()
            return redirect('medialib:post_detail', pk=media_item.pk)
    else:
        form = MediaItemForm()
    return render(request, 'medialib/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    media_items = get_object_or_404(MediaItem, pk=pk)
    if request.method=='POST':
        media_items.delete()
    return redirect('medialib:post_list')