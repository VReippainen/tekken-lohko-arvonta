import os
import time
from pygame import mixer

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
        mixer.init()
        mixer.music.load("valhalla/runtu.mp3")
        mixer.music.play()
        time.sleep(18)
