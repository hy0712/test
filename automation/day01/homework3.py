"""
小明，10岁，男，上山去砍柴
小明，10岁，男，开车去东北
小明，10岁，男，最爱大保健
老李，90岁，男，上山去砍柴
老李，90岁，男，开车去东北
老李，90岁，男，最爱大保健

"""


class Sprot():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def kanchai(self):
        print("%s，%s,%s,上山去砍柴"%(self.name,self.age,self.sex))

    def dongbei(self):
        print("%s，%s,%s,开车去东北"%(self.name,self.age,self.sex))
    def baojian(self):
        print("%s，%s,%s,最爱大保健"%(self.name,self.age,self.sex))

xiaoming = Sprot('小明','10岁','男')
xiaoming.kanchai()
xiaoming.dongbei()
xiaoming.baojian()

laoli = Sprot('老李','90岁','男')
laoli.kanchai()
laoli.dongbei()
laoli.baojian()



