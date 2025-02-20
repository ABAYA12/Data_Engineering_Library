from django.shortcuts import render, redirect, get_object_or_404
from .models import PipelineDetails
from .forms import PipelineDetailsForm

def home(request):
    return render(request, 'home.html')

def pipeline_list(request):
    pipelines = PipelineDetails.objects.all()
    return render(request, 'pipelines/list.html', {'pipelines': pipelines})

def pipeline_detail(request, pk):
    pipeline = get_object_or_404(PipelineDetails, pk=pk)
    return render(request, 'pipelines/detail.html', {'pipeline': pipeline})

def pipeline_add(request):
    if request.method == 'POST':
        form = PipelineDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pipeline_list')
    else:
        form = PipelineDetailsForm()
    return render(request, 'pipelines/add.html', {'form': form})

def pipeline_edit(request, pk):
    pipeline = get_object_or_404(PipelineDetails, pk=pk)
    if request.method == 'POST':
        form = PipelineDetailsForm(request.POST, instance=pipeline)
        if form.is_valid():
            form.save()
            return redirect('pipeline_detail', pk=pipeline.pk)
    else:
        form = PipelineDetailsForm(instance=pipeline)
    return render(request, 'pipelines/edit.html', {'form': form, 'pipeline': pipeline})

def pipeline_delete(request, pk):
    pipeline = get_object_or_404(PipelineDetails, pk=pk)
    if request.method == 'POST':
        pipeline.delete()
        return redirect('pipeline_list')
    return render(request, 'pipelines/delete.html', {'pipeline': pipeline})

def error_404(request, exception):
    return render(request, 'error.html', status=404)
