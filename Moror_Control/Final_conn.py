import multiprocessing as mp
import time as t
from mix_class import Goods_Scan
from Main import In_whole
from classIN_shuttle import *
from classINITIALIZE import *

# From class import function
I = Goods_Scan("win");
S = Shuttle();
IN = initialize();

# Main processing function

if __name__ == "__main__":
    
    IN.clean();
    IN.initial();
    
    # Define

    q1 = mp.Queue();
    q2 = mp.Queue();
    
    Scan_process = mp.Process(target = I.simu,args=(q1,q2));
    Shuttle_process = mp.Process(target = S.shuttle_thread,args = (q2,));

# Processes start

    Scan_process.start();
    Shuttle_process.start();

    while True:

        if not q1.empty():

            check = q1.get();

            if check == 1:
                
                posi = q1.get();
                In_process = mp.Process(target = In_whole,args=(posi,));
                In_process.start();

            elif check == 0:
                
                posi = q1.get();
                Out_process = mp.Process(target = Out,args=(posi,));
                Out_process.start();

        if not Scan_process.is_alive:

            break;

        t.sleep(1.5);

    Scan_process.terminate();
    Shuttle_process.terminate();
    In_process.terminate();
    Out_process.terminate();
    
    IN.clean();
