import schedule
import time
import subprocess
def job():
    subprocess.Popen('scrapy crawl huilv')

schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)