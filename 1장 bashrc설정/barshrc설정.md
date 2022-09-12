# 2022.9.12 월요일
# .bashrc 파일 설정

## 파일 편집기(sublime text) 다운로드 https://www.sublimetext.com/download
 + wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg
+ echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
+ sudo apt-get update
+ sudo apt-get install sublime-text
+ 위 명령어를 터미널에 한줄 한줄 입력해서 설치
+ 실행명령어 : $ subl .
+ [이미지](./git/../../사진/1.png)

## bashrc 파일 열기
+ 터미널이 실행될 때마다 자동으로 실행되는 코드 설정 파일.
+ $ subl ~/.bashrc
+ [이미지](./사진/../../사진/2.png)
+ Alias설정 문법 : $ alias command_name="values"

### ros2 foxy 추천 bashrc명령어 (맨 마지막줄에 추가하면 됨)
```
echo "ROS2 foxy is activated!"
source /opt/ros/foxy/setup.bash
source ~/robot_ws/install/local_setup.bash

source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
source /usr/share/vcstool-completion/vcs.bash
source /usr/share/colcon_cd/function/colcon_cd.sh
export _colcon_cd_root=~/robot_ws

export ROS_DOMAIN_ID=7
export ROS_NAMESPACE=robot1

export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
# export RMW_IMPLEMENTATION=rmw_connext_cpp
# export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
# export RMW_IMPLEMENTATION=rmw_gurumdds_cpp

# export RCUTILS_CONSOLE_OUTPUT_FORMAT='[{severity} {time}] [{name}]: {message} ({function_name}() at {file_name}:{line_number})'
export RCUTILS_CONSOLE_OUTPUT_FORMAT='[{severity}]: {message}'
export RCUTILS_COLORIZED_OUTPUT=1
export RCUTILS_LOGGING_USE_STDOUT=0
export RCUTILS_LOGGING_BUFFERED_STREAM=1

alias sb="source ~/.bashrc; echo \"bashrc is loaded.\""
alias cw='cd ~/robot_ws'
alias cs='cd ~/robot_ws/src'
alias ccd='colcon_cd'

alias cb='cd ~/robot_ws && colcon build --symlink-install'
alias cbs='colcon build --symlink-install'
alias cbp='colcon build --symlink-install --packages-select'
alias cbu='colcon build --symlink-install --packages-up-to'
alias ct='colcon test'
alias ctp='colcon test --packages-select'
alias ctr='colcon test-result'

alias rt='ros2 topic list'
alias re='ros2 topic echo'
alias rn='ros2 node list'

alias killgazebo='killall -9 gazebo & killall -9 gzserver  & killall -9 gzclient'

alias af='ament_flake8'
alias ac='ament_cpplint'

alias testpub='ros2 run demo_nodes_cpp talker'
alias testsub='ros2 run demo_nodes_cpp listener'
alias testpubimg='ros2 run image_tools cam2image'
alias testsubimg='ros2 run image_tools showimage'
```
