from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import AircraftNote
from .forms import NoteForm
from datetime import date, datetime

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

def your_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or handle as necessary
    else:
        form = NoteForm()

    return render(request, 'form_template.html', {'form': form})

def add_note_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_one_ui')  # Redirect to the Unit One UI page
    else:
        form = NoteForm()
    
    return render(request, 'unit_one_ui.html', {'form': form})

def unit_one_notes(request):
    selected_date = request.GET.get('date', date.today().strftime("%Y-%m-%d"))
    notes = AircraftNote.objects.filter(service_time__date=selected_date)
    return render(request, 'unit_one_ui.html', {'notes': notes, 'current_date': selected_date})

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
