from django.shortcuts import render

from dataPipelineWebsite.entry.models import Data


def index(request):
    num_entries = Data.objects.filter(name='name').count()
    return render(request, 'index.html', context={'num_entries': num_entries})
