#!/usr/local/bin python
#coding: utf-8

from pynput.keyboard import Key, Controller, KeyCode
import win32api
import win32con
import os
import time

class Prog(object):
    def __init__(self):
        self.version = "0.1.0"
        self.kb = Controller()
        self.stamina = 120
        self.cost = 30
        self.spend = 180

        self.newCome()
        self.waitSw(10)
        self.autoReview()

    def keyevent(self, vkcode, ssm):
        win32api.keybd_event(vkcode | vkcode, ssm, 0, 0)
        win32api.keybd_event(vkcode | vkcode, ssm, win32con.KEYEVENTF_KEYUP, 0)
        

    def newCome(self):
        print("****Arknights Battlebot****")
        print(" Version: %s Author: Lappland\n" % self.version)

        print("""
        -----------------------------------------------\n
        """)

        sta = input("Please input your current STAMINA(0-999, default 120): ")

        try:
            sta = int(sta)

            if sta >= 0 and sta <= 999:
                self.stamina = sta

        except:
            pass

        print("Stamina read: %s\n" % self.stamina)

        co = input("Please input your current mission COST(0-50, default 30): ")

        try:
            co = int(co)

            if co >= 0 and co <= 50:
                self.cost = co

        except:
            pass

        print("Cost read: %s\n" % self.cost)

        sp = input("Please input your current mission SPEND(1-60, default 3): ")

        try:
            sp = float(sp)

            if sp >= 1 and co <= 60:
                self.spend = sp * 60

        except:
            pass

        print("Spend read: %s\n" % self.spend)

    def waitSw(self, sec):
        print("Press any key to START...")
        os.system("pause")

        while sec >= 1:
            print("\nCountdown %s\n" % sec)
            
            time.sleep(1)
            sec -= 1

    def autoReview(self):
        ct = 0
        while self.stamina >= self.cost:
            ct += 1
            print("Loop %s, Stamina %s\n" % (ct, self.stamina))

            print("\tMission prepare")
            self.keyevent(83, 31)#S

            time.sleep(4)

            print("\tMission start")
            self.keyevent(79, 24)#O

            time.sleep(self.spend)

            print("\tMission end\n")
            self.keyevent(66, 48)#B

            time.sleep(4)
            self.stamina -= self.cost
        
if __name__ == "__main__":
    prog = Prog()

    