#!/usr/bin/env python

import subprocess
import time
import os
# import pwd

def main():
    while 1:
        klipper = subprocess.Popen(['python', '/opt/printer/klipper/klippy/klippy.py', '/opt/printer/cfg/printer.cfg', '-a', '/tmp/klippy_uds'])
        if klipper.wait() == 0:
            # Exited cleanly, don't sleep for long
            time.sleep(1)
        else:
            # Something went wrong, wait a bit before trying again
            time.sleep(30)


if __name__ == '__main__':
    main()


