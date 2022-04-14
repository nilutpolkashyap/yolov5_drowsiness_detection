import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.Qt import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
    def keyboardEventReceived(self, event):
        if event.event_type == 'down':
            if event.name == 'f3':
                print('F3 pressed')
            elif event.name == 'f4':
                print('F4 pressed')

    def setGrabbing(self, enable):
        if enable:
            self.button.setText('stop')
            # on_press returns a hook that can be used to "disconnect" the callback
            # function later, if required
            self.hook = keyboard.on_press(self.keyboardEventReceived)
            self.showMinimized()
        else:
            self.button.setText('start')
            keyboard.unhook(self.hook)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())