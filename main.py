import time
from plyer import notification
while True:
    title = ' 💧  Drin   k Water!'
    message = 'We have to drink water to stay hydrated!'
    notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                     toast=False
                        )

    time.sleep(10)


