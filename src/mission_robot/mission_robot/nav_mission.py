"""Action client: search pose -> wait -> home pose via Nav2 NavigateToPose."""

import time
from math import cos, sin

import rclpy
from action_msgs.msg import GoalStatus
from geometry_msgs.msg import PoseStamped, Quaternion
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
from rclpy.node import Node

# --- Poses (map frame) — Hardcoded, copied over from poses.md ---
HOME_X = -2.0
HOME_Y = 0.5
HOME_Z = 0.0
HOME_QX = 0.0
HOME_QY = 0.0
HOME_QZ = -0.0
HOME_QW = 1.0

SEARCH_X = 0.3
SEARCH_Y = 0.5
SEARCH_Z = 0.0
SEARCH_QX = 0.0
SEARCH_QY = 0.0
SEARCH_QZ = 0.0
SEARCH_QW = 1.0

MAP_FRAME = 'map'
WAIT_AT_SEARCH_SEC = 5.0

def make_pose_stamped(node, x, y, z, qx, qy, qz, qw):
    pose = PoseStamped()
    pose.header.frame_id = MAP_FRAME
    pose.header.stamp = node.get_clock().now().to_msg()
    
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = z
    
    pose.pose.orientation.x = qx
    pose.pose.orientation.y = qy
    pose.pose.orientation.z = qz
    pose.pose.orientation.w = qw

    return pose

class NavMissionNode(Node):

    def __init__(self):
        super().__init__('nav_mission_client')
        self._action_client = ActionClient(self, NavigateToPose , 'navigate_to_pose')

    def send_goal(self, pose: PoseStamped):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = pose

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(goal_msg)

        rclpy.spin_until_future_complete(self, self._send_goal_future)

        goal_handle = self._send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return False

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        
        rclpy.spin_until_future_complete(self, self._get_result_future)

        result = self._get_result_future.result()

        if result.status == GoalStatus.STATUS_SUCCEEDED:
            return True
        else:
            self.get_logger().error(f'Goal failed, status={result.status}')
            return False

    def run_mission(self):
        search_target = make_pose_stamped(self, SEARCH_X, SEARCH_Y, SEARCH_Z, SEARCH_QX, SEARCH_QY, SEARCH_QZ, SEARCH_QW)
        
        search_success = self.send_goal(search_target)
        if not search_success:
            self.get_logger().info('goal failed to reach search target')
            return
        else:
            self.get_logger().info('goal successfully reached search target')

        time.sleep(WAIT_AT_SEARCH_SEC)

        home_target = make_pose_stamped(self, HOME_X, HOME_Y, HOME_Z, HOME_QX, HOME_QY, HOME_QZ, HOME_QW)

        home_success = self.send_goal(home_target)
        if not home_success:
            self.get_logger().info('home navigation failed')
            return
        else:
            self.get_logger().info('home navigation successful')

        return




def main():
    rclpy.init()
    node = NavMissionNode()
    try:
        node.run_mission()
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
