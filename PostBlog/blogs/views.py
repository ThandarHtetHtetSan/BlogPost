from django.views import generic
from .models import Post,PostImage
from django.shortcuts import get_object_or_404

# Create your views here.
def blog_view(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})
def detail_view(request,id):
    post=get_object_or_404(Post,id=id)
    photos=PostImage.objects.filter(post=post)
    return render(request,'post_detail.html',{
        'post': post,
        'photos':photos
    })


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

#
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


from django.shortcuts import render

# Create your views here.
