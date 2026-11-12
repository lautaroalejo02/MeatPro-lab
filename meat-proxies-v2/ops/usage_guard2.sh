#!/usr/bin/env bash
# Usage guard v2: kills the pipeline by its exact Windows PID (tree) when Claude usage >= LIMIT.
# Args: PIDFILE LIMIT [INTERVAL_S]   Log: /tmp/ff/usage_guard.log
PIDFILE=$1; LIMIT=$2; INTERVAL=${3:-300}; LOG=/tmp/ff/usage_guard.log
WINPID=$(tr -d '\r\n ' < "$PIDFILE")
alive() { tasklist //FI "PID eq $WINPID" //NH 2>/dev/null | grep -q " $WINPID "; }
while true; do
  if ! alive; then echo "$(date +%H:%M) DONE pipeline process $WINPID ended" >> $LOG; exit 0; fi
  read h w < <(/tmp/ff/claude_usage.sh)
  echo "$(date +%H:%M) five_hour=$h seven_day=$w" >> $LOG
  if [ "$h" != "NA" ] && python -c "import sys; sys.exit(0 if max(float('$h'),float('$w'))>=float('$LIMIT') else 1)"; then
    taskkill //T //F //PID $WINPID > /dev/null 2>&1
    sleep 2
    if alive; then echo "$(date +%H:%M) PAUSE FAILED: pid $WINPID still alive" >> $LOG; exit 2; fi
    echo "$(date +%H:%M) PAUSED: killed pid $WINPID (five_hour=$h seven_day=$w)" >> $LOG
    exit 0
  fi
  sleep $INTERVAL
done
