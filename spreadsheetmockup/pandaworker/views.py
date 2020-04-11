from django.shortcuts import render, redirect, get_object_or_404
from .models import FileTemplate, LiveReport, ReportFlows
from .forms import FileTemplateForm, LiveReportForm
from .PandaEngine import PandaEngine
from django.conf import settings

import os
# Create your views here.

IMPORT_FILE_TYPES = ['xlsx', 'csv']


def landing(request):
    reports = FileTemplate.objects.all()
    return render(request, 'home.html', {'reports': reports})


def report_detail(request, pk):
    file_template_detail = get_object_or_404(FileTemplate, pk=pk)
    live_reports = LiveReport.objects.filter(template=file_template_detail)
    return render(request, 'details.html', {
        'file_template_detail': file_template_detail,
        'reports': live_reports,
    })


def submit_live_report(request, pk):
    live_report = get_object_or_404(LiveReport, pk=pk)
    form = LiveReportForm(instance=live_report)
    if request.method == 'POST':
        form = LiveReportForm(request.POST, request.FILES)
        if form.is_valid():
            my_engine = PandaEngine()
            live_report = form.save(commit=False)
            live_report.live_file = request.FILES['live_file']
            file_type = live_report.live_file.url.split('.')[-1]
            file_type = file_type.lower()
            live_report.live_data = my_engine.load_columns(live_report.live_file)
            if file_type not in IMPORT_FILE_TYPES:
                return render(request, 'error.html')
            live_report.save()
            return redirect('home')
        else:
            return render(request, 'error.html')
    return render(request, 'create_template.html', {'form': form})


def create_file_template(request):
    form = FileTemplateForm
    if request.method == 'POST':
        print(request.POST)
        form = FileTemplateForm(request.POST, request.FILES)
        if form.is_valid():
            my_engine = PandaEngine()
            file = form.save(commit=False)
            file.fileImport = request.FILES['fileImport']
            file_type = file.fileImport.url.split('.')[-1]
            file_type = file_type.lower()
            print(file.fileImport.url.split('/'))
            print(os.path.join(settings.BASE_DIR, 'media', file.fileImport.url.split('/')[-1]))
            file.column_labels = my_engine.load_columns(file.fileImport)
            if file_type not in IMPORT_FILE_TYPES:
                return render(request, 'error.html')
            file.save()
            live_list = []
            for i in range(0, file.live_instances):
                live_list.append(LiveReport(template=file, report_id=file.name + ":" + str(i)))
                live_list[i].save()
            return redirect('home')
        else:
            return render(request, 'error.html')
    return render(request, 'create_template.html', {'form': form})


def update_file_template(request, pk):
    template_to_update = get_object_or_404(FileTemplate, pk=pk)
    form = FileTemplateForm(instance=template_to_update)
    if request.method == 'POST':
        form = FileTemplateForm(request.POST, request.FILES)
        if form.is_valid():
            my_engine = PandaEngine()
            file = form.save(commit=False)
            file.fileImport = request.FILES['fileImport']
            file_type = file.fileImport.url.split('.')[-1]
            file_type = file_type.lower()
            file.column_labels = my_engine.load_columns(file.fileImport)
            if file_type not in IMPORT_FILE_TYPES:
                return render(request, 'error.html')
            file.save()
            return redirect('home')
        else:
            return render(request, 'error.html')
    return render(request, 'create_template.html',  {'form': form})
