from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import PostModelForm, TutModelForm, UserRegisterForm
from .models import Technology, Tutorial, Upvote
from django.contrib.auth.decorators import login_required


def list_tech(request):
    print(request.user)
    technologies = Technology.objects.all()
    context = {
        'technologies': technologies
    }
    return render(request, 'blog/tech_list.html', context)


def tech_detail(request, pk):
    technology = get_object_or_404(Technology, pk=pk)
    tutorials = Tutorial.objects.filter(tech=technology)
    return render(request, 'blog/tech_detail.html', {'technology': technology, 'tutorials': tutorials})


def tech_create(request):
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form' : form
    }
    return render(request, "blog/tech_create.html", context)


def tut_list(request):
    tutorials = Tutorial.objects.all()
    context = {
        'tutorials' : tutorials
    }
    return render(request, 'blog/tut_list.html', context)


def tut_create(request):
    form = TutModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            var = form.save(commit = False)
            var.users = request.user
            var.save()
            a = var.tech.id
            return redirect('tech_detail',pk=a)
    context = {
        'form' : form
    }django
    return render(request, "blog/tut_create.html", context)

@login_required(login_url="/login/")
def tut_upvote(request, pk):django
    tutorial = get_object_or_404(Tutorial, pk=pk)
    tutorial.upvote +=1
    tutorial.save()
    upvote = Upvote.objects.create(tutorial=tutorial, user=request.user)
    return redirect("tech_detail", pk = tutorial.tech.pk)

@login_required(login_url="/login/")
def tut_unupvote(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    tutorial.upvote -=1
    tutorial.save()
    upvote = Upvote.objects.filter(tutorial=tutorial, user=request.user).first()
    upvote.delete()
    return redirect("tech_detail", pk = tutorial.tech.pk)    


def register(request):django
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('/login/')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})
    











