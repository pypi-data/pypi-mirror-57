from time import sleep
import sys
import os

from colorama import init
init(autoreset=True)


class setlist:
    def magenta(list):
        global magentawordlist
        magentawordlist = list
    def green(list):
        global greenwordlist
        greenwordlist = list
    def red(list):
        global redwordlist
        redwordlist = list


class appearance:
    def delay(delay):
        if not delay == None:
            sleep(float(delay))


def printc(colored, delay=None, skipline=None):
    firstrun = True
    global magentawordlist
    global greenwordlist
    global redwordlist
    global globalwordlist
    #### Usage: printcolored(texttoprint, True/False)
    b = len(colored)
    a = 0
    while a < b:

        if firstrun == True:
            if 'magentawordlist' in globals() or 'magentawordlist' in locals():
                pass
            else:
                magentawordlist = ['None']
                wordlistlenght = len(magentawordlist)
            if 'greenwordlist' in globals() or 'greenwordlist' in locals():
                pass
            else:
                greenwordlist = ['None']
                wordlistlenght = len(greenwordlist)

            if 'redwordlist' in globals() or 'redwordlist' in locals():
                pass

            else:
                redwordlist = ['None']
                wordlistlenght = len(redwordlist)


            if 'magentawordlist' in globals() or 'magentawordlist' in locals():
                wordlistlenght = len(magentawordlist)

            if 'greenwordlist' in globals() or 'greenwordlist' in locals():
                if wordlistlenght < len(greenwordlist):
                    wordlistlenght = len(greenwordlist)

            if 'redwordlist' in globals() or 'redwordlist' in locals():
                if wordlistlenght < len(redwordlist):
                    wordlistlenght = len(redwordlist)



            if 'magentawordlist' in globals() or 'magentawordlist' in locals():

                globalwordlist = str(magentawordlist)
                while len(magentawordlist) < wordlistlenght:
                    magentawordlist.append('None')

            if 'redwordlist' in globals() or 'redwordlist' in locals():

                globalwordlist = globalwordlist + str(redwordlist)
                while len(redwordlist) < wordlistlenght:
                    redwordlist.append('None')


            if 'greenwordlist' in globals() or 'greenwordlist' in locals():

                globalwordlist = globalwordlist + str(greenwordlist)
                while len(greenwordlist) < wordlistlenght:
                    greenwordlist.append('None')


        x = 0
        y = len(colored)
        while x < y:
            zz = 0
            zzz = wordlistlenght
            while zz < zzz:
                if magentawordlist[zz] in colored[a:a+len(magentawordlist[zz])]:
                    if not magentawordlist[zz] == 'None':
                        a = a + len(magentawordlist[zz])
                        q = 0
                        qq = len(magentawordlist[zz])
                        while q < qq:
                            oneletter = magentawordlist[zz]
                            oneletter = oneletter[q]
                            appearance.delay(delay); sys.stdout.write('\033[35m' + oneletter + ''); sys.stdout.flush()
                            q = q+1
                if greenwordlist[zz] in colored[a:a+len(greenwordlist[zz])]:
                    if not greenwordlist[zz] == 'None' :

                        a = a + len(greenwordlist[zz])
                        q = 0
                        qq = len(greenwordlist[zz])
                        while q < qq:
                            oneletter = greenwordlist[zz]
                            oneletter = oneletter[q]
                            appearance.delay(delay); sys.stdout.write('\033[32m' + oneletter + ''); sys.stdout.flush()
                            q = q+1

                if redwordlist[zz] in colored[a:a+len(redwordlist[zz])]:
                    if not redwordlist[zz] == 'None':

                        a = a + len(redwordlist[zz])
                        q = 0
                        qq = len(redwordlist[zz])
                        while q < qq:
                            oneletter = redwordlist[zz]
                            oneletter = oneletter[q]
                            appearance.delay(delay); sys.stdout.write('\033[31m' + oneletter + ''); sys.stdout.flush()
                            q = q+1

                    try:
                        if not colored[a] in globalwordlist:
                            appearance.delay(delay); sys.stdout.write('\033[39m' + colored[a] + ''); sys.stdout.flush()
                            a = a+1
                    except:
                        break


                    if magentawordlist[zz]  == 'None' or greenwordlist[zz]  == 'None' or redwordlist[zz]  == 'None':
                        c = 4
                        q = 1
                        nonetext = 'None'
                        a = a + len(nonetext)-1
                        while q < c:
                            appearance.delay(delay); sys.stdout.write('\033[39m' + nonetext[q] + ''); sys.stdout.flush()
                            q = q+1

                zz = zz+1
                
            x = x+1
        if not a < b:
            break
        
        appearance.delay(delay); sys.stdout.write(colored[a]); sys.stdout.flush()
        firstrun = False
        a = a+1
    if skipline == 'skipline':
        print()