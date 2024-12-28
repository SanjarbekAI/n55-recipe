from django.shortcuts import render, get_object_or_404

from blogs.models import BlogModel


def blog_list_view(request):
    blogs = BlogModel.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, 'blogs/blogs_list.html', context)


def blog_detail_view(request, pk):
    blog = get_object_or_404(BlogModel, id=pk)
    latest_blogs = BlogModel.objects.order_by('-created_at')[:4]
    if blog is not None:
        context = {
            "blog": blog,
            'latest_blogs': latest_blogs
        }
        return render(request, 'blogs/blog_detail.html', context)
