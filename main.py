from winotify import Notification, audio
import time

DesktopNotifier = Notification(app_id = "SyncInternNotification",
                     title = "Deadline",
                     msg = "Python Internship, Sync Company",
                     duration = "long",
                     icon= r"C:\Users\user\Desktop\developer\Sinc.jpg")

DesktopNotifier.set_audio(audio.LoopingAlarm2, loop=False)
DesktopNotifier.add_actions(label="Go To Website!", launch="https://www.sync.com/")
DesktopNotifier.show()