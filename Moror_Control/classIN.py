from IC import *
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as GPIO
import threading
import time
import math
import numpy

GPIO_CHIP_4=GPIO_CHIP(0x23,1);
GPIO_CHIP_7=GPIO_CHIP(0x26,1);
# Event 設定

class inPart1:
    def __init__(self):
        
        self.in_CVR_Dc12V_1=GPIO_CHIP_7.setup(3,'OUT','B');
        self.in_CVR_Dc12V_2=GPIO_CHIP_7.setup(2,'OUT','B');
        self.in_CVR_IFR=GPIO_CHIP_7.setup(0,'IN','B');
        self.in_ARM_Stepr12V_DIR=GPIO_CHIP_4.setup(6,'OUT','B');
        self.in_ARM_Stepr12V_STEP=GPIO_CHIP_4.setup(6,'OUT','A');
        self.factory = PiGPIOFactory();
        self.in_ARM_Servo6V = Servo(21, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.in_ARM_IFR=GPIO_CHIP_7.setup(0,'IN','A');
        self.in_ELE_Stepr12V_DIR=GPIO_CHIP_7.setup(7,'OUT','B');
        self.in_ELE_Stepr12V_STEP=GPIO_CHIP_7.setup(7,'OUT','A');
        self.in_ELE_Stepr5V_STEP=GPIO_CHIP_7.setup(3,'OUT','A');
        self.in_ELE_Stepr5V_STEP=GPIO_CHIP_7.setup(4,'OUT','A');
        self.in_ELE_Stepr5V_STEP=GPIO_CHIP_7.setup(5,'OUT','A');
        self.in_ELE_Stepr5V_STEP=GPIO_CHIP_7.setup(6,'OUT','A');
        self.in_ELE_SWITCH = GPIO_CHIP_7.setup(2,'IN','A');
        
    def IN_cvr_dc12V_start(self):
        
        GPIO_CHIP_7.output(3,0,'B');
        GPIO_CHIP_7.output(2,1,'B');
        time.sleep(1);

    def IN_cvr_dc12V_stop(self):
        
        GPIO_CHIP_7.output(3,0,'B');
        GPIO_CHIP_7.output(2,0,'B');
        time.sleep(1);

    def IN_arm_Servo6V_pull(self):

        for i in numpy.arange(10,95,0.15):
            self.in_ARM_Servo6V.value = math.sin(math.radians(i));
            time.sleep(0.001);

    def IN_arm_Servo6V_back(self):

        for i in numpy.arange(95,178,0.15):
            self.in_ARM_Servo6V.value = math.sin(math.radians(i));
            time.sleep(0.001);

    def step_ARM():
        p = pwm.set_pwm(0,0,3072);

    def step_IN():
        p = pwm.set_pwm(1,0,3072);

    def step_OUT():
        p = pwm.set_pwm(12,0,3072);

    def step_eleIN_floor1(t_IN):
        count =1;

        while True:
            if count > 33:
                t_IN.cancel();
                pwm.set_pwm(1,0,0);
                break;

            count += 1;
            time.sleep(0.14085);

    def step_eleIN_floorN(t_IN):
        count =1;

        while True:
            if count > 32:
                t_IN.cancel();
                pwm.set_pwm(1,0,0);
                break;

            count += 1;
            time.sleep(0.140);

    def IN_arm_Stepr12V(self):
            
            CW = 1;
            CCW = 0;
            SPR = 1255;
            step_count = SPR;
            delay = 0.00015;
            GPIO_CHIP_4.output(6,CW,'B');
            schedule.every(0.1).seconds.do(self.step0)

            print("推桿推出");
            count =1;
            while count <26:
                schedule.run_pending();
                time.sleep(0.1263);
                count=count+1;
            
            print("推桿收回");
            GPIO_CHIP_4.output(6,CCW,'B');
            count =1;
            while count <26:
                schedule.run_pending();
                time.sleep(0.1263);
                count=count+1;

            time.sleep(2);

    def IN_ele_Stepr12V_up(self, Ro):
        
        delay2 = 0.00001;
        GPIO_CHIP_7.output(7, 0,'A');
        pwm.set_pwm_freq(800);
        
        if Ro==1:
            t_IN = th.Timer(0.01,step_IN);
            td_IN = th.Thread(target = step_eleIN_floor1, args = (t_IN, ));
            t_IN.start();
            td_IN.start();
            t_IN.join();
            td_IN.join();

        else:
            t_IN = th.Timer(0.01,step_IN);
            td_IN = th.Thread(target = step_eleIN_floor1, args = (t_IN, ));
            t_IN.start();
            td_IN.start();
            t_IN.join();
            td_IN.join();

            for i in range(Ro-1):
                t_IN = th.Timer(0.01,step_IN);
                td_IN = th.Thread(target = step_eleIN_floorN, args = (t_IN, ));
                t_IN.start();
                td_IN.start();
                t_IN.join();
                td_IN.join();

    def IN_ele_Stepr12V_down(self, Ro):

        delay2 = 0.00001;
        GPIO_CHIP_7.output(7, 1,'A');
        pwm.set_pwm_freq(800);
        
        for i in range(Ro-1):
            t_IN = th.Timer(0.01,step_IN);
            td_IN = th.Thread(target = step_eleIN_floorN, args = (t_IN, ));
            t_IN.start();
            td_IN.start();
            t_IN.join();
            td_IN.join();


    def IN_ele_Stepr12V_bottom(self):
        
        In_ELE_switch = GPIO_CHIP_7.setup(2,'IN','A');
        In_ELE_switch = GPIO_CHIP_7.Input(2,'A');
        
        GPIO_CHIP_7.output(7, 1,'A');
        


    def IN_cvr_IFR(self,in_cvr_IFR):
        
        while in_cvr_IFR == 1:
            in_cvr_IFR = GPIO_CHIP_7.Input(0,'B');
            print("目前沒有偵測到貨物");
            if in_cvr_IFR ==0:
                print("偵測到貨物");
                time.sleep(0.5);
                print("手臂開啟");
                self.IN_arm_Servo6V_pull();
                In_arm_IFR = GPIO_CHIP_7.Input(0,'A');
                self.IN_arm_IFR(In_arm_IFR);

    def IN_arm_IFR(self,in_arm_IFR):
        
        while in_arm_IFR == 1:
            in_arm_IFR = GPIO_CHIP_7.Input(0,'A');           
            if in_arm_IFR == 0:
                print("貨物準備推動");
                time.sleep(1);
                self.IN_cvr_dc12V_stop();
                self.IN_arm_Stepr12V();

    def IN_ele_Stepr5V_push(self):
            
            STEPS_PER_REVOLUTION = 4*4; #定義8步模式下,每轉動一圈的步數為64*64
            SEQUENCE = [[1,0,0,1],
                        [0,0,0,1],
                        [0,0,1,1],
                        [0,0,1,0],
                        [0,1,1,0],
                        [0,1,0,0],
                        [1,1,0,0],
                        [1,0,0,0]]; #1:High,0:low,此為8步模式的電位
            STEPPER_5v_PINS = [6,5,4,3];
            
            for pin in STEPPER_5v_PINS:
                GPIO_CHIP_7.output(pin, 0,'A');
            SEQUENCE_COUNT = len(SEQUENCE); 
            PINS_COUNT = len(STEPPER_5v_PINS);
            sequence_index = 0; 
            direction = 1; 
            steps = 0;
            count = 1;
            print("平台準備推動貨物");
            
            while True:

                for pin in range(0, PINS_COUNT):
                    GPIO_CHIP_7.output(STEPPER_5v_PINS[pin], SEQUENCE[sequence_index][pin],'A');#GPIO.output(代表各個角位，)
                steps += direction;
               
                sequence_index += direction;
                sequence_index %= SEQUENCE_COUNT;

                count += 1;
                if count >=7900:
                    break;
                time.sleep(0.0014);

    def IN_ele_Stepr5V_back(self):
        
        STEPS_PER_REVOLUTION = 4*4; #定義8步模式下,每轉動一圈的步數為64*64
        SEQUENCE = [[1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1],
                    [1,0,0,1]]; #1:High,0:low,此為8步模式的電位
        
        STEPPER_5v_PINS = [6,5,4,3];
        
        for pin in STEPPER_5v_PINS:
            GPIO_CHIP_7.output(pin, 0,'A');
        SEQUENCE_COUNT = len(SEQUENCE); 
        PINS_COUNT = len(STEPPER_5v_PINS);
        sequence_index = 0; 
        direction = 1; 
        steps = 0;
        count = 1;
        print("平台準備收回");
        
        while True:

            for pin in range(0, PINS_COUNT):
                GPIO_CHIP_7.output(STEPPER_5v_PINS[pin], SEQUENCE[sequence_index][pin],'A');#GPIO.output(代表各個角位，)
            steps += direction;

            sequence_index += direction;
            sequence_index %= SEQUENCE_COUNT;

            count += 1;
            if count >=7900:
                break;
            time.sleep(0.0014);
        self.IN_ele_Stepr12V_bottom();

    def Synchronuous_process_IN_ARM_servo_ELE_stepr12V(self,Ro):
        
        print("手臂收回以及平台上升");
        t1 = threading.Thread(target=self.IN_arm_Servo6V_back);
        t2 = threading.Thread(target=self.IN_ele_Stepr12V_up,args=(Ro,));
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        
    def Synchronuous_process_IN_ELE_5V_12V(self,Ro):
        
        print("平台收回以及下降");

        t2 = threading.Thread(target=self.IN_ele_Stepr12V_down,args=(Ro,));
        t1 = threading.Thread(target=self.IN_ele_Stepr5V_back);

        t2.start();
        t1.start();

        t2.join();
        t1.join();
        self.IN_cvr_dc12V_start();
        
    def IN_part1_run(self,Ro):
        
        while True:
            self.IN_cvr_dc12V_start();
            in_cvr_IFR = GPIO_CHIP_7.Input(0,'B');
            self.IN_cvr_IFR(in_cvr_IFR);
            
            self.Synchronuous_process_IN_ARM_servo_ELE_stepr12V(Ro);
            self.IN_ele_Stepr5V_push();
            time.sleep(3);
            self.Synchronuous_process_IN_ELE_5V_12V(Ro);
