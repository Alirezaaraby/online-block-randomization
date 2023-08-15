from functools import wraps
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to access this page.")
    
    return login_required(_wrapped_view)
