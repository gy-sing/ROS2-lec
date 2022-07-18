# 2022.07.18 월요일
# 8강 과제

### 전방 물체까지 일정 거리 접근하면 자동으로 정지하는 과제 작성

```
#!/usr/bin/env/ python3

import sys

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class ParkingNode(Node):

		def __init__(self):
        super().__init__('parking_node')

        self.publisher = self.create_publisher(Twist, 'skidbot/cmd_vel', 10)

        self.subscriber = self.create_subscription(
            LaserScan, 'skidbot/scan', self.sub_callback, 10
        )
        self.subscriber  # prevent unused variable warning
        self.publisher  # prevent unused variable warning

        self.get_logger().info('==== Parking Node Started ====\n')

    def sub_callback(self, msg):
        twist_msg = Twist()
        distance_forward = msg.ranges[360]

        if distance_forward > ???:
            self.get_logger().info(f'Distance from Front Object : {distance_forward}')
						# Write profitable codes in here
        else:
            self.get_logger().info("==== Parking Done!!! ====\n")
						# Write profitable codes in here


def main(args=None):
    rclpy.init(args=args)

    parking_node = ParkingNode()

    try:
        rclpy.spin(parking_node)
    except KeyboardInterrupt:
        print("==== Server stopped cleanly ====")
    except BaseException:
        print("!! Exception in server:", file=sys.stderr)
        raise
    finally:
        # (optional - Done automatically when node is garbage collected)
        rclpy.shutdown()


if __name__ == "__main__":
    main()


```