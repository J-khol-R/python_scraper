from scraper.tasks import scrape_page

def scrape_pages(pages):
    tareas = [scrape_page.delay(page_num) for page_num in pages]
    datos_completos = []
    for tarea in tareas:
        while not tarea.ready():
            pass
        resultado = tarea.get()
        if resultado is not None:
            datos_completos.extend(resultado)
    return datos_completos

def convert_num_pages(pages):
    return [int(numero) for numero in pages.split(",")]

