import time
from plyer import notification #pip install plyer
while True:
    title = ' 💧  Drink Water!'
    message = 'We have to drink water to stay hydrated!'
    notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                     toast=False
                        )

    time.sleep(10) #The number is in seconds.You can change it according to your wish.For 1 hour do 3600 seconds 


