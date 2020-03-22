from django.urls import include, path
from .views import *

"""jis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

app_name = 'jis_app'

urlpatterns = [
    path('case_create_form', caseCreateView, name='case_create_form'),
    path('case_proceeding_create_form', caseProceedingCreateView, name='case_proceeding_create_form'),
    path('case_adjournment_create_form', caseAdjournmentCreateView, name='case_adjournment_create_form'),
]