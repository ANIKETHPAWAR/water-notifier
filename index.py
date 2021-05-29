import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="**PLEASE DRINK WATER NOW",
        message="4 LITRES OF WATER IS NECESSARY FOR YOU ",
        timeout=10
    )
time.sleep(60*60)