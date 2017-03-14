#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import psutil
import time
import sys
import platform

from ISStreamer.Streamer import Streamer

from config import ACCESS_KEY


# --------- User Settings ---------
hostname = platform.node()

# Initial State settings
BUCKET_NAME = ":computer: TPI Loader Controllers"
BUCKET_KEY = "pr1208"
PROCESS_NAME = hostname
# Set the time between checks
MINUTES_BETWEEN_READS = 15
# ---------------------------------


def main():
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " <pid>")
        exit()
    pid = sys.argv[1]

    streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY,
                        access_key=ACCESS_KEY)
    if not psutil.pid_exists(int(pid)):
        print("Error: That process doesn't exist! Exiting ...")
        exit()
    else:
        streamer.log(PROCESS_NAME, "Running")
        streamer.flush()

    while True:
        if not psutil.pid_exists(int(pid)):
            streamer.log(PROCESS_NAME, "Exited")
            streamer.flush()
            exit()
        else:
            streamer.log(PROCESS_NAME, "Running")
            streamer.flush()
        time.sleep(60*MINUTES_BETWEEN_READS)


if __name__ == "__main__":
    main()
