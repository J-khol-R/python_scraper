from celery import shared_task
from bs4 import BeautifulSoup
import requests
from .models import Hockey

@shared_task
def scrape_page(page_num):
    URL_BASE = f'https://www.scrapethissite.com/pages/forms/?page_num={page_num}'
    response = requests.get(URL_BASE)
    soup = BeautifulSoup(response.content, "html.parser")
    
    table = soup.find('table')
    rows = table.find_all('tr')
    
    table_data = []
    for row in rows:
        row_data = {}
        
        cols = row.find_all('td')

        for col in cols:
            
            column_name = col.get('class')[0].replace('-', '_')
            column_value = col.text

            row_data[column_name.replace('-', '_')] = column_value.strip()

        table_data.append(row_data)
    return table_data[1:]

@shared_task
def save_data(data):
    for obj in data:
        hochey_team = Hockey()
        hochey_team.name = obj['name']   
        hochey_team.year = obj['year']   
        hochey_team.wins = obj['wins']  
        hochey_team.losses = obj['losses']   
        if obj['ot_losses'] != '':
            hochey_team.ot_losses = obj['ot_losses']   
        hochey_team.win_percentage = obj['pct']   
        hochey_team.goals_for = obj['gf']   
        hochey_team.goals_against = obj['ga'] 
        if obj['diff'] != '':
            hochey_team.plus_minus = obj['diff']   
        
        hochey_team.save()