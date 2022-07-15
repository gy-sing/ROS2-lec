# 2022.07.16 토요일
# 4강 Gazebo Simulation

<br/> 2강 강의노트
+ https://puzzling-cashew-c4c.notion.site/Gazebo-Simulation-a005ee3fa0cb45f19f86cc5d89ca4f1f


### 환경구성

```
# 폴더 이름을 직접 타이핑하지 마시고 Tab키를 적극 사용하시기를 권장합니다.
$ cd gcamp_ros2_ws/src
$ git clone https://github.com/Road-Balance/gcamp_ros2_basic.git

$ cd ~/gcamp_ros2_ws/
# 프로젝트 패키지 빌드
$ cbp gcamp_gazebo
```

<br/>

### Gazebo 설정 파일에 사용 모델 경로 추가
```
$ gedit ~/.gazebo/gui.ini

# 다음 부분 수정
[model_paths]
filenames=/home/<user_name>/gcamp_ws/src/gcamp_ros_basic/GazeboFiles/models

ex) /home/swimming/gcamp_ros2_ws/src/gcamp_ros2_basic/gcamp_gazebo/GazeboFiles/models
```

### 가즈보 실행 
```
$ cd ~/gcamp_ros2_ws/
$ rosfoxy
$ ros2 launch gcamp_gazebo gcamp_world.launch.py
```
<br/>

## 정리
+ 현재 폴더의 위치를 알아내는 방법 ⇒ pwd 사용
+ tab키 자동완성? 잘 활용