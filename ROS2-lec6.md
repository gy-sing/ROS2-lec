# 2022.07.16 토요일
# 6강 ROS 2 Node, Package와 기본 커멘드 라인 

<br/> 2강 강의노트
+ https://puzzling-cashew-c4c.notion.site/ROS-2-Launch-launch-file-55c2125808ef4b64bade278852b37d6e

<br/>

### launch file
+ `python`문법으로 되어있는 `<>.launch.py` 형식의 파일
+ 개별적으로 실행되는 명령어를 하나의 런치 파일로 통합 실행 가능
+ 방식으로는 Node방식과 ExecuteProcess방식이 있다. (우리는 node방식을 많이 사용할 예정)

<br/> 

### argument와 parameter ??
+ https://github.com/rnanosaur/nanosaur_robot/blob/6aaf41d00c2f95d393d942d22e35c0a3c60fdf66/nanosaur_camera/param/camera.yml
+ 위와 같은 매개변수들(사용 디바이스의 usb port이름, 로봇 바퀴 사이의 거리, 각종 제어 변수들)을 `.yaml` 파일로 정리하고, lauch 시 코드에 import 할 수 있다.
+ 이렇게 잘 모듈화해두면, 추가 코드 수정 없이, 손쉽게 다른 프로젝트에서도 사용할 수 있을 것입니다.
+ `.yaml`파일은 주로 `param` 또는 `config`폴더에서 찾을 수 있음.

<br/>

## 정리
+ `ros2 launch gcamp_gazebo gcamp_world.launch.py` 명령어로 한줄인데 런치 파일 열어보면 가즈보실행, 로봇등장, rviz실행 노드 3개 명령어가 들어 있음.