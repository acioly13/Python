import schedule


def job():
    print("Hello...")


schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
