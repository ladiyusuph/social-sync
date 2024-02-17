from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.core.paginator import (Paginator, EmptyPage,
                                   PageNotAnInteger)
from django.views.decorators.http import require_GET, require_POST
from .forms import ImageCreateForm
from .models import Image
from actions.utils import create_action


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            create_action(request.user, 'bookmarked image', new_item)
            messages.success(request, 'Image added successfully')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 
                  'images/image/detail.html', 
                  {'section': 'images', 
                   'image': image})
    
    
# @login_required
# @require_POST
# def image_like(request):
#     image_id = request.POST.get('id')
#     action = request.POST.get('action')
    
#     if image_id and action:
#         try:
#             image = Image.objects.get(id=image_id)
            
#             if action =="like":
#                 image.users_like.add(request.user)
#             else:
#                 image.users_like.remove(request.user)
                
#             return JsonResponse({'status':'ok'})
#         except Image.DoesNotExist:
#             pass
        
#         return JsonResponse({'status':'error'})
    
    
@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')
    
    try:
        images=paginator.page(page)
        
    except PageNotAnInteger:
        
        images=paginator.page(1)
    except EmptyPage:
        if images_only:
            
            return HttpResponse('')
        
        image = paginator.page(paginator.num_pages)
        
    if images_only:
        return render(request,
                      'images/image/list_images.html',
                      {'section':'images',
                       'images':images})
    
    return render(request,
                  'images/image/list.html',
                  {'section':'images',
                   'images':images})
    
    
    
    

def like_image(request, pk):
    if request.user.is_authenticated:
        image = get_object_or_404(Image, id=pk)
        if image.users_like.filter(id=request.user.id):
            image.users_like.remove(request.user)
            
        else:
            image.users_like.add(request.user)
            create_action(request.user, 'likes', image)
    return redirect('images:detail',image.id, image.slug)


# def unlike_image(request, image_id):
#     image = get_object_or_404(Image, id=image_id)
#     image.users_like.remove(request.user)
#     return JsonResponse({'unliked': True})    
    
    
    
    
    
    
    
    
    
    
    
    
    