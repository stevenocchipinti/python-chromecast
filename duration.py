from __future__ import print_function
import pychromecast
import time
import sys

print("Searching for ChromeCasts... ", end="")
sys.stdout.flush()
casts = pychromecast.get_chromecasts()
print("%s found" % len(casts))

if len(casts) == 0:
  sys.exit(1)
cast = casts[0]

print("Connecting to '%s'... " % cast.name, end="")
cast.wait()
time.sleep(1)
status = cast.media_controller.status
print("connected (status=%s)" % status.player_state)

if status.player_state != "PLAYING":
  sys.exit(1)
else:
  print("%.2f%%" % (status.current_time / status.duration * 100))
