from IC import *
import RPi.GPIO as GPIO
import time
import math
import numpy as np
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

GPIO_CHIP_5=GPIO_CHIP(0x24,1);
GPIO_CHIP_6=GPIO_CHIP(0x25,1);

class outPart1:
    def __init__(self):

        self.out_STAY1_shuttle_IFR=GPIO_CHIP_6.setup(4,'IN','A');
        self.out_stay1_ele_IFR=GPIO_CHIP_6.setup(5,'IN','A');
        self.out_STAY2_shuttle_IFR=GPIO_CHIP_6.setup(6,'IN','A');
        self.out_STAY2_ele_IFR=GPIO_CHIP_6.setup(7,'IN','A');
        self.out_STAY3_shuttle_IFR=GPIO_CHIP_6.setup(6,'IN','B');
        self.out_STAY3_ele_IFR=GPIO_CHIP_6.setup(7,'IN','B');
        self.out_STAY1_Dc5V_1=GPIO_CHIP_6.setup(0,'OUT','B');
        self.out_STAY1_Dc5V_2=GPIO_CHIP_6.setup(0,'OUT','A');
        self.out_STAY2_Dc5V_1=GPIO_CHIP_6.setup(1,'OUT','B');
        self.out_STAY2_Dc5V_2=GPIO_CHIP_6.setup(1,'OUT','A');
        self.out_STAY3_Dc5V_1=GPIO_CHIP_6.setup(2,'OUT','B');
        self.out_STAY3_Dc5V_2=GPIO_CHIP_6.setup(2,'OUT','A');
        self.factory = PiGPIOFactory();
        self.out_STAY2_Servo5V = Servo(21, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.out_STAY3_Servo5V = Servo(20, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=self.factory);
        self.out_ELE_Stepr12V_DIR=GPIO_CHIP_5.setup(7,'OUT','B');
        self.out_ELE_Stepr12V_STEP=GPIO_CHIP_5.setup(7,'OUT','A');
        self.out_ELE_Stepr5V_STEP=GPIO_CHIP_5.setup(3,'OUT','A');
        self.out_ELE_Stepr5V_STEP=GPIO_CHIP_5.setup(4,'OUT','A');
        self.out_ELE_Stepr5V_STEP=GPIO_CHIP_5.setup(5,'OUT','A');
        self.out_ELE_Stepr5V_STEP=GPIO_CHIP_5.setup(6,'OUT','A');
        self.out_CVR_Dc12V_1=GPIO_CHIP_5.setup(3,'OUT','B');
        self.out_CVR_Dc12V_2=GPIO_CHIP_5.setup(2,'OUT','B');

    def OUT_stay1_dc5V_start(self):      
    # 暫存區直流馬達  
      
        GPIO_CHIP_6.output(0,0,'B');
        GPIO_CHIP_6.output(0,1,'A');
        time.sleep(1);

    def OUT_stay1_dc5V_stop(self):
        
        GPIO_CHIP_6.output(0,0,'B');
        GPIO_CHIP_6.output(0,0,'A');
        time.sleep(1);
        
    def OUT_stay2_dc5V_start(self):      
    # 暫存區直流馬達  
      
        GPIO_CHIP_6.output(1,0,'B');
        GPIO_CHIP_6.output(1,1,'A');
        time.sleep(1);

    def OUT_stay2_dc5V_stop(self):
        
        GPIO_CHIP_6.output(1,0,'B');
        GPIO_CHIP_6.output(1,0,'A');
        time.sleep(1);
        
    def OUT_stay3_dc5V_start(self):      
    # 暫存區直流馬達  
      
        GPIO_CHIP_6.output(2,0,'B');
        GPIO_CHIP_6.output(2,1,'A');
        time.sleep(1);

    def OUT_stay3_dc5V_stop(self):
        
        GPIO_CHIP_6.output(2,0,'B');
        GPIO_CHIP_6.output(2,0,'A');
        time.sleep(1);
        
    def OUT_stay1_shuttle_IFR(self,out_stay1_shuttle_IFR):
        
        while OUT_stay1_shuttle_IFR == 1:
            print("目前沒有偵測到貨物");
            Out_stay1_shuttle_IFR = GPIO_CHIP_6.Input(5,'A');
            if OUT_stay1_shuttle_IFR == 0:
                print("偵測到貨物");
                time.sleep(2);
                print("dc5V 開始轉動");
                self.OUT_stay1_dc5V_start();
                Out_stay1_ele_IFR = GPIO_CHIP_6.Input(5,'A');
                self.OUT_stay1_ele_IFR(Out_stay1_ele_IFR);

    def OUT_stay1_ele_IFR(self,out_stay1_ele_IFR):
        
        while out_stay1_ele_IFR == 1:
            out_stay1_ele_IFR = GPIO_CHIP_6.Input(5,'A');           
            if out_stay1_ele_IFR == 0:
                print("dc5V 停止轉動");
                time.sleep(0.5);
                self.OUT_stay1_dc5V_stop();

    def OUT_stay1_run(self):

        Out_stay1_shuttle_IFR = GPIO_CHIP_6.Input(4,'A');
        self.OUT_stay1_shuttle_IFR(Out_stay1_shuttle_IFR);

    def OUT_stay2_shuttle_IFR(self,out_stay2_shuttle_IFR):
        
        while out_stay2_shuttle_IFR == 1:
            print("目前沒有偵測到貨物");
            out_stay2_shuttle_IFR = GPIO_CHIP_6.Input(6,'A');
            if out_stay2_shuttle_IFR == 0:
                print("偵測到貨物");
                time.sleep(2);
                print("dc5V 開始轉動");
                self.OUT_stay2_dc5V_start();
                Out_stay2_ele_IFR = GPIO_CHIP_6.Input(7,'A');
                self.OUT_stay2_ele_IFR(Out_stay2_ele_IFR);

    def OUT_stay2_ele_IFR(self,out_stay2_ele_IFR):
        
        while out_stay2_ele_IFR == 1:
            out_stay2_ele_IFR = GPIO_CHIP_6.Input(7,'A');           
            if out_stay2_ele_IFR == 0:
                print("dc5V 停止轉動");
                time.sleep(0.5);
                self.OUT_stay2_dc5V_stop();

    def OUT_stay2_run(self):

        Out_stay2_shuttle_IFR = GPIO_CHIP_6.Input(6,'A');
        self.OUT_stay2_shuttle_IFR(Out_stay2_shuttle_IFR);

    def OUT_stay3_shuttle_IFR(self,out_stay3_shuttle_IFR):
        
        while out_stay3_shuttle_IFR == 1:
            print("目前沒有偵測到貨物");
            out_stay3_shuttle_IFR = GPIO_CHIP_6.Input(6,'B');
            if out_stay3_shuttle_IFR == 0:
                print("偵測到貨物");
                time.sleep(2);
                print("dc5V 開始轉動");
                self.OUT_stay3_dc5V_start();
                out_stay3_ele_IFR = GPIO_CHIP_6.Input(7,'B');
                self.OUT_stay3_ele_IFR(out_stay3_ele_IFR);

    def OUT_stay3_ele_IFR(self,out_stay3_ele_IFR):
        
        while out_stay3_ele_IFR == 1:
            out_stay3_ele_IFR = GPIO_CHIP_6.Input(7,'B');           
            if out_stay3_ele_IFR == 0:
                print("dc5V 停止轉動");
                time.sleep(0.5);
                self.OUT_stay3_dc5V_stop();

    def OUT_stay3_run(self):

        Out_stay3_shuttle_IFR = GPIO_CHIP_6.Input(6,'B');
        self.OUT_stay3_shuttle_IFR(Out_stay3_shuttle_IFR);

    def step12():
        p = pwm.set_pwm(12,0,3072);

    def OUT_ele_Stepr12V_up1(self):
        
        SPR2 = 1500;
        # SPR2 = 6500(second floor); 
        step_count2 = SPR2;
        delay2 = 0.00001;
        GPIO_CHIP_5.output(7, 1,'B');
        pwm.set_pwm_freq(800);
        schedule.every(0.1).seconds.do(self.step12)

        count = 1;
        while count < 31:
            schedule.run_pending();
            time.sleep(0.1263);
            count = count +1;
        pwm.set_pwm(12,0,0);

    def OUT_ele_Stepr12V_down1(self):
        
        SPR2 = 1500;
        # SPR2 = 5450;
        step_count2 = SPR2;
        delay2 = 0.00001;                         
        GPIO_CHIP_5.output(7, 0,'B');
        pwm.set_pwm_freq(800);
        schedule.every(0.1).seconds.do(self.step12)

        count = 1;
        while count < 31:
            schedule.run_pending();
            time.sleep(0.1263);
            count = count +1;
        pwm.set_pwm(12,0,0);
        
        time.sleep(2);

    def OUT_ele_Stepr12V_up2(self):
        
        SPR2 = 1500;
        step_count2 = SPR2;
        delay2 = 0.00001;
        GPIO_CHIP_5.output(7, 1,'B');
        pwm.set_pwm_freq(800);
        schedule.every(0.1).seconds.do(self.step12)

        count = 1;
        while count < 64:
            schedule.run_pending();
            time.sleep(0.1263);
            count = count +1;
        pwm.set_pwm(12,0,0);

    def OUT_ele_Stepr12V_down2(self):
        
        SPR2 = 1500;
        step_count2 = SPR2;
        delay2 = 0.00001;
        GPIO_CHIP_5.output(7, 0,'B');
        pwm.set_pwm_freq(800);
        schedule.every(0.1).seconds.do(self.step12)

        count = 1;
        while count < 64:
            schedule.run_pending();
            time.sleep(0.1263);
            count = count +1;
        pwm.set_pwm(12,0,0);

    def OUT_ele_Stepr12V_up3(self):
        
        SPR2 = 1500;
        step_count2 = SPR2;
        delay2 = 0.00001;
        GPIO_CHIP_5.output(7, 1,'B');
        pwm.set_pwm_freq(800);
        schedule.every(0.1).seconds.do(self.step12)

        count = 1;
        while count < 97:
            schedule.run_pending();
            time.sleep(0.1263);
            count = count +1;
        pwm.set_pwm(12,0,0);

    def OUT_ele_Stepr12V_down3(self):
        
        SPR2 = 1500;
        step_count2 = SPR2;
        delay2 = 0.00001;
        GPIO_CHIP_5.output(7, 0,'B');
        pwm.set_pwm_freq(800);
        schedule.every(0.1).seconds.do(self.step12)

        count = 1;
        while count < 97:
            schedule.run_pending();
            time.sleep(0.1263);
            count = count +1;
        pwm.set_pwm(12,0,0);

    def OUT_ele_Stepr5V_push(self):
            
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
                GPIO_CHIP_5.output(pin, 0,'A');
            SEQUENCE_COUNT = len(SEQUENCE); 
            PINS_COUNT = len(STEPPER_5v_PINS);
            sequence_index = 0; 
            direction = 1; 
            steps = 0;
            count = 1;
            print("平台準備推動貨物");
            
            while True:

                for pin in range(0, PINS_COUNT):
                    GPIO_CHIP_5.output(STEPPER_5v_PINS[pin], SEQUENCE[sequence_index][pin],'A');#GPIO.output(代表各個角位，)
                steps += direction;
               
                sequence_index += direction;
                sequence_index %= SEQUENCE_COUNT;

                count += 1;
                if count >=7900:
                    break;
                time.sleep(0.0014);

    def OUT_ele_Stepr5V_back(self):
        
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
            GPIO_CHIP_5.output(pin, 0,'A');
        SEQUENCE_COUNT = len(SEQUENCE); 
        PINS_COUNT = len(STEPPER_5v_PINS);
        sequence_index = 0; 
        direction = 1; 
        steps = 0;
        count = 1;
        print("平台準備收回");
        
        while True:

            for pin in range(0, PINS_COUNT):
                GPIO_CHIP_5.output(STEPPER_5v_PINS[pin], SEQUENCE[sequence_index][pin],'A');#GPIO.output(代表各個角位，)
            steps += direction;

            sequence_index += direction;
            sequence_index %= SEQUENCE_COUNT;

            count += 1;
            if count >=7900:
                break;
            time.sleep(0.0014);

    def OUT_cvr_dc12V_start(self):
        
        GPIO_CHIP_5.output(3,1,'B');
        GPIO_CHIP_5.output(2,0,'B');
        time.sleep(1);

    def OUT_cvr_dc12V_stop(self):
        
        GPIO_CHIP_5.output(3,0,'B');
        GPIO_CHIP_5.output(2,0,'B');
        time.sleep(1);

    def OUT_stay1_servo(self):
        time.sleep(1);
        
    def OUT_stay2_servo(self):
        
        for i in np.arange(60,-50,-0.4):
        
            self.out_STAY3_Servo5V.value = math.sin(math.radians(i));
            time.sleep(0.001);
        
        time.sleep(1.5);
        
        for i in np.arange(-50,60,0.4):

            self.out_STAY3_Servo5V.value = math.sin(math.radians(i));
            time.sleep(0.0005);
            
    def OUT_stay3_servo(self):
        
        for i in np.arange(60,-50,-0.4):
        
            self.out_STAY2_Servo5V.value = math.sin(math.radians(i));
            time.sleep(0.0002);
        
        time.sleep(1.5);
        
        for i in np.arange(-50,60,0.4):

            self.out_STAY2_Servo5V.value = math.sin(math.radians(i));
            time.sleep(0.002);
            
    def OUT_stay2_servo_zero(self):
        
        for i in np.arange(59,60,0.4):

            self.out_STAY3_Servo5V.value = math.sin(math.radians(i));
            time.sleep(0.0005);
        
    def OUT_stay3_servo_zero(self):
        
        for i in np.arange(59,60,0.4):

            self.out_STAY2_Servo5V.value = math.sin(math.radians(i));
            time.sleep(0.0013);
            
    def OUT_run(self,Io):

        time.sleep(0.1);
        Io = int(Io);

        while Io == 0:

            out_stay1_ele_IFR = GPIO_CHIP_6.Input(5,'A');
            out_stay2_ele_IFR = GPIO_CHIP_6.Input(7,'A');
            out_stay3_ele_IFR = GPIO_CHIP_6.Input(7,'B');

            if out_stay1_ele_IFR ==0:

                print('暫1升降sensor偵測到');

                self.OUT_ele_Stepr12V_up1();
                time.sleep(1);

                self.OUT_stay1_dc5V_start();
                time.sleep(3);

                self.OUT_stay1_servo();
                time.sleep(1);

                self.OUT_stay1_dc5V_stop();
                self.OUT_ele_Stepr12V_down1();
                self.OUT_ele_Stepr5V_push();
                self.OUT_ele_Stepr5V_back();

                time.sleep(1);
                self.OUT_cvr_dc12V_start();
                
                time.sleep(2);
                self.OUT_cvr_dc12V_stop();

                break;

            if out_stay2_ele_IFR ==0:
                print('暫2升降sensor偵測到');
                self.OUT_ele_Stepr12V_up2();
                time.sleep(1);
                self.OUT_stay2_dc5V_start();
                time.sleep(3);
                self.OUT_stay2_servo();
                time.sleep(1);
                self.OUT_stay2_dc5V_stop();
                self.OUT_ele_Stepr12V_down2();
                self.OUT_ele_Stepr5V_push();
                self.OUT_ele_Stepr5V_back();
                time.sleep(1);
                self.OUT_cvr_dc12V_start();
                time.sleep(2);
                self.OUT_cvr_dc12V_stop();
                break;

            if out_stay3_ele_IFR ==0:
                print('暫3升降sensor偵測到');
                self.OUT_ele_Stepr12V_up3();
                time.sleep(1);
                self.OUT_stay3_dc5V_start();
                time.sleep(3);
                self.OUT_stay3_servo();
                time.sleep(1);
                self.OUT_stay3_dc5V_stop();
                self.OUT_ele_Stepr12V_down3();
                self.OUT_ele_Stepr5V_push();
                self.OUT_ele_Stepr5V_back();
                time.sleep(1);
                self.OUT_cvr_dc12V_start();
                time.sleep(2);
                self.OUT_cvr_dc12V_stop();
                break;
            



