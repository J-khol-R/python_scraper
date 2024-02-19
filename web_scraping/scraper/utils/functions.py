from scraper.tasks import scrape_page

def scrape_pages(pages):
    tasks = [scrape_page.delay(page_num) for page_num in pages]
    complete_data = []
    for task in tasks:
        while not task.ready():
            pass
        result = task.get()
        if result is not None:
            complete_data.extend(result)
    return complete_data

def convert_num_pages(pages):
    return [int(num) for num in pages.split(",")]

