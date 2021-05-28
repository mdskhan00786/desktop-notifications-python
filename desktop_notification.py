from pynotifier import Notification
Notification(title='Checkup',
description='You have a doctors appointment on coming Thursday at 5:00 pm. ',
duration=20).send()
