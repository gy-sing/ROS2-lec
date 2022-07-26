# 2022.07.26 화요일
# 14강 Service 프로그래밍 - c++

<br/> 8강 강의노트
+ https://puzzling-cashew-c4c.notion.site/Service-python-f3a43eda3a4745fdb5f1dc1774b75e45

<br/>

### Service Server 생성
```
c++

m_service = create_service<TurningControl>(
    "turn_robot", 
		std::bind(&RobotTurnServer::response_callback, 
							this, 
							std::placeholders::_1,
							 std::placeholders::_2));

void response_callback(std::shared_ptr<TurningControl::Request> request, 
		std::shared_ptr<TurningControl::Response> response)

	...
```

### create_service
+ 사용하는 srv 타입 - TurningControl
+ 생성할 service 이름 - turn_robot
+ request 시 실행될 callback - std::bind...

+ Server는 무슨 요구가 왔는지 파악하고,
+ 그에 따라 필요한 연산을 수행한 뒤
+ response에 연산 결과를 넣어 되돌려줘야 합니다.


### 비동기
+ response 시간이 필요한 service request 동안 다른 일을 하다가, response가 오는 시점에 다시 돌아와 그 결과를 받습니다.