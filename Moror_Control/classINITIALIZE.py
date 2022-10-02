from IC import *
import threading
import time
import multiprocessing as mp
import queue
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import threading as th
import math
import numpy
import Adafruit_PCA9685
import schedule
from classOUT import *

pwm = Adafruit_PCA9685.PCA9685();
OUT_STAY = outPart1();

GPIO_CHIP_1 = GPIO_CHIP(0x20,1);
GPIO_CHIP_2 = GPIO_CHIP(0x21,1);
GPIO_CHIP_3 = GPIO_CHIP(0x22,1);
GPIO_CHIP_5 = GPIO_CHIP(0x24,1);
GPIO_CHIP_7 = GPIO_CHIP(0x26,1);

class initialize:
    
    def __init__(self):
        
        self.SHUTTLE_1_SWITCH = GPIO_CHIP_1.setup(2,'IN','B');
        self.SHUTTLE_2_SWITCH = GPIO_CHIP_2.setup(2,'IN','B');
        self.SHUTTLE_3_SWITCH = GPIO_CHIP_3.setup(2,'IN','B');
        self.out_ELE_SWITCH = GPIO_CHIP_5.setup(2,'IN','A');
        self.in_ELE_SWITCH = GPIO_CHIP_7.setup(2,'IN','A');
        self.SHUTTLE_1_Stepr12V_DIR = GPIO_CHIP_1.setup(0,'OUT','B');
#         self.SHUTTLE_1_Stepr12V_STEP = GPIO_CHIP_1.setup(0,'OUT','A');
        self.SHUTTLE_2_Stepr12V_DIR = GPIO_CHIP_2.setup(0,'OUT','B');
#         self.SHUTTLE_2_Stepr12V_STEP = GPIO_CHIP_2.setup(0,'OUT','A');
        self.SHUTTLE_3_Stepr12V_DIR = GPIO_CHIP_3.setup(0,'OUT','B');
#         self.SHUTTLE_3_Stepr12V_STEP = GPIO_CHIP_3.setup(0,'OUT','A');
        self.out_ELE_Stepr12V_DIR = GPIO_CHIP_5.setup(7,'OUT','B');
