#!/bin/bash
set -e

# setup ros2 environment
source "/opt/ros/$ROS_DISTRO/setup.bash" --
source /root/cohdainterfaces_ws/install/setup.bash
source /root/cohdatoros_ws/install/setup.bash

ros2 topic list

ros2 topic echo /Cohda_Signals/MAPEM

exec "$@"