from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

import sys, pyodbc

from app.sql import DataBase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"design\main_window.ui", self)
        self.setWindowTitle("DataBase")
        self.db = DataBase(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes; '
        'user=22200322; Database=DB_for_python_lessons;')
        # Объявление таблицы
        self.model_left = QStandardItemModel(self)
        self.leftTable.setModel(self.model_left)
        self.model_left.setHorizontalHeaderLabels(['ID', 'Имя', 'Номер телефона', 'Роль', 'Пароль', 'Хеш пароля'])
        self.load_data()

        self.model_right = QStandardItemModel(self)
        self.rightTable.setModel(self.model_right)
        self.model_right.setHorizontalHeaderLabels(['ID', 'Имя', 'Номер телефона', 'Роль', 'Пароль', 'Хеш пароля'])
        self.load_right_data()

        # Подключение кнопок
        self.addButton.clicked.connect(self.add_data_button)
        self.delButton.clicked.connect(self.delete)
        self.editButton.clicked.connect(self.edit_data_button)
        self.send_to_left.clicked.connect(self.send_to_left_Button)
        self.send_to_right.clicked.connect(self.send_to_right_Button)

    def add_to_right_table(self):
        self.add = AddDataWindow(self.db)
        self.add.setFixedSize(406, 279)
        self.add.data_added.connect(self.load_data)
        self.add.show()

    def send_to_left_Button(self):
        selected_index = self.rightTable.selectedIndexes()
        if not selected_index:
            QMessageBox.warning(self, 'Предупреждение', 'Пожалуйста, выберите строку для удаления.')
            return

        row_to_delete = selected_index[0].row()
        selected_user_id = self.model_right.item(row_to_delete, 0).text()
        selected_username = self.model_right.item(row_to_delete, 1).text()
        selected_user_last_name = self.model_right.item(row_to_delete, 2).text()
        selected_user_role = self.model_right.item(row_to_delete, 3).text()
        selected_user_password = self.model_right.item(row_to_delete, 4).text()

        self.db.add_user_r(selected_user_id, selected_username, selected_user_last_name, selected_user_role, selected_user_password)
        self.db.delete_user(selected_user_id, selected_username, selected_user_last_name, selected_user_role, selected_user_password)


    def send_to_right_Button(self):
        selected_index = self.leftTable.selectedIndexes()
        if not selected_index:
            QMessageBox.warning(self, 'Предупреждение', 'Пожалуйста, выберите строку для удаления.')
            return

        row_to_delete = selected_index[0].row()
        selected_user_id = self.model_left.item(row_to_delete, 0).text()
        selected_username = self.model_left.item(row_to_delete, 1).text()
        selected_user_last_name = self.model_left.item(row_to_delete, 2).text()
        selected_user_role = self.model_left.item(row_to_delete, 3).text()
        selected_user_password = self.model_left.item(row_to_delete, 4).text()

        self.db.send_to_left_table(selected_user_id, selected_username, selected_user_last_name, selected_user_role, selected_user_password)
        self.db.delete_user_right(selected_user_id, selected_username, selected_user_last_name, selected_user_role, selected_user_password)

    def load_data(self):
        self.model_left.clear()
        data = self.db.get_info()

        for row in data:
            print(row)
            items = [QStandardItem(str(field)) for field in row]
            self.model_left.appendRow(items)


    def load_right_data(self):
        self.model_right.clear()
        data = self.db.get_info_r()

        for row in data:
            print(row)
            items = [QStandardItem(str(field)) for field in row]
            self.model_right.appendRow(items)
    
    def close_data(self):
        close = self.db.close_db(self.database)

        if not close:
            print("База данных активна")
        else:
            pyodbc.pooling = False
            print("База данных выключена")

    def add_data_button(self):
        self.add = AddDataWindow(self.db)
        self.add.setFixedSize(406, 400)
        self.add.data_added.connect(self.load_data)
        self.add.show()


    def delete(self):
        selected_index = self.leftTable.selectedIndexes()
        if not selected_index:
            QMessageBox.warning(self, 'Предупреждение', 'Пожалуйста, выберите строку для удаления.')
            return

        row_to_delete = selected_index[0].row()
        selected_user_id = self.model_left.item(row_to_delete, 0).text()
        selected_username = self.model_left.item(row_to_delete, 1).text()
        selected_user_last_name = self.model_left.item(row_to_delete, 2).text()
        selected_user_role = self.model_left.item(row_to_delete, 3).text()
        selected_user_password = self.model_left.item(row_to_delete, 4).text()


        try:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Подтверждение")
            msg_box.setText("Вы уверены, что хотите продолжить?")
            msg_box.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            result = msg_box.exec_()
            if result == QMessageBox.Ok:
                self.db.delete_user(selected_user_id, selected_username, selected_user_last_name, selected_user_role, selected_user_password)
                print(selected_user_id, selected_username, selected_user_last_name, selected_user_role, selected_user_password)
                QMessageBox.information(self, 'Успех', 'Данные удалены успешно.')
                self.model_left.removeRow(row_to_delete)
            else:
                QMessageBox.information(self, 'Успех', 'Действие отменено')
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', str(e))
            print(e)



    def edit_data_button(self):
        selected_index = self.tableView.selectedIndexes()
        if not selected_index:
            QMessageBox.warning(self, 'Предупреждение', 'Пожалуйста, выберите строку для удаления.')
            return

        row_to_delete = selected_index[0].row()
        val_user_id = self.model.item(row_to_delete, 0).text()
        val_username = self.model.item(row_to_delete, 1).text()
        val_user_last_name = self.model.item(row_to_delete, 2).text()
        val_user_role = self.model.item(row_to_delete, 3).text()
        val_user_password = self.model.item(row_to_delete, 4).text()       
        self.edit = EditDataWindow(self.db, val_user_id, val_username, val_user_last_name, val_user_role, val_user_password)
        self.edit.setFixedSize(406, 319)
        self.edit.data_edit.connect(self.load_data)
        self.edit.show()

