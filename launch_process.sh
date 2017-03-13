#!/bin/bash
# --------- User Settings ---------
PROCESS2RUN="sudo python3 /home/pi/loader-controller/loader-controller.py"
MONITOR_SCRIPT="/home/pi/rpi-process-monitor/monitor_process.py"
# ---------------------------------
nohup $PROCESS2RUN &
VAR=`pgrep -f "$PROCESS2RUN"`
echo $VAR
nohup python $MONITOR_SCRIPT $VAR &
