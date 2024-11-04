#!/usr/bin/env python3
import rclpy
import rclpy.logging
from rclpy.node import Node

class lab(Node):

    def __init__(self):
        super().__init__("lab")
        self.get_logger().info('Lab node started')
        self.create_timer(1,self.timer__callback)
        self.create_timer(0.5,self.timer_callback1)

    def timer__callback(self):
        self.get_logger().info('Hello world')
        
    
    def timer_callback1(self):
        self.get_logger().error('Salut')
        


def main(args=None):
    rclpy.init(args=args)
    node=lab()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()