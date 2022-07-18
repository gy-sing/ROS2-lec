# 2022.07.18 월요일
# 8강 Topic 프로그래밍 - python

<br/> 8강 강의노트
+ https://puzzling-cashew-c4c.notion.site/Topic-python-abf265c0af7b45c38264914d164d7349

<br/>

### Publisher Node 코드 분석

```
def main(args=None):
		# ROS Node가 동작하기 위해서는 현 상태에 대한 정보를 알아내는 등 초기 작업이 필요합니다.
    rclpy.init(args=args)
		
		# 아직 살펴보지 않았지만, 새로운 Node에 해당하는 무언가를 만들었습니다.
    cmd_vel_publisher = CmdVelPublisher()

		# rclpy에게 이 Node를 반복해서 실행 (=spin) 하라고 전달하고 있습니다.
    rclpy.spin(cmd_vel_publisher)

		# Node의 실행 중 여러 상태들에 대한 로그, 잘 실행되고 있는지를 보고 싶을 것입니다. 
		# 이 때 사용되는 함수입니다.
    cmd_vel_publisher.get_logger().info('\n==== Stop Publishing ====')

		# 사용을 마친 생성물은 종료됩니다.
    cmd_vel_publisher.destroy_node()

		# 마찬가지로 사용을 마친 Node는 종료됩니다.
    rclpy.shutdown()
```
```
def main(args=None):
    rclpy.init(args=args)

    cmd_vel_publisher = CmdVelPublisher()
		
		# ROS2에서 시간을 다루기 위해 아래와 같은 방식을 사용합니다.
		# 기본적으로 CPU clock을 사용하기 때문에 절대 시간과 정확히 일치한다는 보장은 없습니다.
    start_time = cmd_vel_publisher.get_clock().now().to_msg().sec
    clock_now  = start_time
		time_delta = 0

		# 5초 동안만 실행하기 위한 로직이 추가되었습니다.
    while (clock_now - start_time) < 5:
				# 단 한 번만 spin시키기 위해 spin_once가 사용되었습니다.
        rclpy.spin_once(cmd_vel_publisher)
        clock_now = cmd_vel_publisher.get_clock().now().to_msg().sec

        time_delta = clock_now - start_time
        print(f'{time_delta} seconds passed')

		# 나머지는 이전 예제와 동일합니다.
    cmd_vel_publisher.stop_robot()

    cmd_vel_publisher.get_logger().info('\n==== Stop Publishing ====')
    cmd_vel_publisher.destroy_node()

    rclpy.shutdown()
```

<br/>

### Class
+ ROS2의 모든 개발은 Class 형태로 개발을 추천하고 있습니다. 더불어 모든 Class는 **Node**를 기본적으로 상속받아야 합니다. 이 Node안에 node 동작에 필수적인 기능들이 모두 구현되어 있습니다. *(Composition)*
+ 상속이란, 마치 유산을 상속하듯이 **상위 Class가 구현해 둔 것을 추가 개발 없이 동일하게 사용할 수 있다**는 것과 더불어, 상속받은 Class **자신만의 기능을 추가할 수 있다**는 뜻입니다.

