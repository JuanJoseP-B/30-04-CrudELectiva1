from django.shortcuts import render, redirect, get_object_or_404
from .models import Calificacion
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CalificacionForm, UsernameRecoveryForm, UserRegisterForm

def recover_username(request):
    if request.method == 'POST':
        form = UsernameRecoveryForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            users = User.objects.filter(email=email)
            if users.exists():
                # En un entorno real, enviaríamos un correo. Aquí simulamos con un mensaje.
                usernames = ", ".join([u.username for u in users])
                messages.success(request, f"Se ha encontrado el usuario asociado a este correo: {usernames}")
            else:
                messages.error(request, "No se encontró ningún usuario con ese correo electrónico.")
    else:
        form = UsernameRecoveryForm()
    return render(request, 'registration/recover_username.html', {'form': form})
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar_calificaciones')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    promedio_general = Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg'] or 0
    return render(request, 'calificaciones/listar.html', {
        'calificaciones': calificaciones,
        'promedio_general': round(promedio_general, 2)
    })

@login_required
def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_calificaciones')
    else:
        form = CalificacionForm()
    return render(request, 'calificaciones/crear.html', {'form': form})

@login_required
def editar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('listar_calificaciones')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'calificaciones/editar.html', {'form': form, 'calificacion': calificacion})

@login_required
def eliminar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('listar_calificaciones')
    return render(request, 'calificaciones/eliminar.html', {'calificacion': calificacion})

@login_required
def promedio_general_view(request):
    promedio_general = Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg'] or 0
    return render(request, 'calificaciones/promedio_general.html', {
        'promedio_general': round(promedio_general, 2)
    })
