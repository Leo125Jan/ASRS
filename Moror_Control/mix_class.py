import cv2
import numpy as np
import pyzbar
from pyzbar.pyzbar import decode
import time as t
import datetime as dt
import mysql.connector as mc
import random as r
import tkinter as tk
import threading as th

# 視窗設定
cap = cv2.VideoCapture(0);
cap.set(3,600); #ID 3 指window的高
cap.set(4,600); #ID 4 指window的寬

class Goods_Scan:

    def __init__(self,win):

        self.win = win;

    def confirm(self):

        mydb8 = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
        mycursor8 = mydb8.cursor();

        sql = "SELECT Code FROM ps WHERE Code = %s";
        code = mydata;
        value = (code,);

        mycursor8.execute(sql,value);
        result8 = mycursor8.fetchall();

        if len(result8) > 0:

            return True;

        else:

            return False;

    def start(self):

        global count;
        count = 1;
    
    def stop(self):
        
        global count;
        count = 0;

    def Scan(self):

        while True:
            
            global img;
            success,img = cap.read();

            for barcode in decode(img):

                global mydata;
                mydata = barcode.data.decode('utf-8');

                pts = np.array([barcode.polygon],np.int32);
                pts = pts.reshape((-1,1,2));
                cv2.polylines(img,[pts],True,(255,0,255),5);
                pts2 = barcode.rect;
                cv2.putText(img,mydata,(pts2[0]-50,pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2);

                if self.confirm() == True:

                    mess = "Authorized";
                    cv2.putText(img,mess,(pts2[0]+50,pts2[1]-20),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2);

                elif self.confirm() == False:

                    mess = "Unrecognized";
                    cv2.putText(img,mess,(pts2[0]+50,pts2[1]-20),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2);
                    
            cv2.imshow('Result',img);
            cv2.waitKey(50);
                    
            global count;
            
            if count == 0:
                
                cap.release();
                cv2.destroyAllWindows();
                
                break;
            
    def GUI(self,q1,q2):

        self.win = tk.Tk();
        self.win.title("Keyboard Detect");
        self.win.geometry("400x400");
        
        def arrange(q1,q2,ro,co):

            mydb3 = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
            mycursor3 = mydb3.cursor();
            mycursor3.execute("SELECT Code FROM ps ");
            result3 = mycursor3.fetchall();

            if len(result3) > 0 and len(result3) <= 4:

                st = 0;

                while st == 0:

                    ct = 0;
                    mydb4 = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
                    mydb5 = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
                    mydb6 = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");

                    mycursor4 = mydb4.cursor();
                    mycursor5 = mydb5.cursor();
                    mycursor6 = mydb6.cursor();

                    mycursor4.execute("SELECT Ro FROM ps");
                    mycursor5.execute("SELECT Co FROM ps");
                    mycursor6.execute("SELECT ID FROM ps ORDER BY ID DESC");

                    result4 = mycursor4.fetchall();
                    result5 = mycursor5.fetchall();
                    result6 = mycursor6.fetchone();

                    for count in range(0,len(result4)-1):

                        if(result4[len(result4)-1] == result4[count] and result5[len(result5)-1] == result5[count]):

                            ro = str(r.randint(1,3));
                            co = str(r.randint(1,3));
                            Id = str(result6[0]);
                            sql = "UPDATE ps SET  Ro = %s , Co = %s WHERE ID = %s";
                            value = (ro,co,Id);
                            mycursor4.execute(sql,value);
                            mydb4.commit();

                        else:

                            ct = ct + 1;

                    if ct == len(result4)-1:

                        st = 1;
                        posi = (ro,co);
                        q1.put(posi);
                        q2.put(posi);
                        break;

        def insert(q1,q2):

            mydb = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
            mycursor = mydb.cursor();
            mycursor.execute("SELECT Code FROM ps");
            result = mycursor.fetchall();
            
            global mydata;

            if len(result) < 4:

                ro = str(r.randint(1,3));
                co = str(r.randint(1,3));
                Id = mydata;

                mydb1 = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
                mycursor1 = mydb1.cursor();
                sql = "INSERT INTO ps(Code,Ro,Co) VALUES(%s,%s,%s)";
                value = (Id,ro,co);
                mycursor1.execute(sql,value);
                mydb1.commit();

            arrange(q1,q2,ro,co);

            t.sleep(0.5);

        def delete(q1,q2):

            mydb = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
            mycursor = mydb.cursor();
            mycursor.execute("SELECT Code FROM ps");
            result = mycursor.fetchall();
            
            global mydata;

            if len(result) > 0 and len(result) <= 4:
                
                mydb1 = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
                mycursor1 = mydb1.cursor();

                sql_r = "SELECT Ro FROM ps WHERE Code = %s";
                value_r = (mydata,);
                mycursor1.execute(sql,value_r);
                result_r = mycursor1.fetchone();

                sql_c = "SELECT Co FROM ps WHERE Code = %s";
                value_c = (mydata,);
                mycursor1.execute(sql,value_c);
                result_c = mycursor1.fetchone();

                posi = (result_r,result_c);
                q1.put(posi);
                q2.put(posi);

                mydb2 = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
                mycursor2 = mydb2.cursor();

                sql = "DELETE FROM ps WHERE Code = %s";
                value = (mydata,);
                mycursor2.execute(sql,value);
                mydb2.commit();

            t.sleep(1);

        def In_record():

            mydb = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
            mycursor = mydb.cursor();
            mycursor.execute("SELECT Code FROM ps");
            result = mycursor.fetchall();
            
            global mydata;

            if len(result) < 4:

                mydb9 = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
                mycursor9 = mydb9.cursor();

                sql = "UPDATE wine SET TIMEIN = %s ,LOGDATE = %s , STATUS = %s WHERE Code = %s"; 

                code = mydata;
                localtime = t.localtime();
                logdate = dt.date.today();
                status = "0";
                value = (localtime,logdate,status,code);

                mycursor9.execute(sql,value);
                mydb9.commit();

        def Out_record():

            mydb = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
            mycursor = mydb.cursor();
            mycursor.execute("SELECT Code FROM ps");
            result = mycursor.fetchall();
            
            global mydata;

            if len(result) <= 4:

                mydb7 = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
                mycursor7 = mydb7.cursor();
                sql = "SELECT * FROM wine WHERE Code = %s AND LOGDATE = %s AND STATUS = %s ";

                code = mydata;
                logdate = dt.date.today();
                status = "0";
                value = (code,logdate,status);

                mycursor7.execute(sql,value);
                result7 = mycursor7.fetchall();

                if len(result7) > 0:

                    mydb8 = mc.connect(host = "localhost", user = "To", passwd = "SQL123", database = "qrcode");
                    mycursor8 = mydb8.cursor();

                    sql = " UPDATE wine SET TIMEOUT = %s , STATUS = %s WHERE Code = %s AND LOGDATE = %s ";

                    localtime = t.localtime();
                    status = "1";
                    code = mydata;
                    logdate = dt.date.today();
                    value = (localtime,status,code,logdate);

                    mycursor8.execute(sql,value);
                    mydb8.commit();

        def key_detect(event):

            test = tk.Label(text="You press the key: " + event.char );
            test.pack();
            global img;
                
            if event.char == "a":
                
                cv2.rectangle(img,(0,225),(700,275),(0,255,0),cv2.FILLED);
                cv2.putText(img,"Data Saved",(180,250),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),3);
                cv2.imshow("Result",img);
                
                q1.put(1);
                q2.put(1);
                insert(q1,q2);
                In_record();

                cv2.waitKey(500);
                
            elif event.char == "d":
                
                cv2.rectangle(img,(0,225),(700,275),(0,255,0),cv2.FILLED);
                cv2.putText(img,"Data deleted",(180,250),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),3);
                cv2.imshow("Result",img);
                
                q1.put(0);
                q2.put(0);
                delete(q1,q2);
                Out_record();

                cv2.waitKey(500);
                
            elif event.char == "q":

                tes = tk.Label(text="Stop");
                tes.pack();

                self.win.destroy();
                self.stop();
                
        self.win.bind("<KeyPress>",key_detect);
        self.win.mainloop();

    def simu(self,q1,q2):

        self.start();
        t1 = th.Thread(target = self.GUI, args = (q1,q2));
        t2 = th.Thread(target = self.Scan);
        t1.start();
        t2.start();
        t1.join();
        t2.join();
