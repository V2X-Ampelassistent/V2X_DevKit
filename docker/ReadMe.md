# Docker Development Environment

## How to build and run the Docker Container

First, build the Docker:
```bash
docker build -t ros_ws .  
```
If you are using a Mac with Apple Chip, use ```docker build --platform linux/arm64/v8 -t ros_ws .  ``` instead.

Second, create the Docker Container:
```bash
docker run -it -d --name ros_ws_01 ros_ws    
```

It is now recommended to attach to the Docker Container using VSCode.

## How to use the Docker Container

The Docker container will automatically set up the ROS workspace. In the ```/root``` Folder, there should be a Folder ```ROS_ws``` and a Folder ```V2X_DevKit```.

First make sure the ROS packages were installed and sourced successfuly: 
```bash
ros2 pkg list | grep v2x
```
You should now see a list containing ```v2x_cohdainterfaces``` and ```v2x_cohdatoros```.

To run tests, start the DSRC and GPS Publishers using
```bash
ros2 run v2x_cohdatoros DSRC_publisher 
```
and
```bash
ros2 run v2x_cohdatoros GPS_publisher 
```
in separate terminal windows.

After that, start to replay a ```.pcap``` file using the pcap_player included in V2X_DevKit (You will have to copy a ```.pcap``` into the Dockercontainer yourself!):
```bash
python3 /root/V2X_DevKit/pcap_player/pcap_player.py <PATH_TO_YOUR_PCAP_FILE> "127.0.0.1"
```

Open a new terminal tab and look at the published Messages using
```bash
ros2 topic echo /Cohda_Signals/MAPEM 
```
```bash
ros2 topic echo /Cohda_Signals/SPATEM
```
or
```bash
ros2 topic echo /Cohda_Signals/GPS
```