#         self.out_ELE_Stepr12V_STEP = GPIO_CHIP_5.setup(7,'OUT','A');
        self.in_ELE_Stepr12V_DIR = GPIO_CHIP_7.setup(7,'OUT','A');

        
        self.factory = PiGPIOFactory();
        self.SHUTTLE_1_Servo6V = Servo( 6, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.SHUTTLE_1_Servo5V = Servo(13, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.SHUTTLE_2_Servo6V = Servo(19, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.SHUTTLE_2_Servo5V = Servo(26, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.SHUTTLE_3_Servo6V = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.SHUTTLE_3_Servo5V = Servo(16, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.in_ARM_Servo6V = Servo(21, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        
    def initial(self):
        
        self.in_ARM_Servo6V.value = None;
        self.SHUTTLE_1_Servo5V.value = math.sin(math.radians(-45));
        self.SHUTTLE_2_Servo5V.value = math.sin(math.radians(-38));
        self.SHUTTLE_3_Servo5V.value = math.sin(math.radians(-38));
        self.SHUTTLE_1_Servo6V.value = math.sin(math.radians(178));
        self.SHUTTLE_2_Servo6V.value = math.sin(math.radians(0));
        self.SHUTTLE_3_Servo6V.value = math.sin(math.radians(5));
        
    def td_(self,t1,t2,t3,t4,t5):
        
        Shuttle_1_switch = GPIO_CHIP_1.setup(2,'IN','B');
        Shuttle_2_switch = GPIO_CHIP_2.setup(2,'IN','B');    
        Shuttle_3_switch = GPIO_CHIP_3.setup(2,'IN','B');
        In_ELE_switch = GPIO_CHIP_7.setup(2,'IN','A');
        Out_ELE_switch = GPIO_CHIP_5.setup(2,'IN','A');
        
        while True:
            
            Shuttle_1_switch = GPIO_CHIP_1.Input(2,'B');
            Shuttle_2_switch = GPIO_CHIP_2.Input(2,'B');
            Shuttle_3_switch = GPIO_CHIP_3.Input(2,'B');
            In_ELE_switch = GPIO_CHIP_7.Input(2,'A');
            Out_ELE_switch = GPIO_CHIP_5.Input(2,'A');
            
            if Shuttle_1_switch == 1:
                
                pwm.set_pwm(11,0,0);
                t1.cancel();
                
                print('SHUTTLE1已歸零');
            
            if Shuttle_2_switch == 1:
                
                pwm.set_pwm(13,0,0);
                t2.cancel();
                
                print('SHUTTLE2已歸零');
                
            if Shuttle_3_switch == 1:
                
                pwm.set_pwm(14,0,0);
                t3.cancel();
                
                print('SHUTTLE2已歸零');
                
            if In_ELE_switch == 1:
                
                pwm.set_pwm(1,0,0);
                t4.cancel();
                
                print('SHUTTLE2已歸零');
                
            if Out_ELE_switch == 1:
                
                pwm.set_pwm(12,0,0);
                t5.cancel();
                
                print('SHUTTLE2已歸零');
                
            if Shuttle_1_switch == 1 and Shuttle_2_switch == 1 and Shuttle_3_switch == 1 and In_ELE_switch == 1 and Out_ELE_switch == 1:
                
                break;
            
            time.sleep(0.001);

    def Initialize_shuttle_1(self):
        
        CW = 1;
        CCW = 0;                        
        GPIO_CHIP_1.output(0, 0,'B');
        pwm.set_pwm_freq(800);
        pwm.set_pwm(11,0,3072);
            
    def Initialize_shuttle_2(self):
        
        CW = 1;
        CCW = 0;                       
        GPIO_CHIP_2.output(0, 1,'B');
        pwm.set_pwm_freq(800);
        pwm.set_pwm(13,0,3072);

    def Initialize_shuttle_3(self):
        
        CW = 1;
        CCW = 0;                       
        GPIO_CHIP_3.output(0, 0,'B');
        pwm.set_pwm_freq(800);
        pwm.set_pwm(14,0,3072);
           
            
    def Initialize_IN_ele(self):

        CW = 1;
        CCW = 0;                        
        GPIO_CHIP_7.output(7, 0,'A');
        pwm.set_pwm_freq(800);
        pwm.set_pwm(1,0,3072);

    def Initialize_OUT_ele(self):
        
        CW = 1;
        CCW = 0;                      
        GPIO_CHIP_5.output(7, CCW,'B');
        pwm.set_pwm_freq(800);
        pwm.set_pwm(12,0,3072);
        
    def Initialize_OUT_ele_final(self):
        
        GPIO_CHIP_5.output(7,1,'B');
        pwm.set_pwm(12,0,3072);
    
    def OUT_ele_final_step(self,t6):

        count = 1;
        
        while True:
            
            if count > 4:
                
                t6.cancel();
                pwm.set_pwm(12 ,0, 0);
                
                break;
            
            count += 1;
            time.sleep(0.1);
        
    def clean(self):
        
        self.in_ARM_Servo6V.value = math.sin(math.radians(10));
        self.in_ARM_Servo6V.value = None;
        self.SHUTTLE_1_Servo6V.value = None;
        self.SHUTTLE_1_Servo5V.value = None;
        self.SHUTTLE_2_Servo6V.value = None;
        self.SHUTTLE_2_Servo5V.value = None;
        self.SHUTTLE_3_Servo6V.value = None;
        self.SHUTTLE_3_Servo5V.value = None;
        
        PINS = [0,1,2,3,4,5,6,7];
        
        for pin in PINS:
            
            GPIO_CHIP_1.output(pin, 0,'A');
            GPIO_CHIP_2.output(pin, 0,'A');
            GPIO_CHIP_3.output(pin, 0,'A');
            GPIO_CHIP_5.output(pin, 0,'A');
            GPIO_CHIP_7.output(pin, 0,'A');
            GPIO_CHIP_1.output(pin, 0,'B');
            GPIO_CHIP_2.output(pin, 0,'B');
            GPIO_CHIP_3.output(pin, 0,'B');
            GPIO_CHIP_5.output(pin, 0,'B');
            GPIO_CHIP_7.output(pin, 0,'B');
            
            GPIO_CHIP_1.setup(pin, 'IN','A');
            GPIO_CHIP_2.setup(pin, 'IN','A');
            GPIO_CHIP_3.setup(pin,'IN','A');
            GPIO_CHIP_5.setup(pin,'IN','A');
            GPIO_CHIP_7.setup(pin,'IN','A');
            GPIO_CHIP_1.setup(pin,'IN','B');
            GPIO_CHIP_2.setup(pin,'IN','B');
            GPIO_CHIP_3.setup(pin,'IN','B');
            GPIO_CHIP_5.setup(pin,'IN','B');
            GPIO_CHIP_7.setup(pin,'IN','B');

    def INITIALIZE(self):
        
        self.initial();
        
        t1 = th.Timer(0.1,self.Initialize_shuttle_1);
        t2 = th.Timer(0.1,self.Initialize_shuttle_2);
        t3 = th.Timer(0.1,self.Initialize_shuttle_3);
        t4 = th.Timer(0.1,self.Initialize_IN_ele);
        t5 = th.Timer(0.1,self.Initialize_OUT_ele);
        td = th.Thread(target = self.td_, args = (t1,t2,t3,t4,t5));

        
        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t5.start();
        td.start();

        t1.join();
        t2.join();
        t3.join();
        t4.join();
        t5.join();
        td.join();
        
        t6 = th.Timer(0.01,self.Initialize_OUT_ele_final);
        td_final = th.Thread(target = self.OUT_ele_final_step, args = (t6,));
        t6.start();
        td_final.start();
        t6.join();
        td_final.join();

        OUT_STAY.OUT_stay2_servo_zero();
        OUT_STAY.OUT_stay3_servo_zero();