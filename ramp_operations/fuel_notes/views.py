from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import AircraftNote

@login_required
def user_redirect(request):
    if request.user.is_superuser or is_admin(request.user):
        return redirect('admin_ui')
    elif is_unit_one(request.user):
        return redirect('unit_one_ui')
    elif is_fueler(request.user):
        return redirect('fueler_ui')
    elif is_overview(request.user):
        return redirect('overview_ui')
    else:
        # Redirect to a default page if the user doesn't belong to any group
        return render(request, 'index.html')

def unit_one_notes(request):
    notes = AircraftNote.objects.all()
    return render(request, 'unit_one_notes.html', {'notes': notes})

def is_admin(user):
    return user.groups.filter(name='Admin').exists() or user.is_superuser

def is_unit_one(user):
    return user.groups.filter(name='Unit One').exists()

def is_fueler(user):
    return user.groups.filter(name='Fueler').exists()

def is_overview(user):
    return user.groups.filter(name='Overview').exists()

@login_required
@user_passes_test(is_admin, login_url='/', redirect_field_name=None)
def admin_ui(request):
    return render(request, 'admin_ui.html')

@login_required
@user_passes_test(is_unit_one, login_url='/', redirect_field_name=None)
def unit_one_ui(request):
    return render(request, 'unit_one_ui.html')

@login_required
@user_passes_test(is_fueler, login_url='/', redirect_field_name=None)
def fueler_ui(request):
    return render(request, 'fueler_ui.html')

@login_required
@user_passes_test(is_overview, login_url='/', redirect_field_name=None)
def overview_ui(request):
    return render(request, 'overview_ui.html')
