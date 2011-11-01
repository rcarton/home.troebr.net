from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext






@login_required
def home(request):
    """Home page."""
    return render_to_response('home.html', RequestContext(request, {}))


def hello(request):
    """Auth page."""
    
    name = ''
    unknown = True
    if request.method == 'POST':
        name = request.POST.get('HI_THERE', None).lower()
        password = request.POST.get('PASSWURD', None)
        name = 'tim' if name == 'timothy' else name
        name = 'rachel' if name == 'montoose' else name
        
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                unknown = False
            else:
                # Return a 'disabled account' error message
                pass
    next = request.GET.get('next', request.POST.get('next', '/'))
        
    return render_to_response('hello.html', RequestContext(request, {'cname': name, 'unknown': unknown, 'next': next}))  
    
    
    
def disconnect(request):
    logout(request)
    return redirect('hello')