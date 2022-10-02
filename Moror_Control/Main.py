from classIN_shuttle import*
from classIN_part2 import*
from classIN import*
from classINITIALIZE import*
from classOUT import*

IN = initialize();

F1 = inPart1();
ST = inPart2();
SH = Shuttle();
OT = outPart1();

def In_whole(posi):
    
    Ro = int(posi[0]);
    IN.initial();
    F1.IN_part1_run(Ro);
    ST.In_stay(Ro);

def Out_whole(posi):
    
    IN.initial();
    OT.OUT_run();
