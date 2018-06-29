#!/usr/bin/env python3
import rospy,ast
import actionlib

from geometry_msgs.msg import PoseWithCovarianceStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from agvcode.srv import AgvNav, AgvNavResponse, AgvNavRequest

# TODO
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path


class PathSetall(Path):
    def __init__(self, pathAll):
        super().__init__()
        self.header.seq = 1
        self.header.stamp = rospy.Time.now()
        self.header.frame_id = 'map'
        self.poses = pathAll


class PoseStampedSetall(PoseStamped):
    def __init__(self, positionx, positiony):
        super().__init__()
        self.header.stamp = rospy.Time.now()
        self.header.frame_id = 'map'

        self.pose.position.x = positionx
        self.pose.position.y = positiony
        self.pose.position.z = 0

        self.pose.orientation.x = 0
        self.pose.orientation.y = 0
        self.pose.orientation.z = 0
        self.pose.orientation.w = 1


class InitialposeSetall(PoseWithCovarianceStamped):
    def __init__(self, init_coordinate):
        super().__init__()
        self.header.seq = 1
        self.header.stamp = rospy.Time.now()
        self.header.frame_id = 'map'

        self.pose.pose.position.x = init_coordinate[0]
        self.pose.pose.position.y = init_coordinate[1]
        self.pose.pose.position.z = 0

        self.pose.pose.orientation.x = 0
        self.pose.pose.orientation.y = 0
        self.pose.pose.orientation.z = 0
        self.pose.pose.orientation.w = 1


def goal_pose(pose):
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0]
    goal_pose.target_pose.pose.position.y = pose[1]
    goal_pose.target_pose.pose.position.z = 0
    goal_pose.target_pose.pose.orientation.x = 0
    goal_pose.target_pose.pose.orientation.y = 0
    goal_pose.target_pose.pose.orientation.z = 0
    goal_pose.target_pose.pose.orientation.w = 1
    return goal_pose


def go_forward(request):
    request = ast.literal_eval(request.coordinate)
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    pub = rospy.Publisher('initialpose', PoseWithCovarianceStamped, queue_size=1000, latch=True)
    initialpose = InitialposeSetall(request[0])
    pub.publish(initialpose)

    # TODO
    # pub123 = rospy.Publisher('/move_base/NavfnROS/plan', Path, queue_size=1000, latch=True)
    pub123 = rospy.Publisher('/plan123', Path, queue_size=1000, latch=True)
    path = list()
    for i in request:
        x0, y0 = i
        path.append(PoseStampedSetall(x0, y0))
    my_Goad = PathSetall(path)
    pub123.publish(my_Goad)
    ##

    for pose in request:
        goal = goal_pose(pose)
        client.send_goal(goal)
        client.wait_for_result()

    return AgvNavResponse(True, "none")


if __name__ == '__main__':
    rospy.init_node('agvontheway_serv')
    service = rospy.Service('agv_nav', AgvNav, go_forward)
    rospy.spin()



