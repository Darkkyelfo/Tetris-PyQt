import os

os.popen("pyuic4 campoTetris.ui -o campoTetris.py -x")

os.popen("pyrcc4 -o blocos_rc.py blocos.qrc")
