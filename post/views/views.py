from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from account.models import UsersGroups
from post.models import Post


def index(request):
    return render(request, "post/index.html")


@login_required
def getPosts(request):
    context = {}
    user_group = UsersGroups.objects.get(user_id=request.user.id)
    posts = Post.objects.filter(group=user_group.group)
    context["posts"] = posts
    print(context)
    return render(request, "post/index.html", context)