from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from auto_updater import get_data

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_data.get_price, 'interval', seconds=5)
    scheduler.start()