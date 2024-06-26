from django.urls import path
from .views import *

urlpatterns = [
    path('getlinks/', GetLinksView.as_view(), name="getlinks"),
    path('createupdatelink/', CreateUpdateLinkView.as_view(), name="createupdatelink"),
]