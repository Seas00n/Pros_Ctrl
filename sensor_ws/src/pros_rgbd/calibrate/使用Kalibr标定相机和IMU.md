# 使用Kalibr标定相机和IMU

## 安装Kalibr

```shell
mkdir -p ~/Downloads/kalibr_workspace/src
cd ~/Downloads/kalibr_workspace/src
git clone https://github.com/ethz-asl/Kalibr.git
cd ~/Downloads/kalibr_workspace
catkin_build -DCMAKE_UILD_TYPE=Release
source ~/Codes/kalibr_workspace/devel/setup.bash
```

## 标定相机

### 编写棋盘格的标定文件chessboard.yaml (e.g 8x11 size=20mm)

```html
target_type: 'checkerboard' #gridtype
targetCols: 11               #number of internal chessboard corners
targetRows: 8                #number of internal chessboard corners
rowSpacingMeters: 0.02       #size of one chessboard square [m]
colSpacingMeters: 0.02       #size of one chessboard square [m]

```

### 启动相机(OAK)

```
roslaunch depthai_examples stereo_inertial_node.launch enableRviz:=false depth_aligned:=false stereo_fps:=4
```

### 录制rosbag存储双目相机消息

`/stereo_inertial_publisher/left/image_rect`

`/stereo_inertial_publisher/right/image_rect`

到`stereo.bag`文件中

```
rosbag record /stereo_inertial_publisher/left/image_rect /stereo_inertial_publisher/right/image_rect -O stereo.bag
```

### 标定

```shell
rosrun kalibr kalibr_calibrate_cameras --bags stereo.bag --topics /stereo_inertial_publisher/left/image_rect /stereo_inertial_publisher/right/image_rect --models pinhole-radtan --target chessboard.yaml 

```

