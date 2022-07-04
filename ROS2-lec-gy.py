"""

2022.07.03
lec1

+ ROS ??
> robot operating system
> 로봇 개발에 필요한 여러가지 툴 제공
> 기존에 존재하는 다양한 로봇 오픈소스  제공(시각화, 시뮬)
> 로봇 하드웨어 만들기전 다양한 실험 가능


2022.07.04
lec2

+ 우분투 부팅 usb 만들고 설치
https://ubuntu.com/tutorials/create-a-usb-stick-on-windows#10-installation-complete

+ 우분투 리눅스? 환경에 ROS 2 Foxy 설치
>
$ locale  # check for UTF-8

$ sudo apt update && sudo apt install locales
$ sudo locale-gen en_US en_US.UTF-8
$ sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
$ export LANG=en_US.UTF-8

locale  # verify settings

$ sudo apt update && sudo apt install curl gnupg2 lsb-release -y
$ sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg

$ sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
$ sudo apt update

# Desktop Install (Recommended): ROS, RViz, demos, tutorials.
$ sudo apt install ros-foxy-desktop -y
# 여기서 ros-foxy-desktop -y에 설치할 수 없다고 에러뜸..
# 우분투 다시 설치하고 해보기

# Install argcomplete (optional)
$ sudo apt install -y python3-pip
$ pip3 install -U argcomplete


+ Gazebo 11
> 이번 ROS2 강의에서 실습이 진행될 시뮬레이션
> 공식적으로 ROS를 지원하는 시뮬레이션
> 
$ sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
$ wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
$ sudo apt update

$ sudo apt install gazebo11 libgazebo11-dev -y

# Gazebo ROS 패키지들도 설치해줍니다.
$ sudo apt install ros-foxy-gazebo-ros-pkgs -y

# 설치 이후 실행을 통해 확인해 보세요!
$ gazebo
"""