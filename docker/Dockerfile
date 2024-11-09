FROM osrf/ros:foxy-desktop

SHELL ["/bin/bash", "-c"]

RUN \
    # Update
    sudo apt-get update \
    # install requirements
    && sudo apt-get install -y python3-pip \
    && pip3 install scapy \
    && pip3 install asn1tools \
    && pip3 install lark \
    # download git stuff
    && cd \
    && git clone https://github.com/V2X-Ampelassistent/V2X_DevKit.git \
    && mkdir ROS_ws \
    && cd ROS_ws \
    && mkdir src \
    && cd src \
    && git clone https://github.com/V2X-Ampelassistent/v2x_cohdainterfaces.git \
    && git clone https://github.com/V2X-Ampelassistent/v2x_cohdatoros.git

RUN \
    cd  \
    && cd ROS_ws \
    && source /opt/ros/foxy/setup.bash \
    && colcon build --symlink-install \
    && source install/setup.bash

RUN \
    cd \
    && echo "source /opt/ros/foxy/setup.bash" >> .bashrc \
    && echo "source /root/ROS_ws/install/setup.bash" >> .bashrc