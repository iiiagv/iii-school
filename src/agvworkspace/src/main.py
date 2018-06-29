import agv_client as c
import rospy
import threading

if __name__ == '__main__':
    # try:
    rospy.init_node('submission_client')
    A = c.TcpClient('192.168.0.115', '1357')
    # A = c.TcpClient('127.0.0.1', 2310)
    # A.receive_mode = True
    A.bind_request()
    A.start_listen()
    A.ask_mission()
    A.is_sock_error()




    # while True:
    #     pass
    # A.listen_receive_data()
    # A.idle_timer()

    #
    # except KeyboardInterrupt:
    #     pass
