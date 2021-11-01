from django.shortcuts import render, redirect
from .models import SiteComments
from .forms import SiteCommentForm

def Sitecomment(request):
    sitecomments = SiteComments.objects.all()
    if request.method == 'POST':
        c_form = SiteCommentForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return redirect('comment-page')
    else:
        form = SiteCommentForm()

        context = {
        'sitecomments':sitecomments,
        'form':form
    
}
    return render(request, 'Sitecomments/single-post.html', context)
