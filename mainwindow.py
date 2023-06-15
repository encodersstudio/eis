import csv, os
import urllib, urllib.request
from urllib.parse import urlparse

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
        self.fd_name = ""

        self.upload_button = QPushButton("Upload CSV")
        self.upload_button.clicked.connect(self.upload_file)

        self.select_folder_button = QPushButton("Select Images Folder")
        self.select_folder_button.clicked.connect(self.select_folder)

        self.upload_label = QLabel("Upload CSV containing image URLs")
        self.select_folder_label = QLabel("Select folder containing images")

        self.download_images_button = QPushButton("Download Images")
        self.download_images_button.setEnabled(False)
        self.download_images_button.clicked.connect(self.download_img)

        self.entries_label = QLabel()
        self.progress_label = QLabel()
        self.convert_label = QLabel()

        self.convert_button = QPushButton("Convert to Webp")
        # self.convert_button.setEnabled(False)
        self.convert_button.clicked.connect(self.convert_to_webp)

        layout.addWidget(self.upload_label)
        layout.addWidget(self.upload_button)
        layout.addWidget(self.select_folder_label)
        layout.addWidget(self.select_folder_button)
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
            self.upload_label.setText(file_name[0])
            self.filename = file_name[0]
            self.download_images_button.setEnabled(True)
            read_file = csv.reader(open(self.filename))
            self.t_num = len(list(read_file))
            self.entries_label.setText(f"Total Images: {self.t_num}")
        return file_name

    def select_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_name:
            self.fd_name = folder_name
            self.select_folder_label.setText(folder_name)

    def download_img(self):
        # download_images(self.filename, self.num)
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        working_directory = f"{desktop}\downloaded_images"

        if not os.path.exists(working_directory):
            os.makedirs(working_directory)

        with open("{0}".format(self.filename), 'r') as csvfile:
            # iterate on all lines

            i = 0
            for line in csvfile:
                # splitted_line = line.split(',')
                # check if we have an image URL

                if line != '' and line != "\n":
                    f_name = urlparse(line)
                    urllib.request.urlretrieve(line, f"{working_directory}\{os.path.basename(f_name.path)}")
                    print("Image saved for {0}".format(line))
                    i += 1

                else:
                    print("No result for {0}".format(line))
            self.progress_label.setText(f"{i}/{self.t_num} Images saved.")
            self.download_images_button.setEnabled(False)
        self.fd_name = working_directory
        self.convert_button.setEnabled(True)

    def convert_to_webp(self):
        print(self.fd_name)
        run_converter(self.fd_name)
        self.convert_label.setText("Images converted to webp")
        # self.convert_button.setEnabled(False)


