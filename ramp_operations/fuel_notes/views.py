from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import AircraftNote
from .forms import EditNoteForm, NoteForm
from datetime import date
from django.http import JsonResponse

def is_admin(user):
    return user.groups.filter(name='Admin').exists() or user.is_superuser

def is_unit_one(user):
    return user.groups.filter(name='Unit One').exists()

def is_fueler(user):
    return user.groups.filter(name='Fueler').exists()

def is_overview(user):
    return user.groups.filter(name='Overview').exists()

@login_required
def user_redirect(request):
    """Redirect users to their specific UI based on their group."""
    redirect_urls = {
        'is_admin': 'admin_ui',
        'is_unit_one': 'unit_one_ui',
        'is_fueler': 'fueler_ui',
        'is_overview': 'overview_ui',
    }
    for check, url in redirect_urls.items():
        if globals()[check](request.user):
            return redirect(url)
    return render(request, 'index.html')

@login_required
@user_passes_test(is_admin, login_url='/', redirect_field_name=None)
def admin_ui(request):
    return render(request, 'admin_ui.html')

@login_required
@user_passes_test(is_unit_one, login_url='/', redirect_field_name=None)
def unit_one_ui(request):
    notes = AircraftNote.objects.all().order_by('-created_at')
    return render(request, 'unit_one_ui.html', {'notes': notes})

@login_required
@user_passes_test(is_fueler, login_url='/', redirect_field_name=None)
def fueler_ui(request):
    return render(request, 'fueler_ui.html')

@login_required
@user_passes_test(is_overview, login_url='/', redirect_field_name=None)
def overview_ui(request):
    return render(request, 'overview_ui.html')

def add_note_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_one_ui')
    else:
        form = NoteForm()
    return render(request, 'unit_one_ui.html', {'form': form})

def unit_one_notes(request):
    notes = AircraftNote.objects.all().order_by('-created_at')
    return render(request, 'unit_one_ui.html', {'notes': notes})

def get_note_data(request, note_id):
    note = AircraftNote.objects.get(id=note_id)
    return JsonResponse({
        'tail_number': note.tail_number,
        # Include other fields
    })

def edit_note_view(request, note_id):
    note = AircraftNote.objects.get(id=note_id)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('unit_one_ui')
    else:
        form = EditNoteForm(instance=note)
    return render(request, 'unit_one_ui.html', {'form': form})