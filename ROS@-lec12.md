# 2022.07.25 월요일
# 12강 ROS 2 Service

<br/> 8강 강의노트
+ https://puzzling-cashew-c4c.notion.site/ROS-2-Service-4f3ae91a0f914b7faa8c00172baa3612

<br/>

### ROS 2 Service 개념
+ ![img](https://puzzling-cashew-c4c.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fd297a106-65b6-4d10-9ed3-aff85c05791a%2Fservice1.gif?table=block&id=eb14bfcb-1c98-4a8a-a05c-056ddcc11bdf&spaceId=5fbee23e-d9ec-4824-b2be-c8716a8602cd&userId=&cache=v2)
+ 그림과 같이 클라이언트 노드가 서버 노드로 request를 주면, 해당 request에 대응하는 적절한 response가 다시 client에게 전달된다.
+ 하나의 Service Server에는 여러 Client Node가 request 할 수 있지만, Server는 동시에 여러 request를 처리하지는 못한다.

<br/>

### Topic Service 차이
+ Topic publish를 하면 여러 Node가 Subscribe 가능합니다. 반면, Service는 request가 온 대상에게만 response를 줍니다. ⇒ 1:1
+ Service Server는 동시에 여러 request를 처리할 수 없습니다. 현재 작업중인 request가 처리될 때 까지 다른 request는 기다리고 있어야 합니다.
+ Topic은 대부분 지속적으로 publish를 진행하는 반면, Service는 1회성에 가깝습니다.

분명한 요청의 주체가 있으며, 빠르게 동작이 완료되는 경우
 ⇒  **Service**
 
 <br/>

불특정한 node가 Subscribe의 대상이 되며, 지속적으로 데이터의 송수신이 일어나는 경우
  ⇒ **Topic**

<br/>

### ROS 2 Service Commands
+ Service는 srv라는 타입을 사용합니다. 
+ 전체 service list는 다음과 같이 확인
```
$ ros2 service list

#서비스가 어떤 타입을 사용하는지 검색
$ ros2 service type /spawn_entity 
```
