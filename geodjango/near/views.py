from django.shortcuts import render
from django.contrib.gis import geos, measure
from django.contrib.gis.db.models.functions import Distance
from .models import People
from .forms import AddressForm
from .utils import geocoder


def index(request):
    form = AddressForm()
    peoples = []
    if request.POST:
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            try:
                lng, lat = geocoder(address)
            except Exception:
                pass
            else:
                location = geos.Point(lng, lat, srid=4326)
                peoples = People.objects.annotate(distance=Distance('location', location)).filter(
                    location__distance_lte=(location, measure.D(km=50))).order_by('distance')

    return render(request, 'near/index.html', {'form': form, 'peoples': peoples})
