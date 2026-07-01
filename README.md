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
