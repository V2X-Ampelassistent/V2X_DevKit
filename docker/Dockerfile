FROM osrf/ros:foxy-desktop

SHELL ["/bin/bash", "-c"]

RUN \
    # Update
    sudo apt-get update \
    # install requirements
    && sudo apt-get install -y python3-pip vim \
    && pip3 install scapy \
    && pip3 install asn1tools \
    && pip3 install lark

# Add and build cohdainterfaces
ADD https://github.com/V2X-Ampelassistent/v2x_cohdainterfaces.git /root/cohdainterfaces_ws/src/v2x_cohdainterfaces

RUN \
    cd /root/cohdainterfaces_ws \
    && source /opt/ros/foxy/setup.bash \
    && colcon build --symlink-install \
    && source install/setup.bash

# Add and build cohdatoros
ADD https://github.com/V2X-Ampelassistent/v2x_cohdatoros.git /root/cohdatoros_ws/src/v2x_cohdatoros

RUN \
    cd /root/cohdatoros_ws \
    && source /opt/ros/foxy/setup.bash \
    && colcon build --symlink-install \
    && source install/setup.bash

# Add tools from the DevKit
ADD https://github.com/V2X-Ampelassistent/V2X_DevKit.git /root/V2X_DevKit/

RUN \
    cd \
    && echo "source /opt/ros/foxy/setup.bash" >> .bashrc \
    && echo "source /root/cohdainterfaces_ws/install/setup.bash" >> .bashrc \
    && echo "source /root/cohdatoros_ws/install/setup.bash" >> .bashrc \
    && chmod +x /root/V2X_DevKit/pcap_player/pcap_player.py

ENV PATH "/root/V2X_DevKit/pcap_player/:$PATH"