## Mission Overview

This is warehouse simulation robot, designed to execute the following mission:

Map the warehouse [the first time using SLAM] or load prebuilt Map → Localize on the map → navigate to a given search pose → detect target → report/publish target found message→ return home.

## Environment and robot specifications

This is a project built in simulation, with gazebo as the physics engine and visualized in RViz.

Built in wsl (Ubuntu 22.04)

Graphics using WSLg

robotics: ROS2 Humble

Robot model: TurtleBot3_MODEL=waffle_pi → for LiDar and camera

## Software architecture

Mission Node[written from scratch]

SLAM [Slam toolbox]

Localization [AMCL]

Navigation [Nav2] (think → path to take to get to the target physical location)

Target marker detection [ArUco] (think → what the camera should look for once at location)

## Repo Layout

docs/system_graph.md: data flow documentation

docs/poses.md: search locations

src/mission_robot: mission node/other nodes

maps/: saved occupancy grids (`.yaml` + `.pgm`)

## Launch cheatsheet

Run in **every** terminal before launching:

```bash
export TURTLEBOT3_MODEL=waffle_pi
source /opt/ros/humble/setup.bash
```

### Navigation (Week 3 — Gazebo + Nav2)

**Terminal 1 — Gazebo + robot**

```bash
export TURTLEBOT3_MODEL=waffle_pi
source /opt/ros/humble/setup.bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Wait until the robot is visible. If the world loads without a robot, spawn manually:

```bash
ros2 run gazebo_ros spawn_entity.py \
  -entity turtlebot3_waffle_pi \
  -file $(ros2 pkg prefix turtlebot3_gazebo)/share/turtlebot3_gazebo/models/turtlebot3_waffle_pi/model.sdf \
  -x -2.0 -y -0.5 -z 0.01
```

**Terminal 2 — map + AMCL + Nav2**

SLAM-built map:

```bash
export TURTLEBOT3_MODEL=waffle_pi
source /opt/ros/humble/setup.bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py \
  use_sim_time:=true \
  map:=/mnt/c/Users/007kh/OneDrive/Research/ROS_robot/maps/warehouse_map.yaml
```

Demo map (fallback):

```bash
ros2 launch turtlebot3_navigation2 navigation2.launch.py \
  use_sim_time:=true \
  map:=/mnt/c/Users/007kh/OneDrive/Research/ROS_robot/maps/map.yaml
```

RViz may open automatically. If not:

```bash
rviz2 -d $(ros2 pkg prefix turtlebot3_navigation2)/share/turtlebot3_navigation2/rviz/tb3_navigation2.rviz
```

**RViz after launch:** Fixed Frame = `map` → **2D Pose Estimate** → **Nav2 Goal**

If the `map` frame is missing before initial pose:

```bash
ros2 topic pub --once /initialpose geometry_msgs/msg/PoseWithCovarianceStamped \
"{header: {frame_id: 'map'}, pose: {pose: {position: {x: -2.0, y: -0.5, z: 0.0}, orientation: {w: 1.0}}}}"
```

### SLAM (mapping — do not run with navigation at the same time)

With Gazebo running in Terminal 1:

```bash
source /opt/ros/humble/setup.bash
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=true
```

Teleop (optional):

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

RViz (manual):

```bash
rviz2
```

Set Fixed Frame = `map`, add Map (`/map`, QoS: Transient Local), LaserScan (`/scan`), TF.

Save map:

```bash
mkdir -p /mnt/c/Users/007kh/OneDrive/Research/ROS_robot/maps
ros2 run nav2_map_server map_saver_cli -f /mnt/c/Users/007kh/OneDrive/Research/ROS_robot/maps/warehouse_map
```

### Quick reference

| Goal | Terminals |
|------|-----------|
| Nav2 / autonomous nav | Gazebo → `navigation2.launch.py` → RViz initial pose |
| SLAM / build map | Gazebo → `slam_toolbox` → teleop → RViz |
| Manual drive only | Gazebo → teleop |

**Notes**

- `navigation2.launch.py` does not start Gazebo — launch sim first.
- Always pass `use_sim_time:=true` when using Gazebo.
- `nav2 class docking could not be loaded` is optional; safe to ignore for now.
