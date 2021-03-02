import itertools
import threading
import sys
import time
from script_info import animation_finihsed

done = False
animate_over = animation_finihsed()

def animate(info):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break      
        sys.stdout.write('\r{0} '.format(info) + c)
        sys.stdout.flush()
        time.sleep(0.1)
    print('\n'+ animate_over, sep="")