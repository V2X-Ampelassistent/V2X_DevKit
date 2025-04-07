#!/bin/bash
set -e

# setup ros2 environment
source "/opt/ros/$ROS_DISTRO/setup.bash" --
source /root/cohdainterfaces_ws/install/setup.bash
source /root/cohdatoros_ws/install/setup.bash

# broadcast recording.pcap to docker network
python3 /root/V2X_DevKit/pcap_player/pcap_player.py /root/V2X_DevKit/docker/pcap_recordings/recording.pcap "172.30.255.255"

exec "$@"