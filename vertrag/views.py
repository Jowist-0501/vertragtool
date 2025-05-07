from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

#region Firma
# Liste aller Firmen
def firmen_liste(request):
    firmen = Firma.objects.all()
    return render(request, 'firmen/liste.html', {'firmen': firmen})

# Neue Firma erstellen
def firmen_erstellen(request):
    if request.method == 'POST':
        form = FirmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('firmen_liste')
    else:
        form = FirmaForm()
        return render(request, 'firmen/formular.html', {'form': form})

# Firma bearbeiten
def firmen_bearbeiten(request, pk):
    firma = get_object_or_404(Firma, pk=pk)
    form = FirmaForm(request.POST or None, instance=firma)
    if form.is_valid():
        form.save()
        return redirect('firmen_liste')
    return render(request, 'firmen/formular.html', {'form': form})

# Firma löschen
def firmen_loeschen(request, pk):
    firma = get_object_or_404(Firma, pk=pk)
    if request.method == 'POST':
        firma.delete()
        return redirect('firmen_liste')
    return render(request, 'firmen/bestaetigung.html', {'firma': firma})
#endregion Firma

#region Tätigkeiten
# Liste aller Tätigkeiten
def taetigkeiten_liste(request):
    taetigkeiten = Taetigkeit.objects.all()
    return render(request, 'taetigkeiten/liste.html', {'taetigkeiten': taetigkeiten})

# Neue Tätigkeit erstellen
def taetigkeiten_erstellen(request):
    if request.method == 'POST':
        form = TaetigkeitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taetigkeiten_liste')
    else:
        form = TaetigkeitForm()
        return render(request, 'taetigkeiten/formular.html', {'form': form})
    
# Tätigkeit bearbeiten
def taetigkeiten_bearbeiten(request, pk):
    taetigkeit = get_object_or_404(Taetigkeit, pk=pk)
    form = TaetigkeitForm(request.POST or None, instance=taetigkeit)
    if form.is_valid():
        form.save()
        return redirect('taetigkeiten_liste')
    return render(request, 'taetigkeiten/formular.html', {'form': form})

# Tätigkeit löschen
def taetigkeiten_loeschen(request, pk):
    taetigkeiten = get_object_or_404(Taetigkeit, pk=pk)
    if request.method == 'POST':
        taetigkeiten.delete()
        return redirect('taetigkeiten_liste')
    return render(request, 'taetigkeiten/bestaetigung.html', {'taetigkeiten': taetigkeiten})
#endregion Tätigkeiten

#region Verträge
def vertraege_liste(request):
    vertraege = Firma.objects.all()
    return render(request, 'vertraege/liste.html', {'vertraege': vertraege})

def vertrag_erstellen(request):
    if request.method == 'POST':
        form = VertragForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vertragsliste')
        
    else:
        form = VertragForm()

    return render(request, 'vertraege/vertrag_erstellen.html', {'form': form})
#endregion Verträge