import bear_kids_player
from PyQt5.QtWidgets import QApplication
from config_processing import get_config
import sys
def run_bear_kids_player():
    app = QApplication(sys.argv)
    player = bear_kids_player.VideoWindow()
    player.resize(680, 550)
    # showMaximized()
    # show()
    player.setStyleSheet("background-color:black;");
    player.showFullScreen()
    sys.exit(app.exec_())
