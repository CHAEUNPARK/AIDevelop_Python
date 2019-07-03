### 모듈간 내부적인 충돌 일어날 수 있으니 조심 as 사용 권장
### *는 왠만하면 안쓰는 것을 권장(실무)
### 직접 import하려는 함수나 클래스를 명시해주는 것을 권장

from sam import *

aa()
s = Car()
s.showInfo()