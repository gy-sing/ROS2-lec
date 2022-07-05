# 2022.07.03
## Lec1
--------

### ROS ??
- robot operating system
- 로봇 개발에 필요한 여러가지 툴 제공
- 기존에 존재하는 다양한 로봇 오픈소스  제공(시각화, 시뮬)  
- 로봇 하드웨어 만들기전 다양한 실험 가능

<br/>

# 2022.07.04
# lec2
--------

## 우분투 부팅 usb 만들고 설치
+ https://ubuntu.com/tutorials/create-a-usb-stick-on-windows#10-installation-complete

<br/>

## 우분투 환경에 ROS 2 Foxy 설치  
<코드>  
- $ locale  # check for UTF-8  
- $ sudo apt update && sudo apt install locales  
- $ sudo locale-gen en_US en_US.UTF-8  
- $ sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8  
- $ export LANG=en_US.UTF-8  
- $ locale  # verify settings  
- $ sudo apt update && sudo apt install curl gnupg2 lsb-release -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg  
- $ sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'  
- $ sudo apt update  
- $ sudo apt install ros-foxy-desktop -y  
> 여기서 ros-foxy-desktop -y에 설치할 수 없다고 에러뜸..
>> 우분투 다시 설치하고 해보기
- $ sudo apt install -y python3-pip
- $ pip3 install -U argcomplete

<br/>

## Gazebo 11
- 이번 ROS2 강의에서 실습이 진행될 시뮬레이션
- 공식적으로 ROS를 지원하는 시뮬레이션  

<코드>  
- $ sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
- $ wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
- $ sudo apt update
- $ sudo apt install gazebo11 libgazebo11-dev -y
- $ sudo apt install ros-foxy-gazebo-ros-pkgs -y

<br/>

# 2022.07.04
# Lec3 lec3 윈도우에서 ROS 2 Foxy설치
+ 윈도우에서는 exe파일 하나하나 설치 눌러야 하는 귀찮음 있음  
+ 그래서 Chocolatey 프로그램 이용  

'''  
PowerShell  
$ Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
'''
