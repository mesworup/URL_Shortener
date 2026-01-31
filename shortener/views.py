from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import ShortURL
from .forms import ShortURLForm
from .utils import generate_short_code

@login_required
def dashboard(request):
    urls = ShortURL.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"urls": urls})

@login_required
def create_short_url(request):
    form = ShortURLForm(request.POST or None)
    if form.is_valid():
        short = form.save(commit=False)
        short.user = request.user

        custom = form.cleaned_data.get("custom_code")
        short.short_code = custom if custom else generate_short_code()

        if ShortURL.objects.filter(short_code=short.short_code).exists():
            form.add_error("custom_code", "Short code already exists")
        else:
            short.save()
            return redirect("dashboard")

    return render(request, "create.html", {"form": form})

@login_required
def delete_url(request, id):
    url = get_object_or_404(ShortURL, id=id, user=request.user)
    url.delete()
    return redirect("dashboard")

#redirect 
def redirect_url(request, short_code):
    url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(url.original_url)
