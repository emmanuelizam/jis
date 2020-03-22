from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
from .forms import *

# Create your views here.

def caseCreateView(request):
    form = CaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CaseForm()
    
    context = {
        'form':form
    }

    return render(request, 'casedetail_form.html', context=context)

def caseProceedingCreateView(request):
    form = CaseProceedingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CaseProceedingForm()
    
    context = {
        'form':form
    }

    return render(request, 'casedetail_form.html', context=context)

def caseAdjournmentCreateView(request):
    form = CaseAdjournmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CaseAdjournmentForm()
    
    context = {
        'form':form
    }

    return render(request, 'casedetail_form.html', context=context)

def caseJudgementSummaryView():
    pass

def queryPendingCasesView():
    pass

def queryResolvedCasesView():
    pass

def queryCasesByDateView():
    pass

def queryCasesByCINView():
    pass

'''
def createCourtCase():
    pass

def createCourtCase():
    pass

def createCourtCase():
    pass
'''