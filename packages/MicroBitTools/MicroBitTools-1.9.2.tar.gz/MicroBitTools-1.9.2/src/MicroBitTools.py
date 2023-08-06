import os
import shutil
import uflash
import requests
import serial
import microfs
import time

readymicrobithexurl = "https://cdn.discordapp.com/attachments/249832375272472576/648205212280160256" \
                      "/microbitserialsystem.hex "

readymicrobithexurl = "https://www.dropbox.com/s/80yye8jt7h33cwx/microbitserialsystem.hex?dl=1"


class InternalTools:
    def yntoboolean(data="no"):
        data = data.lower()
        if data == "y":
            return True
        elif data == "n":
            return False
        else:
            return "ERROR: \nInput was not either y or n"
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'


def flash(pythonfile):
    drive = InternalTools.get_mb()
    tryn = 0
    while drive == "":
        if tryn == 1:
            print("Please plug in a microbit")
        tryn = tryn + 1
        input()
        drive = InternalTools.get_mb()

    pyfilenoext = pythonfile[:-3]
    os.system("cd " + os.getcwd())
    os.system('py2hex "' + pythonfile + '"')
    print("Moving to microbit.")
    shutil.move(pyfilenoext + ".hex", drive)
    print("Done!")


def flashF(folder):
    import microfs, uflash, os, time
    # SerialSystem.ser.close()

    print("MicroBit is at: " + microfs.find_microbit()[0] + "\nMicroBit directory is at: " + uflash.find_microbit())
    try:
        mfiles = microfs.ls()
    except OSError as e:
        print(str(
            e) + "\nMicrobit is probably calibrating, calibrate and then try again\nIf it still does not work try to "
                 "replug your microbit or close other programs that is accessing your microbit")
        return "Could not write"
    print("Removing old stuff: " + str(mfiles))
    for file in mfiles:
        microfs.rm(file)

    files = os.listdir(folder)
    print("Flashing new stuff: " + str(files))
    for file in files:
        microfs.put(folder + "\\" + file)

    print("Flashed new stuff: " + str(microfs.ls()) + "\n")

    time.sleep(0.1)
    print("Done!" + "\n" +
          "Don't forget to name your main file \"main.py\"" + "\n" + InternalTools.bcolors.BOLD +
          "Reset your MicroBit to apply changes!"
          )
    # except OSError as e:
    #     exit(str(e) + "\n\nReplug microbit")
    # except TypeError as e:
    #     exit(str(e) + "\n\nReplug microbit")
    # SerialSystem.ser.open()


def export(arg1):
    flash(arg1)


class SerialSystem:
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = "COM3"

    microbitpath = uflash.find_microbit()

    # FIXA
    def readyMicroBit(self, printb=False):
        # shutil.copyfile(os.getcwd() + "\\src\\" + "microbitserialsystem.hex", self.microbitpath+"SerialSystem.hex")
        # shutil.copy
        if printb:
            print("Downloading HEX")
        url = readymicrobithexurl
        r = requests.get(url)
        if printb:
            print("Downloaded HEX")
            print("Fixing HEX")
        content = ""
        # contentb = r.content
        # contentb = str(contentb)
        # contentb = contentb[:-1]
        # contentb = contentb[2:]
        # contentsplit = contentb.split("\\n")
        # for i in contentsplit:
        #     content = content + i + "\n"
        content = r.content.decode("UTF-8")
        if printb:
            print("Fixed HEX\n" + content)
            print("Moving HEX to microbit")

        try:
            file = open("SerialSystem.hex", "w")

            file.write(content)

            file.close()

            shutil.move("SerialSystem.hex", uflash.find_microbit() + "SerialSystem.hex")
        except shutil.Error as e:
            print(e)
            print("SerialSystem hex already installed")
            os.remove(os.getcwd() + "\\SerialSystem.hex")
        if printb:
            print("Moved HEX to microbit")

    def display(self):
        self.ser.open()
        self.ser.writeline("")
        self.ser.close()

    def read(self):
        try:
            self.ser.open()
        except serial.serialutil.SerialException as e:
            print(str(e))
        try:
            mbd = str(self.ser.readline())
        except serial.serialutil.SerialException:
            return {"error": "Can not find MicroBit"}
        except IndexError:
            return {"error": "Unknown error"}

        try:
            mbdf = mbd[2:]
            # mbdf = mbdf.replace(" ", "")
            mbdf = mbdf.replace("'", "")
            mbdf = mbdf.replace("\\r\\n", "")
            mbdf = mbdf.replace("\\xc2", "")
        except IndexError:
            return {"error": "Could not read!"}

        if mbdf.startswith("}"):
            mbdf = mbdf[1:]
            mbdfsplit = mbdf.split("\\xa7")
            try:
                temp = int(mbdfsplit[0])
                try:
                    brightness = int(mbdfsplit[1])
                except ValueError:
                    brightness = ""
                ButtonA = InternalTools.yntoboolean(mbdfsplit[2][2:])
                ButtonB = InternalTools.yntoboolean(mbdfsplit[3][2:])
                CmpsH = int(mbdfsplit[4])

                dicmbd = {
                    "temp": temp,
                    "brightness": brightness,
                    "Buttons": {
                        "A": ButtonA,
                        "B": ButtonB
                    },
                    "CompassHeading": CmpsH
                }
                self.ser.close()
                return dicmbd
            except IndexError:
                self.ser.close()
                return {"error": "Could not read!"}
        else:
            self.ser.close()
            return {"error": "Could not read!"}


def test():
    print("SUCCESS")
