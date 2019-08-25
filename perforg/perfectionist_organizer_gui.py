#Импорт необходимых библиотек
import os
import re
import getpass
import shutil
import platform
import sys
from PyQt5 import QtWidgets
import design
#Проверка операционной системы, которой пользуется юзер
type_os = platform.system()
#Создание словарей с расширениями файлов и папкой, куда их нужно перекинуть
video_folder = {".3gp" : "Видео/", ".avi" : "Видео/", ".flv" : "Видео/", ".m4v" : "Видео/", ".mkv" : "Видео/", ".mov" : "Видео/", ".mp4" : "Видео/", ".wmv" : "Видео/", ".webm" : "Видео/"}
music_folder = {".mp3" : "Музыка/", ".aac": "Музыка/", ".flac" : "Музыка/", ".mpc" : "Музыка/", ".wma" : "Музыка/", ".wav" : "Музыка/"}
pic_folder = {".raw" : "Изображения/", ".jpg" : "Изображения/", ".tiff" : "Изображения/", ".psd" : "Изображения/", ".bmp" : "Изображения/", ".gif" : "Изображения/", ".png" : "Изображения/", ".jp2" : "Изображения/", ".jpeg" : "Изображения/"}
doc_folder = {".doc" : "Документы/", ".docx" : "Документы/", ".txt" : "Документы/", ".rtf" : "Документы/", ".pdf" : "Документы/", ".fb2" : "Документы/", ".djvu" : "Документы/", ".xls" : "Документы/", ".xlsx" : "Документы/", ".ppt" : "Документы/", ".pptx" : "Документы/", ".mdb" : "Документы/", ".accdb" : "Документы/", ".rar" : "Документы/", ".zip" : "Документы/", ".7z" : "Документы/"}
#Определяем имя пользователя в системе
usermane = getpass.getuser()
class ExampleApp(QtWidgets.QMainWindow, design.Ui_main_window):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.start_button.clicked.connect(self.move_files)
    def move_files(self):
        user_downloads_path = self.label_downloads_answer.text()
        default_path_d_win = r"C:/Users/" + usermane + r"/" + user_downloads_path + r"/"
        default_path_u_win = r"C:/Users/" + usermane + r"/"
        downloads_path_win = os.listdir(r"C:/Users/" + usermane + r"/" + user_downloads_path)
        for music_format in music_folder:
            for name_file in downloads_path_win:
                if name_file.endswith(music_format):
                    result = name_file.split(str(music_format), 1)
                    os.rename(default_path_d_win + result[0] + music_format, default_path_u_win + "Music" + r"/" + result[0] + music_format)
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()