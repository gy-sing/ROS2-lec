# 2022.07.15 금요일
# 2강 Linux20.04 - ROS 2 Foxy 설치
+ 우분투 재설치하다가 디스크 지우기 눌러서 윈도우까지 날라감... 내자료...아니.. 리눅스 설치된 파티션만 지워야지 왜그랬어
+ 백업 잘하자

<br/> 2강 강의노트
+ https://puzzling-cashew-c4c.notion.site/ROS-2-Foxy-Linux20-04-58f0c6f2537e498eb8fe163ad1f13ce5

<br/>

## ROS 2 Foxy 설치
```
$ locale  # check for UTF-8
$ sudo apt update && sudo apt install locales
$ sudo locale-gen en_US en_US.UTF-8
$ sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
$ export LANG=en_US.UTF-8

locale  # verify settings

$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F42ED6FBAB17C654
$ sudo apt update && sudo apt install curl gnupg2 lsb-release -y
$ sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg

$ sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
$ sudo apt update

# Desktop Install (Recommended): ROS, RViz, demos, tutorials.
$ sudo apt install ros-foxy-desktop -y

# Install argcomplete (optional)
$ sudo apt install -y python3-pip
$ pip3 install -U argcomplete
```

## Gazebo 11 설치
```
$ sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
$ wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
$ sudo apt update

$ sudo apt install gazebo11 libgazebo11-dev -y

# Gazebo ROS 패키지들도 설치해줍니다.
$ sudo apt install ros-foxy-gazebo-ros-pkgs -y

# 설치 이후 실행을 통해 확인해 보세요!
$ gazebo
```

