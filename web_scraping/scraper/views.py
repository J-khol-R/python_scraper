from django.shortcuts import render
from .utils.functions import convert_num_pages
from .utils.functions import scrape_pages
from .tasks import save_data
from .models import Hockey
import os

def index(request):
    data = None
    message = None
    
    if request.method == 'POST':
        pagesText = request.POST.get('num_pages')
        list_pages = convert_num_pages(pagesText)
        
        workers = request.POST.get('num_workers')
        if workers == None or workers == "0" or "-" in workers:
            workers = 1
        project_root = os.path.dirname(os.path.abspath(__file__))  
        file_path = os.path.join(project_root, 'num_workers.txt')  
        with open(file_path, 'w') as f:
            f.write(workers)
        
        data = scrape_pages(list_pages)
        save_data.delay(data)
        
        message = "Saved data, you can go to the results view to see the information and filter it to your liking c:"
        

    return render(request, 'index.html', {'message': message})

def results(request):
    teams = Hockey.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        wins = request.POST.get('wins')
        losses = request.POST.get('losses')

        if name:
            teams = teams.filter(name__icontains=name)
        if year:
            teams = teams.filter(year=year)
        if wins:
            teams = teams.filter(wins=wins)
        if losses:
            teams = teams.filter(losses=losses)

    return render(request, 'table.html', {'teams': teams})