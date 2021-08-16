class Bicycle(object):
    def run(self, km, name):
        if km == 0:
            pass
        else:
            print('%s得改用腳踩才能跑上%d公里唷~' % (name, km))


class EBicycle(Bicycle):
    def __init__(self, volume,km=0):
        self.volume = volume
        self.km = km
        print('電動車剛買時,內存電力:%d度。總里程數:%d公里。' % (volume, self.km))
        self.ten = 0  

    def fill_charge(self, vol=0):
        print('-'*20)
        self.volume += vol
        print('電動車已充:%d度電,目前電力:%d度。' % (vol, self.volume))

    def run(self, km, name):
        print('-'*20)
        print('%s想騎電動車:%d公里去溜搭~' % (name, km))

        if self.volume <= 0:
            print('沒電了啦，電動車不會跑了唷!')
            super().run(km, name)

        if self.volume > 0:
            print('跑前電力:', self.volume, '度。能再跑:', self.volume * 10, '公里。')
            if self.volume * 10 <= km:
                super().run(km - self.volume * 10, name)
                self.volume = 0  
                print('跑後電力:%d度。' % self.volume)
            elif self.volume*10 >= km:  
                if km <= 10 and self.ten+km < 10:
                    self.volume -= 0
                    self.ten += km
                elif km <= 10 and self.ten+km >= 10:
                    self.ten = (self.ten + km) - 10
                    self.volume -= 1
                elif km >= 10:
                    self.volume -= km // 10
                    if self.ten + km >= 10:
                        self.ten = (self.ten + km) - 10
                        self.volume -= 1
                    elif self.ten + km < 10:
                        self.ten += km
                        self.volume -= 0

                print('跑後電力:%d度。'%self.volume)
                self.km += km  
                print('總里程數:%d公里。' % self.km)


b = Bicycle()
b.run(10, 'Dora')
e = EBicycle(5)  
e.fill_charge(3)
e.run(4, 'Dora')
e.run(28, 'Dora')
e.run(200, 'Dora')
e.fill_charge(50)
e.run(7, 'Dora')
e.run(50, 'Dora')
e.run(350, 'Dora')
e.run(3, 'Dora')
e.fill_charge(4)
e.run(0, 'Dora')
e.run(12, 'Dora')
