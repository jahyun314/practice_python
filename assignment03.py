class Employee():
  def __init__(self,name,base,extra=0):
    self.__name = name
    self.__base = base
    self.__extra = extra

  def getName(self):
    return self.__name

  def getBase(self):
    return self.__base

  def getExtra(self):
    return self.__extra

  def calc_salary(self):
    return (self.__base + self.__extra)
  
  def plus_extra(self,num):
    self.__extra += num
  
  def __str__(self):
    return "이    름 : %s\n기 본 금 : %d\n초과금액 : %d\n총 월 급 : %d\n=================" \
      %(self.__name,self.__base,self.__extra, (self.__base + self.__extra))


class Manager(Employee):
  def __init__(self,name,base,add,extra=0):
    super().__init__(name,base,extra)
    self.__add = add

  def calc_salary(self):
    return (self.getBase + self.getExtra + self.__add)

  def __str__(self):
    return "이   름: %s\n기 본 금 : %d\n초과금액 : %d\n추가수당 : %d\n총 월 급 : %d\n=================" \
      %(self.getName(),self.getBase(),self.getExtra(),self.__add,(self.getBase()+self.getExtra()+self.__add))

#객체 생성
e1 = Employee("홍길동", 200)
e2 = Employee("이영희", 220)
m1 = Manager("김철수",250,30)

#초기값 출력
print(e1)
print(e2)
print(m1)

#초가근무 더하고 출력
print("%s : 초과근무액 50,60 추가" % e1.getName())
e1.plus_extra(50)
e1.plus_extra(60)
print(e1)

print("%s : 초과근무액 60, 60, 60 추가" % e2.getName())
e2.plus_extra(60)
e2.plus_extra(60)
e2.plus_extra(60)
print(e2)

print("%s : 초과근무액 50, 50 추가" % m1.getName())
m1.plus_extra(50)
m1.plus_extra(50)
print(m1)