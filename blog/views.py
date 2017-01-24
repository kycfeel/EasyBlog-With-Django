from django.shortcuts import render

def post_lists(request):
    return render(request, 'blog/post_list.html', {})
