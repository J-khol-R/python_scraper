import os

with open('/app/scraper/num_workers.txt', 'r') as f:
    num_workers = f.read().strip()

os.system(f'celery -A web_scraping worker --loglevel=info --concurrency={num_workers}')