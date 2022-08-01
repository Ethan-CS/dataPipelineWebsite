from django.contrib import admin

# Register your models here.
from dataPipelineWebsite.entry.forms import DataEntryForm
from dataPipelineWebsite.entry.models import Data

admin.site.register(Data)
