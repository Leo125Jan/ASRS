from IC import *
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import threading
import time
import math
import numpy

GPIO_CHIP_1 = GPIO_CHIP(0x20,1);
GPIO_CHIP_2 = GPIO_CHIP(0x21,1);
GPIO_CHIP_3 = GPIO_CHIP(0x22,1);
GPIO_CHIP_8 = GPIO_CHIP(0x27,1);
delay = 0.001;
    
class Shuttle:
  
    def __init__(self):
        
        self.SHUTTLE_1_Stepr12V_DIR = GPIO_CHIP_1.setup(0,'OUT','B');
        self.SHUTTLE_1_Stepr12V_STEP = GPIO_CHIP_1.setup(0,'OUT','A');
        self.SHUTTLE_2_Stepr12V_DIR = GPIO_CHIP_2.setup(0,'OUT','B');
        self.SHUTTLE_2_Stepr12V_STEP = GPIO_CHIP_2.setup(0,'OUT','A');
        self.SHUTTLE_3_Stepr12V_DIR = GPIO_CHIP_3.setup(0,'OUT','B');
        self.SHUTTLE_3_Stepr12V_STEP = GPIO_CHIP_3.setup(0,'OUT','A');
        
        self.factory = PiGPIOFactory();
        self.SHUTTLE_1_Servo6V = Servo( 6, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.SHUTTLE_1_Servo5V = Servo(13, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.SHUTTLE_2_Servo6V = Servo(19, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.SHUTTLE_2_Servo5V = Servo(26, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.SHUTTLE_3_Servo6V = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.SHUTTLE_3_Servo5V = Servo(16, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        
        self.SHUTTLE_1_Servo5V.value = math.sin(math.radians(-38));
        self.SHUTTLE_2_Servo5V.value = math.sin(math.radians(-38));
        self.SHUTTLE_3_Servo5V.value = math.sin(math.radians(-38));
        
        self.in_STAY_1_IFR = GPIO_CHIP_8.setup(3,'IN','A');
        self.in_STAY_2_IFR = GPIO_CHIP_8.setup(4,'IN','A');
        self.in_STAY_3_IFR = GPIO_CHIP_8.setup(5,'IN','A');

    def shuttle_1_servo_pull(self):
            
        for i in numpy.arange(0,80,0.15):
            
            self.SHUTTLE_1_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay); 

        for i in numpy.arange(-38,0,0.15):
            
            self.SHUTTLE_1_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay); 

        for i in numpy.arange(80,174,0.15):
            
            self.SHUTTLE_1_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay);

        for i in numpy.arange(0,-38,-0.15):
            
            self.SHUTTLE_1_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay);

    def shuttle_1_servo_push(self):

        for i in numpy.arange(-38,0,0.15):
            
            self.SHUTTLE_1_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay);
            
        for i in numpy.arange(0,80,0.15):
            
            self.SHUTTLE_1_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay); 

        for i in numpy.arange(0,-38,-0.15):
            
            self.SHUTTLE_1_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay);
            
        for i in numpy.arange(80,174,0.15):
            
            self.SHUTTLE_1_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay);

    def shuttle_2_servo_pull(self):

        for i in numpy.arange(0,80,0.15):
            
            self.SHUTTLE_3_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay); 

        for i in numpy.arange(-38,0,0.15):
            
            self.SHUTTLE_3_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay); 

        for i in numpy.arange(80,174,0.15):
            
            self.SHUTTLE_3_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay);

        for i in numpy.arange(0,-38,-0.15):
            
            self.SHUTTLE_3_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay);

    def shuttle_2_servo_push(self):

        for i in numpy.arange(-38,0,0.15):
            
            self.SHUTTLE_3_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay);
            
        for i in numpy.arange(0,80,0.15):
            
            self.SHUTTLE_3_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay); 

        for i in numpy.arange(0,-38,-0.15):
            
            self.SHUTTLE_3_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay);
            
        for i in numpy.arange(80,174,0.15):
            
            self.SHUTTLE_3_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay);

    def shuttle_3_servo_pull(self):
        
        for i in numpy.arange(0,80,0.15):
            
            self.SHUTTLE_3_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay); 

        for i in numpy.arange(-38,0,0.15):
            
            self.SHUTTLE_3_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay); 

        for i in numpy.arange(80,174,0.15):
            
            self.SHUTTLE_3_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay);

        for i in numpy.arange(0,-38,-0.15):
            
            self.SHUTTLE_3_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay);

    def shuttle_3_servo_push(self):
        
        for i in numpy.arange(-38,0,0.15):
            
            self.SHUTTLE_3_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay);
            
        for i in numpy.arange(0,80,0.15):
            
            self.SHUTTLE_3_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay); 

        for i in numpy.arange(0,-38,-0.15):
            
            self.SHUTTLE_3_Servo5V.value = math.sin(math.radians(i));
            time.sleep(delay);
            
        for i in numpy.arange(80,176,0.15):
            
            self.SHUTTLE_3_Servo6V.value = math.sin(math.radians(i));
            time.sleep(delay);

    def step_1():
        p = pwm.set_pwm(11,0,3072);

    def step_2():
        p = pwm.set_pwm(13,0,3072);  

    def step_3():
        p = pwm.set_pwm(14,0,3072);

    def step_shuttle1(t_shuttle1):
        count =1;

        while True:
            if count > 10:
                t_shuttle1.cancel();
                pwm.set_pwm(11,0,0);
                break;
                
            count += 1;
            time.sleep(0.14085);

    def step_shuttle2(t_shuttle2):
        count =1;

        while True:
            if count > 10:
                t_shuttle2.cancel();
                pwm.set_pwm(13,0,0);
                break;

            count += 1;
            time.sleep(0.14085);

    def step_shuttle3(t_shuttle3):
        count =1;

        while True:
            if count > 10:
                t_shuttle3.cancel();
                pwm.set_pwm(14,0,0);
                break;

            count += 1;
            time.sleep(0.14085);

    def shuttle_1_stepr12V(self,rotation,direction):

        delay2 = 0.00001;
        pwm.set_pwm_freq(800);
        GPIO_CHIP_1.output(0, direction,'B');
        
        for i in range(rotation):
            t1 = th.Timer(0.01,step_1);
            td_1 = th.Thread(target = step_shuttle1, args = (t1, ));
            t1.start();
            td_1.start();
            t1.join();
            td_1.join();

    def shuttle_1(self,q2):
        
        In_STAY_1_IFR = GPIO_CHIP_1.Input(3,'A');
        location = 1;
        
        
        while True:
            
            In_STAY_1_IFR = GPIO_CHIP_1.Input(3,'A');
            
            if not q2.empty():
                
                IO = int(q2.get());
            
                if IO == 1:
                    
                    posi = q2.get();
                    Ro = int(posi[0]);
                    Co = int(posi[1]);
                    
                    if Ro == 1:
                        
                        EN_rotation = location-1;   #跟入口差的圈數
                        self.shuttle_1_stepr12V(EN_rotation,0);
                        
                        while In_STAY_1_IFR == 1:
                            
                            if In_STAY_1_IFR == 0:
                                
                                time.sleep(1);
                                self.shuttle_1_servo_pull();
                                
                                if Co == 1:
                                    
                                    self.shuttle_1_stepr12V(Co,1);
                                    
                                elif Co == 2:
                                    
                                    self.shuttle_1_stepr12V(Co,1);
                                    
                                elif Co ==3:
                                    
                                    self.shuttle_1_stepr12V(Co,1);
                                    
                                self.shuttle_1_servo_push();
                                location = Co+1;
                                
                                break;
                            
                            time.sleep(2);

                elif IO == 0:
                    
                    posi = q2.get();
                    Ro = int(posi[0]);
                    Co = int(posi[1]);
                    
                    diviation = location - Co; #跟最後位置差的圈數，也可以用正負來看方向
                    
                    if diviation<0:
                        
                        self.shuttle_1_stepr12V(diviation,1);
                        
                    else:
                        
                        self.shuttle_1_stepr12V(diviation,0);
                        
                    self.shuttle_1_servo_pull();
                    EX_rotation = 5-location;
                    self.shuttle_1_stepr12V(EX_rotation,0);
                    self.shuttle_1_servo_push();
                    location = 5;
                
    def shuttle_2(self,q2):
        
        In_STAY_2_IFR = GPIO_CHIP_2.Input(3,'A');
        location = 1;
        
        while True:
            
            In_STAY_2_IFR = GPIO_CHIP_2.Input(3,'A');
            
            if not q2.empty():
                
                IO = int(q2.get());
               
                if IO == 1:
                    
                    posi = q2.get();
                    Ro = int(posi[0]);
                    Co = int(posi[1]);
                    
                    if Ro == 2:
                        
                        EN_rotation = location-1;   #跟入口差的圈數
                        self.shuttle_2_stepr12V(EN_rotation,0);
                        
                        while In_STAY_2_IFR == 1:
                            
                            if In_STAY_2_IFR == 0:
                                
                                time.sleep(1);
                                self.shuttle_2_servo_pull();
                                
                                if Co == 1:
                                    
                                    self.shuttle_2_stepr12V(Co,1);
                                    
                                elif Co == 2:
                                    
                                    self.shuttle_2_stepr12V(Co,1);
                                    
                                elif Co ==3:
                                    
                                    self.shuttle_2_stepr12V(Co,1);
                                    
                                self.shuttle_2_servo_push();
                                location = Co+1;
                                
                            time.sleep(2);

                elif IO == 0:
                    
                    diviation = location - Co; #跟最後位置差的圈數，也可以用正負來看方向
                    
                    if diviation<0:
                        
                        self.shuttle_2_stepr12V(diviation,1);
                        
                    else:
                        
                        self.shuttle_2_stepr12V(diviation,0);
                        
                    self.shuttle_2_servo_pull();
                    EX_rotation = 5-location;
                    self.shuttle_2_stepr12V(EX_rotation,0);
                    self.shuttle_2_servo_push();
                    location = 5;
                
    def shuttle_3(self,q2):
        
        In_STAY_3_IFR = GPIO_CHIP_3.Input(3,'A');
        location = 1;
        
        while True:
            
            In_STAY_3_IFR = GPIO_CHIP_3.Input(3,'A');
            
            if not q2.empty():
                
                IO = int(q2.get());
            
                if IO == 1:
                    
                    posi = q2.get();
                    Ro = int(posi[0]);
                    Co = int(posi[1]);
                    
                    if Ro == 3:
                        
                        EN_rotation = location-1;   #跟入口差的圈數
                        self.shuttle_3_stepr12V(EN_rotation,0);
                        
                        while In_STAY_2_IFR == 1:
                            
                            if In_STAY_3_IFR == 0:
                                
                                time.sleep(1);
                                self.shuttle_3_servo_pull();
                                
                                if Co == 1:
                                    
                                    self.shuttle_3_stepr12V(Co,1);
                                    
                                elif Co == 2:
                                    
                                    self.shuttle_3_stepr12V(Co,1);
                                    
                                elif Co ==3:
                                    
                                    self.shuttle_3_stepr12V(Co,1);
                                    
                                self.shuttle_3_servo_push();
                                location = Co+1;
                                
                            time.sleep(2);

                elif IO == 0:
                    
                    diviation = location - Co; #跟最後位置差的圈數，也可以用正負來看方向
                    
                    if diviation<0:
                        
                        self.shuttle_3_stepr12V(diviation,1);
                        
                    else:
                        
                        self.shuttle_3_stepr12V(diviation,0);
                        
                    self.shuttle_3_servo_pull();
                    EX_rotation = 5-location;
                    self.shuttle_3_stepr12V(EX_rotation,0);
                    self.shuttle_3_servo_push();
                    location = 5;
                
    def shuttle_thread(self,q2):
        
        t1 = threading.Thread(target = self.shuttle_1, args = (q2,));
        t2 = threading.Thread(target = self.shuttle_2, args = (q2,));
        t3 = threading.Thread(target = self.shuttle_3, args = (q2,));
        
        t1.start();
        t2.start();
        t3.start();