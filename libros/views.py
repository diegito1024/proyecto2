from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista.html', {'libros': libros})

def agregar_libro(request):
    form = LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'libros/form.html', {'form': form})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    form = LibroForm(request.POST or None, instance=libro)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'libros/form.html', {'form': form})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'libros/eliminar.html', {'libro': libro})

def toggle_disponible(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.disponible = not libro.disponible
    libro.save()
    return redirect('lista_libros')

def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="libros.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 800, "Listado de Libros")
    y = 760

    for libro in Libro.objects.all():
        p.drawString(100, y, f"{libro.titulo} - {libro.autor}")
        y -= 20

    p.showPage()
    p.save()
    return response


