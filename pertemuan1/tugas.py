class motor:
    def __init__(self, nama,):
        self.nama = nama
        
    def suara_motor(self):
        pass
    
class motor_klx(motor):
    def suara_motor(self):
        return ('brummm')
    
class motor_beat(motor):
    def suara_motor(self):
        return ('wushhh')
    
class motor_balap(motor):
    def suara_motor(self):
        return ('wronggg')
    
class motor_rx(motor):
    def suara_motor(self):
        return ('trentenggg')
    
motor_klx = motor_klx('Motor KLX')
motor_beat = motor_beat('Motor BEAT')
motor_balap = motor_balap('Motor Balap')
motor_rx = motor_rx('Motor rx')

print(f'{motor_klx.nama} bersuara {motor_klx.suara_motor()}')
print(f'{motor_beat.nama} bersuara {motor_beat.suara_motor()}')
print(f'{motor_balap.nama} bersuara {motor_balap.suara_motor()}')
print(f'{motor_rx.nama} bersuara {motor_rx.suara_motor()}')