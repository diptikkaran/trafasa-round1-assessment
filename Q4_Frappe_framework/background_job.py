import time
from queue import Queue
from threading import Thread

def generate_report(report_name):
    print(f"Generating report: {report_name}")
    time.sleep(5)
    print(f"{report_name} generated successfully.")


def worker():
    while True:
        report = task_queue.get()

        if report is None:
            break

        generate_report(report)
        task_queue.task_done()


task_queue = Queue()

thread = Thread(target=worker)
thread.start()

task_queue.put("Monthly Sales Report")

task_queue.join()

task_queue.put(None)

thread.join()