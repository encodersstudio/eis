import csv, os
import urllib, urllib.request

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QLabel, QProgressBar
from downloadimage import download_images
from converter import run_converter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Encoders' Image Studio")

        layout = QVBoxLayout()

        self.filename = ""
        self.t_num = 0
        self.num = 0

        self.upload_button = QPushButton("Upload CSV")
        self.upload_button.clicked.connect(self.upload_file)

        self.label = QLabel("Upload CSV containing image URLs")

        self.download_images_button = QPushButton("Download Images")
        self.download_images_button.setEnabled(False)
        self.download_images_button.clicked.connect(self.download_img)

        self.entries_label = QLabel()
        self.progress_label = QLabel()
        self.convert_label = QLabel()

        self.convert_button = QPushButton("Convert to Webp")
        self.convert_button.setEnabled(False)
        self.convert_button.clicked.connect(self.convert_to_webp)

        layout.addWidget(self.upload_button)
        layout.addWidget(self.label)
        layout.addWidget(self.download_images_button)
        layout.addWidget(self.entries_label)
        layout.addWidget(self.progress_label)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.convert_label)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
    def upload_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Upload CSV", "", "(*.csv)")
        if file_name:
            self.label.setText(file_name[0])
            self.filename = file_name[0]
            self.download_images_button.setEnabled(True)
            read_file = csv.reader(open(self.filename))
            self.t_num = len(list(read_file))
            self.entries_label.setText(f"Total Images: {self.t_num}")
        return file_name

    def download_img(self):

        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        working_directory = f"{desktop}/images_jpgs"
        if not os.path.exists(working_directory):
            os.makedirs(working_directory)
        # download_images(self.filename, self.num)
        with open("{0}".format(self.filename), 'r') as csvfile:
            # iterate on all lines

            i = 0
            for line in csvfile:
                # splitted_line = line.split(',')
                # check if we have an image URL
                if line != '' and line != "\n":
                    urllib.request.urlretrieve(line, f"{working_directory}/image{str(i+1)}.jpg")
                    # print("Image saved for {0}".format(line))
                    i += 1

                # else:
                    # print("No result for {0}".format(line))
            self.progress_label.setText(f"{i}/{self.t_num} Images saved.")
            self.download_images_button.setEnabled(False)
        self.convert_button.setEnabled(True)

    def convert_to_webp(self):
        run_converter()
        self.convert_label.setText("Images converted to webp")
        self.convert_button.setEnabled(False)


