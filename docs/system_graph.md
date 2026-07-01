# System graph (Week 1 — teleop + simulation)

## Nodes observed 
/camera_driver
/gazebo
/robot_state_publisher
/rviz
/transform_listener_impl_621688818840
/turtlebot3_diff_drive
/turtlebot3_imu
/turtlebot3_joint_state
/turtlebot3_laserscan

## Topic list 

Published topics:
 * /camera/camera_info [sensor_msgs/msg/CameraInfo] 1 publisher
 * /camera/image_raw [sensor_msgs/msg/Image] 1 publisher
 * /clicked_point [geometry_msgs/msg/PointStamped] 1 publisher
 * /clock [rosgraph_msgs/msg/Clock] 1 publisher
 * /goal_pose [geometry_msgs/msg/PoseStamped] 1 publisher
 * /imu [sensor_msgs/msg/Imu] 1 publisher
 * /initialpose [geometry_msgs/msg/PoseWithCovarianceStamped] 1 publisher
 * /joint_states [sensor_msgs/msg/JointState] 1 publisher
 * /odom [nav_msgs/msg/Odometry] 1 publisher
 * /parameter_events [rcl_interfaces/msg/ParameterEvent] 9 publishers
 * /performance_metrics [gazebo_msgs/msg/PerformanceMetrics] 1 publisher
 * /robot_description [std_msgs/msg/String] 1 publisher
 * /rosout [rcl_interfaces/msg/Log] 10 publishers
 * /scan [sensor_msgs/msg/LaserScan] 1 publisher
 * /tf [tf2_msgs/msg/TFMessage] 2 publishers
 * /tf_static [tf2_msgs/msg/TFMessage] 1 publisher

Subscribed topics:
 * /clock [rosgraph_msgs/msg/Clock] 7 subscribers
 * /cmd_vel [geometry_msgs/msg/Twist] 1 subscriber
 * /joint_states [sensor_msgs/msg/JointState] 1 subscriber
 * /odom [nav_msgs/msg/Odometry] 1 subscriber
 * /parameter_events [rcl_interfaces/msg/ParameterEvent] 10 subscribers
 * /robot_description [std_msgs/msg/String] 1 subscriber
 * /scan [sensor_msgs/msg/LaserScan] 1 subscriber
 * /tf [tf2_msgs/msg/TFMessage] 1 subscriber
 * /tf_static [tf2_msgs/msg/TFMessage] 1 subscriber



teleop_twist_keyboard
  publishes → /cmd_vel
  subscribed by → (fill from ros2 topic info)

gazebo / robot_state_publisher / etc.
  publishes → /scan
  publishes → /odom

## Notes
- When teleop is not running, /cmd_vel has no publisher.
- RViz only visualizes; it does not publish /cmd_vel.


