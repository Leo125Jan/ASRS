from IC import *

GPIO_CHIP_8=GPIO_CHIP(0x27,1);
class inPart2:

    def __init__(self):
        
        self.in_STAY_1_Dc5V_1=GPIO_CHIP_8.setup(0,'OUT','B');
        self.in_STAY_1_Dc5V_2=GPIO_CHIP_8.setup(0,'OUT','A');
        self.in_STAY_1_IFR=GPIO_CHIP_8.setup(3,'IN','A');
        self.in_STAY_2_Dc5V_1=GPIO_CHIP_8.setup(1,'OUT','B');
        self.in_STAY_2_Dc5V_2=GPIO_CHIP_8.setup(1,'OUT','A');
        self.in_STAY_2_IFR=GPIO_CHIP_8.setup(4,'IN','A');
        self.in_STAY_3_Dc5V_1=GPIO_CHIP_8.setup(2,'OUT','B');
        self.in_STAY_3_Dc5V_2=GPIO_CHIP_8.setup(2,'OUT','A');
        self.in_STAY_3_IFR_1=GPIO_CHIP_8.setup(5,'IN','A');


    def IN_stay_1_motor_start(self):
        
        global GPIO_CHIP_8;
        GPIO_CHIP_8.output(0,1,'B');
        GPIO_CHIP_8.output(0,0,'A');

    def In_stay_1_motor_stop(self):
        
        global GPIO_CHIP_8;
        GPIO_CHIP_8.output(0,0,'B');
        GPIO_CHIP_8.output(0,0,'A');

    def In_stay_2_motor_start(self):
        
        global GPIO_CHIP_8;
        GPIO_CHIP_8.output(1,1,'B');
        GPIO_CHIP_8.output(1,0,'A');

    def In_stay_2_motor_stop(self):

        GPIO_CHIP_8.output(1,0,'B');
        GPIO_CHIP_8.output(1,0,'A');

    def In_stay_3_motor_start(self):
        global GPIO_CHIP_8;
        GPIO_CHIP_8.output(2,0,'B');
        GPIO_CHIP_8.output(2,1,'A');

    def In_stay_3_motor_stop(self):
        
        GPIO_CHIP_8.output(2,0,'B');
        GPIO_CHIP_8.output(2,0,'A');

    def In_stay(self,Ro):
        In_STAY_1_IFR = GPIO_CHIP_8.Input(3,'A');        
        In_STAY_2_IFR = GPIO_CHIP_8.Input(4,'A');
        In_STAY_3_IFR = GPIO_CHIP_8.Input(5,'A');
        
        if Ro == 1:
            if In_STAY_1_IFR == 1:
                self.In_stay_1_motor_start();
            else:
                self.In_stay_1_motor_stop();
        elif Ro == 2:
            if In_STAY_2_IFR == 1:
                self.In_stay_2_motor_start();
            else:
                self.In_stay_2_motor_stop();
        else:
            if In_STAY_3_IFR == 1:
                self.In_stay_3_motor_start();
            else:
                switch = In_STAY_3_IFR;
                print(switch);
                self.In_stay_3_motor_stop();








