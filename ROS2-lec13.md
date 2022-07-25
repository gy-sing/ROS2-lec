# 2022.07.25 월요일
# 13강 Service 프로그래밍 - python

<br/> 8강 강의노트
+ https://puzzling-cashew-c4c.notion.site/Service-python-f3a43eda3a4745fdb5f1dc1774b75e45

<br/>

### Service Client 작성
+ Class 내부
```
class SpawnRobot(Node):

    def __init__(self):
        super().__init__("gazebo_model_spawner")
				# Service Client는 다음과 같이 생성합니다. 하단에 보충 설명을 더하겠습니다. 
        self.client = self.create_client(SpawnEntity, "/spawn_entity")

				# Server가 없으면 아무리 request를 해도 대답이 없을 것입니다.
				# 이를 방지하기 위해 최대로 Server를 기다릴 시간을 지정합니다.
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().error("service not available, waiting again...")

				# 등장시킬 로봇의 외형을 담은 파일에 접근합니다.
        # Get urdf path
        self.urdf_file_path = os.path.join(
            get_package_share_directory("gcamp_gazebo"),
            "urdf",
            "skidbot2.urdf",
        )

				# request를 선업합니다.
        self.req = SpawnEntity.Request()
```

<br/>

### future
+ future는 특정 작업에 대한 약속을 받아내는 것.
```
    future = robot_spawn_node.send_req()

    rclpy.spin_until_future_complete(robot_spawn_node, future)
```

+ robot_spawn_node.send_req()는 반드시 끝날 것을 보장(=약속=promise)하니, 그동안 robot_spawn_node를 spin시키고 있을게~ 라는  뜻이 됩니다.


![img](https://puzzling-cashew-c4c.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fd297a106-65b6-4d10-9ed3-aff85c05791a%2Fservice1.gif?table=block&id=bb84bf37-6ac9-45b5-8cef-08ea11278ffa&spaceId=5fbee23e-d9ec-4824-b2be-c8716a8602cd&userId=&cache=v2)
+ 1 Servic를 생성하고
+ 2 request를 받아 
+ 3 그에 대응하는 작업을 수행한 뒤 
+ 4 response를 되돌려줍니다.