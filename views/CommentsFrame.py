from PyQt5 import QtWidgets, QtCore, QtGui
from database.Post import Post as PostDB

class CommentsFrame(QtWidgets.QFrame):

    parent = None
    width = 500
    height = 600
    position = [0, 0]
    db_conn = None
    user_id = 0
    post_id = 0
    data = []

    def __init__(self, parent, conn, user, post):
        super().__init__(parent)

        self.parent = parent
        self.db_conn = conn
        self.user_id = user
        self.post_id = post
        self.setup()
        self.show_comments()

    def clear_comments(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clear_comments(child.layout(), None)

    def show_comments(self):
        self.data = PostDB.get_comments(self.db_conn, self.post_id)

        for comment in self.data:
            label = QtWidgets.QLabel(comment[2])
            label.setFixedHeight(100)

            self.main_layout.addWidget(label)

    def send_comment(self):
        text = self.new_comment_field.text()

        if text != '':
            PostDB.send_comment(self.db_conn, self.post_id, self.user_id, text)
            self.clear_comments(self.main_layout)
            self.show_comments()

    def close_frame(self, event):
        self.close()

    def setup(self):
        self.position = [(self.parent.width() - self.width)/2, (self.parent.height() - self.height)/2]

        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.setAlignment(QtCore.Qt.AlignRight)
        self.frame_layout = QtWidgets.QVBoxLayout(self)

        self.setFixedSize(self.width, self.height)
        self.setStyleSheet('background-color: #FFFFFF')
        self.move(self.position[0], self.position[1])

        self.close_label = QtWidgets.QLabel()
        self.close_label.setFixedSize(25, 25)
        self.close_label.setPixmap(QtGui.QPixmap('assets/close_icon.png'))
        self.close_label.setScaledContents(True)
        self.close_label.mousePressEvent = self.close_frame
        self.header_layout.addWidget(self.close_label)

        self.main_content = QtWidgets.QWidget()
        self.main_content.setStyleSheet('background-color: #e6e6e6')
        self.main_layout = QtWidgets.QVBoxLayout(self.main_content)

        self.comments_scrollarea = QtWidgets.QScrollArea()
        self.comments_scrollarea.setFixedSize(self.width - 50, self.height // 2)
        self.comments_scrollarea.setWidgetResizable(True)
        self.comments_scrollarea.setAlignment(QtCore.Qt.AlignCenter)
        self.comments_scrollarea.setWidget(self.main_content)

        self.new_comment_frame = QtWidgets.QWidget(self)
        self.new_comment_frame.setFixedSize(self.width - 50, self.height // 2)
        self.new_comment_layout = QtWidgets.QHBoxLayout(self.new_comment_frame)

        self.new_comment_field = QtWidgets.QLineEdit()
        self.new_comment_button = QtWidgets.QPushButton(text='OK')
        self.new_comment_button.clicked.connect(self.send_comment)

        self.new_comment_layout.addWidget(self.new_comment_field)
        self.new_comment_layout.addWidget(self.new_comment_button)

        self.frame_layout.addLayout(self.header_layout)
        self.frame_layout.addWidget(self.comments_scrollarea)
        self.frame_layout.addWidget(self.new_comment_frame)
