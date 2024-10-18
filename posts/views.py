from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .form import PostForm

# Create your views here.

def index(request):
    # l = [i for i in range(1, 10)]
    miras = Post.objects.all() # SELECT * FROM Post 



    return render(request, 'posts/index.html', {"x": miras})

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
        return render(request, 'posts/addPost.html', {"form": form})

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
            
            

    
    

# create
# use