import rclpy
from rclpy.node import Node
from tf2_msgs.msg import TFMessage
from nav_msgs.msg import Odometry
from std_msgs.msg import String
import time
import sys
import termios
import tty
import threading
import select


class pub(Node):
    def __init__(self):
        super().__init__('pub_test')

        print('f')
        self.pub = self.create_publisher(String,'/command',10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def get_key(self):
        key = input()
        return key
    
    def timer_callback(self):
        key = self.get_key()
        msg = String()
        msg.data = key

        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    image_subscriber = pub()

    try:
        rclpy.spin(image_subscriber)
    except:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()