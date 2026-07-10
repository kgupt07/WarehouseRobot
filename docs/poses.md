# Poses (map frame)

All poses use `frame_id: map`. Yaw in **radians**.

Copy the numeric values into `mission_robot/nav_mission.py` (HOME_* and SEARCH_* constants).

## Home
      x: -2.0
      y: -0.5
      z: 0.0
      qx: 0.0
      qy: 0.0
      qz: -0.0
      qw: 1.0

## SearchA
      x: 0.3
      y: 0.5
      z: 0.0
      qx: 0.0
      qy: 0.0
      qz: 0.072
      qw: 1.0

## SearchB
      x: 0.46
      y: -1.74
      z: 0.0
      x: 0.0
      y: 0.0
      z: 0.1
      w: 1.0

## How to record from RViz / AMCL

After **2D Pose Estimate** and driving to a spot (or sending a Nav2 goal):

```bash
ros2 topic echo /amcl_pose --once
```

Use `pose.pose.position.x`, `pose.pose.position.y`, and convert quaternion to yaw if needed.

Or note x, y from a successful goal click in RViz (Properties panel on goal).
