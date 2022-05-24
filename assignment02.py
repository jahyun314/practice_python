import random

# ans=정답,ip=입력
def compare_answer(ans,ip):
  if ans==ip:
    num = 0
  elif ans>ip:
    num = -1
  elif ans<ip:
    num = 1
  return num


answer = random.randint(10,99)
count = 0

while count<10:
  my_answer = int(input("두자리 정수 입력: "))
  count += 1
  key = compare_answer(answer, my_answer)
  if key == 0:
    print("정답입니다. %d번 만에 맞추셨습니다\n게임 끝!!!" %(count))
    break
  elif key == 1:
    print("아닙니다. 더 작은 숫자입니다!")
  elif key == -1:
    print("아닙니다. 더 큰 숫자입니다!")
