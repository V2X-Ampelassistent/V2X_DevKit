#!/bin/bash
set -e

# setup ros2 environment
source "/opt/ros/$ROS_DISTRO/setup.bash" --
source /root/cohdainterfaces_ws/install/setup.bash
source /root/cohdatoros_ws/install/setup.bash

ros2 run v2x_cohdatoros GPS_publisher 

exec "$@"