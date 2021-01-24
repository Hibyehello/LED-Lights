import sys
import windowqt as winqt
import windowtk as wintk

try:
    import RPi.GPIO
    import windowqtrpi as rpiqt
    import windowtkrpi as rpitk
    gpio = 1
    print ("GPIO pins are enabled")
    try:
        import PyQt5.QtCore
        print ("Attempting to use PyQt5")
        qt = 1
        rpiqt.main()
    except:
        print ("PyQt5 is not installed")
        qt = 0
    if qt == 0:
        try:
            try:
                import tkinter
            except:
                import Tkinter
            print ("Using tkinter")
            rpitk.main()
        except:
            print ("Cannot run Program")
except:
    print ("No GPIO pins found, or Not a Raspberry pi")
    gpio = 0

if gpio == 0:
    try:
        import PyQt5.QtCore
        qt = 1
        print ("Attempting to use PyQt5")
        winqt.main()
    except ImportError:
        print ("PyQt5 is not Installed")
        qt = 0

if qt == 0:
    try:
        try:
            import tkinter
        except:
            import Tkinter
        print ("using tkinter")
        wintk.main()
    except ImportError:
        print ("tkinter is not installed")
