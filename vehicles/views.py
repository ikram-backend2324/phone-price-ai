import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import PhoneInspection, PhoneBrand
from .forms import PhoneInspectionForm
from .ai_module import analyze_phone_image


@login_required
def index(request):
    if request.user.role == 'admin':
        inspections = PhoneInspection.objects.select_related('user').all()
    else:
        inspections = PhoneInspection.objects.select_related('user').filter(user=request.user)
    return render(request, 'vehicles/index.html', {'inspections': inspections})


@login_required
def upload(request):
    form = PhoneInspectionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        inspection = form.save(commit=False)
        inspection.user = request.user
        inspection.save()

        result = analyze_phone_image(inspection.image.path)
        inspection.result = result["text"]
        inspection.confidence = result["confidence"]
        inspection.price_min = result["price_min"]
        inspection.price_max = result["price_max"]
        inspection.save()
        return redirect('result', inspection.id)

    return render(request, 'vehicles/upload.html', {'form': form})


@login_required
def result(request, pk):
    inspection = get_object_or_404(PhoneInspection, id=pk)
    return render(request, 'vehicles/result.html', {'inspection': inspection})


def brand_suggestions(request):
    """Return all admin-managed brands as JSON for autocomplete."""
    q = request.GET.get('q', '').strip()
    qs = PhoneBrand.objects.all().order_by('name')
    if q:
        qs = qs.filter(name__icontains=q)
    brands = list(qs.values_list('name', flat=True))
    return JsonResponse({'brands': brands})
