from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    data = {'user': request.user}
    return render(request, 'homepage/index.html', context=data)

