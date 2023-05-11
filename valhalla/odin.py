import os
import time
import winsound


def anna_runtua(n):
    for _ in range(n):
        winsound.Beep(3000, 100)

class Runtu(Exception):
    def __init__(self, msg):
        self.message = """                                                                                
                                                                                
             @@                                      @@@@           @@@,        
           @@@@@@                                    @@@@           @@@         
        @@@@    @@@@       @@@                @@     /@@%           @@@         
     ,@@@&        .@@@     @@@@@@.         @@@@@      @@(     %@@   @@@         
     @@@@          @@@@    @@@ @@@@@(   @@@&  @@      @@(      @@@@@@@@         
       *@@@@    .@@@.      @@@    /@@@@@*     @@     /@@(          @@@@         
          @@@@@@@@         @@@   %@@@ @@@@@   @@*    /@@@           @@@@@@@     
           %@@@@@*         @@@@@@@       @@@@@@@*    &@@@           @@@  @@@@   
         @@@@  @@@@@       @@@@             ,@@@*    @@@@           @@@         
      @@@@@      ,@@@@@    @                    @    @@@@           @@@         
      @@@           @@.                              @@@@           @@@,        
                                                                                
                                                                                """
        self.message += f"\nJuuso, olet pettänyt odotukseni! Ota rangaistuksesi, kulauta juomasi ja palaa koodin ääreen viisaampana!\n"
        super().__init__(self.message)
        anna_runtua(3)
