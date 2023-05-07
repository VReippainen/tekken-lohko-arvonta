import os


def play_runtu_beeps(n):
    for _ in range(n):
        os.system("powershell.exe '[console]::beep(3000, 300)'")
        os.system("powershell.exe 'Start-Sleep -Seconds 0.1'")

class JuusoException(Exception):
    def __init__(self, msg):
        self.message = f"WTF Juuso, huikkaa!\n{msg}"
        super().__init__(self.message)
        play_runtu_beeps(3)