class AddDataWindow(QMainWindow):
    data_added = pyqtSignal()
    def __init__(self, db):
       super().__init__()
       uic.loadUi(r"design\add_data_form.ui", self)
       self.setWindowTitle("Add data")
       self.model = QStandardItemModel(self)
       self.pushButton.clicked.connect(self.append_data)
       self.right_table.clicked.connect(self.append_data_r)
       self.db = db
       self.main_window = MainWindow()

    def append_data(self):
        username = self.lineEdit.text()
        last_name = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        self.db.add_user(username, last_name, password)
        self.data_added.emit()
        # Уведомление и завершение работы окна Add_data_window
        QMessageBox.information(self, "Успех", "Данные успешно добавлены")
        AddDataWindow.close(self)

    def append_data_r(self):
        username = self.lineEdit.text()
        last_name = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        self.db.add_user_r(username, last_name, password)
        self.data_added.emit()
        # Уведомление и завершение работы окна Add_data_window
        QMessageBox.information(self, "Успех", "Данные успешно добавлены")
        AddDataWindow.close(self)


class EditDataWindow(QMainWindow):
    data_edit = pyqtSignal()
    def __init__(self, db, val_user_id, val_username, val_last_name, val_user_role, val_user_password):
       super().__init__()
       uic.loadUi(r"design\edit_data_form.ui", self)
       self.setWindowTitle("Edit data")
       self.model = QStandardItemModel(self)
       self.pushButton.clicked.connect(self.edit_data)
       self.db = db
       self.name_input.setText(val_username)
       self.last_name_input.setText(val_last_name)
       self.password_input.setText(val_user_password)
       self.user_id = val_user_id
       self.role = val_user_role
       print(f"\nИмя пользователя: {val_username},\n ID: {val_user_password}\n")
    def edit_data(self):              
        try:
            new_name = self.name_input.text()
            new_last_name = self.last_name_input.text()
            new_password = self.password_input.text()
            print(f"\nusername: {new_name},\n last name: {new_last_name}\npassword: {new_password}")
            # добавление данных в БД
            self.db.update_user(self.user_id ,new_name, new_last_name, new_password)
            self.data_edit.emit()
            QMessageBox.information(self, "Успех", "Данные обновлены")
            EditDataWindow.close(self)
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", "Не удалось выполнить запрос(")
            print(f"Запрос не удалось реализовать(. Ошибка: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(1032, 685)
    window.show()
    sys.exit(app.exec())