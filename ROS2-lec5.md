# 2022.07.16 토요일
# 5강 ROS 2 Node, Package와 기본 커멘드 라인 

<br/> 5강 강의노트
+ https://puzzling-cashew-c4c.notion.site/ROS-2-Node-Package-9093c602cb5c466b94071eb096375b54

<br/> 

### Node 란?
+ 로봇 개발을 하기 위해서는 로봇을 구성하는 여러 센서들, 그리고 이들 센서 데이터를 통해 지속적으로 판단하고 동작해야 하는 시스템. node들 사이에 서로 데이터를 주고 받는 구조.

+ ![img](https://puzzling-cashew-c4c.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe35707d3-d7ea-4f0d-8923-a7f6a2f908e5%2FNodes-TopicandService.gif?table=block&id=16694956-a4f6-4fb1-a787-a60226770071&spaceId=5fbee23e-d9ec-4824-b2be-c8716a8602cd&userId=&cache=v2)

+ turtlesim node를 실행하면 파란 창이나오고 거북이가 나오고 각 노드가 실행된것

<br/>

### Rqt_Graph
+ 데이터가 어디 노드로 보내고 있는지 실시간으로 편하게 볼 수 있음.
+ 설치코드
```
# rqt 관련 패키지 설치
$ sudo apt install ros-foxy-rqt*
# 실행
$ rqt_graph
 ```
<br/>

 ### Package란?
 + **파일 관점**에서는 관련된 라이브러리, 모델링 파일들, 설정 파일들을 모아둔 폴더로 생각할 수 있다.
+ **기능 관점**에서는 시뮬레이션, 하드웨어 관련, 모델링, 원격 조종 등으로 분리시킨 모듈로 생각할 수 있다.
+ 더불어 `colcon build`가 수행되는 **빌드의 단위** 이다.

<br/>

## 정리
+ 이번 강의에서 미리 만들어둔 패키지를 사용하지만 나중에 직접 패키지 만들어 보기
+ ament를 사용하여 패키지를 만드는 방법
```
$ ros2 pkg create --build-type ament_cmake  <패키지이름> --dependencies rclcpp <종속성> 
$ ros2 pkg create --build-type ament_python <패키지이름> --dependencies rclpy <종속성> 
```