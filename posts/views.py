from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Post_Attachments
from .form import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    # l = [i for i in range(1, 10)]
    miras = Post.objects.all() # SELECT * FROM Post 
    for post in miras:
        att = Post_Attachments.objects.filter(post_id = post.pk)
        post.att = att
    return render(request, 'posts/index.html', {"x": miras})

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
        return render(request, 'posts/addPost.html', {"form": form})
@login_required
def edit_post(request, pid):
    # p = get_object_or_404(post, pk=pid)
    p = Post.objects.get(pk=pid)
    if request.method != 'POST':
        form = PostForm(instance=p)
    else:
        form = PostForm(request.POST, instance=p)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    
    return render(request, 'posts/editPost.html', {'form': form})
@login_required       
def delete_post(request, pid):
    post = Post.objects.get(pk = pid)
    post.delete()
    return redirect('post_list')

    
    

# create
# use