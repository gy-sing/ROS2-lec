# 2022.07.17 일요일
# 7강 ROS 2 Topic

<br/> 7강 강의노트
+ https://puzzling-cashew-c4c.notion.site/ROS-2-Topic-a1bd364220dc4db9beb6d29b79dfdf71

<br/>

### Topic?
+ 앞선 `rqt_graph`에서 각 노드들 사이에 화살표는 데이터가 오고 간다는 것을 의미하며, 이를 Topic이라 지칭합니다. 정의에 따르면, Topic은 Node들 사이에 데이터(Message)가 오가는 길(Bus)의 이름입니다.
+ ROS2에서도 `Publisher`(발행자) `Subscriber`(구독자)로 나누어 송신, 수신자를 구분합니다.
그리고 이들 사이에 **Message**가 전달되며, 이 길의 이름이 **Topic**이다.
+ ![img](https://puzzling-cashew-c4c.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ffac392e2-808d-4fc4-b11a-8bb99634ded9%2Ftopic.gif?table=block&id=d5f11c00-7b5f-4272-9c88-d066e437a5c1&spaceId=5fbee23e-d9ec-4824-b2be-c8716a8602cd&userId=&cache=v2)
+ 또한 Topic은 일대 다 즉 여러 Node들로 부터 데이터를 받을 수 있고, 전송 시에도 여러 Node들에게 전송이 가능한 방식이다.
+ ![img](https://puzzling-cashew-c4c.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F07986117-5511-4298-bb91-3471882da179%2Ftopic2.gif?table=block&id=bddd4e57-a806-4c82-a11c-ac58204d2033&spaceId=5fbee23e-d9ec-4824-b2be-c8716a8602cd&userId=&cache=v2)