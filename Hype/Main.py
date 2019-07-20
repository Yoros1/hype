'''docstring'''
import sys
import psycopg2
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWizard, QWizardPage, QFileDialog, QWidget, QVBoxLayout, QDesktopWidget, QCalendarWidget, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QValidator, QIntValidator, QDoubleValidator, QPixmap
from pyqtlet import L, MapWidget
from ui_main_window import *
from ui_login_form import *
from ui_signup_wizard import *
from ui_signup_confirmation import *

class Main(QMainWindow):
    ''' class Main docstring '''
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # /* set window location in center of each monitor
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # set window location in center of each monitor /*
        self.statusBar().showMessage('Ready for fly ... ')

        self.ui.btn_setting.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.btn_wallet.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btn_3.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.btn_4.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.btn_5.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.btn_6.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.btn_7.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(6))
        self.ui.btn_8.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(7))
        self.ui.btn_9.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(8))
        
    def setting(self):
        ''' setting method docstring '''

class Validator(QDoubleValidator):
    '''class docstring'''
    def validate(cls, self, str, int):
        super().validate(self, str, int)
        self.onlyint = QIntValidator()

class Login(QDialog):
    '''class Login docstring'''
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_login_form() # making ui object
        self.ui.setupUi(self) # filling ui
        self.ui.btn_enter_acnt.clicked.connect(self.handleLogin)
        self.ui.btn_request_temp_pass.clicked.connect(self.request_temp_pass)
        self.ui.btn_sign_up.clicked.connect(self.signup)
        self.ui.btn_cancel_login.clicked.connect(lambda x: self.close())

    def handleLogin(self):
            if (self.ui.lineEdit_username.text() == 'foo' and
                self.ui.lineEdit_password.text() == 'bar'):
                self.accept()
            else:
                QtWidgets.QMessageBox.warning(
                    self, 'Error', 'نام کاربری یا رمز عبور اشتباه است!')

    def request_temp_pass(self):
        ''' request for temporary password '''
        self.ui.label_msg_temp_pass.setText('درخواست رمز یکبار مصرف ارسال شد')

    def signup(self):
        ''' signup method docstring'''
        signup_obj = Signup()
        signup_obj.show()
        if signup_obj.exec_():
            signup_obj.show()

class MapWindow(QDialog):
    
    def __init__(self, parent=None):
        # Setting up the widgets and layout
        super().__init__(parent=parent)
        self.mapWidget = MapWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mapWidget)
        self.setLayout(self.layout)
        self.setModal(True)

        # Working with the maps with pyqtlet
        self.map = L.map(self.mapWidget)
        self.map.setView([35.76898, 51.45872], 18)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)
        self.marker = L.circleMarker([35.76898, 51.45872])
        self.marker.bindPopup('Maps are a treasure.')
        self.map.addLayer(self.marker)

class DatePicker(QCalendarWidget):
    ''' dat picker widget '''
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.calendar_widget = QCalendarWidget()
        self.setWindowModality(True)
        self.show()

class Signup(QWizard):
    ''' this class is used for generate ui object for signup wizard and show the ui object '''
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_signup_wizard()
        self.ui.setupUi(self)
        self.ui.toolButton_upload_img.clicked.connect(self.upload_profile_image)
        self.ui.toolButton_upload_card.clicked.connect(self.upload_nationalcard)
        self.ui.toolButton_pin_location.clicked.connect(self.pin_my_location)
        self.ui.toolButton_calendar.clicked.connect(self.date_picker)
        self.button(QWizard.NextButton).clicked.connect(self.validateCurrentPage)
        
        self.wizard_finish_button = self.button(QtWidgets.QWizard.FinishButton)
        self.wizard_finish_button.disconnect()
        self.wizard_finish_button.clicked.connect(self.signup_finish)
        self.card_path = ''
        
        int_rgx = QRegExp("[0-9]+.?[0-9]{,2}")
        name_rgx = QRegExp('')
        email_rgx = QRegExp('')

        int_validator = QRegExpValidator(int_rgx, self.ui.lineEdit_mobile)
        self.ui.lineEdit_mobile.setValidator(int_validator)
        self.ui.lineEdit_nationalCode.setValidator(int_validator)
        
        ###### set validator for values of signup pages here      

    def upload_profile_image(self):
        ''' this method is used for image uploading'''
        file_name = QFileDialog.getOpenFileName(self, 'select image', 'C\\', 'image files (*.jpg *.png *.jpeg)')
        self.profile_img_path = file_name[0]
        pixmap = QPixmap(self.profile_img_path)
        self.ui.label_img.setPixmap(QPixmap(pixmap))
        self.ui.label_img.setScaledContents(True)
        
    def upload_nationalcard(self):
        ''' this method is used for image uploading'''
        file_name = QFileDialog.getOpenFileName(self, 'select image', 'C\\', 'image files (*.jpg *.png *.jpeg)')
        self.card_path = file_name[0]
        pixmap = QPixmap(self.card_path)
        self.ui.label_nationalCard.setPixmap(QPixmap(pixmap))
        self.ui.label_nationalCard.setScaledContents(True)
    
    def date_picker(self):
        ''' pick date from calendar widget '''
        self.calendar_obj = DatePicker()
        self.birth_date = self.calendar_obj.selectedDate()
        birth_day = self.birth_date.day()
        birth_month = self.birth_date.month()
        birth_year = self.birth_date.year()
        self.ui.lineEdit_birth_day.setText(str(birth_day))
        self.ui.lineEdit_birth_month.setText(str(birth_month))
        self.ui.lineEdit_birth_year.setText(str(birth_year))

    def validateCurrentPage(self):
        ''' docstring '''
        if self.ui.lineEdit_mobile.text() == '':
            self.ui.lbl_warning_msg.setText('وارد کردن "تلفن همراه" الزامی است ')
            return False

        # if len(self.ui.lineEdit_mobile.text()) < 11:
        #     self.ui.lbl_warning_msg.setText('تلفن همراه را درست وارد نمایید')
        #     return False

        # elif self.ui.lineEdit_firstName.text() == '':
        #     self.ui.lbl_warning_msg.setText('وارد کردن "نام" الزامی است ')
        #     return False

        # elif self.ui.lineEdit_lastName.text() == '':
        #     self.ui.lbl_warning_msg.setText('وارد کردن  "نام خانوادگی" الزامی است ')
        #     return False

        # elif self.ui.lineEdit_nationalCode.text() == '':
        #     self.ui.lbl_warning_msg.setText('وارد کردن کد ملی الزامی است')
        #     return False

        # elif self.card_path == '':
        #     self.ui.lbl_warning_msg.setText('بارگذاری تصویر کارت ملی الزامی است ')
        #     return False

        else:
            self.first_name = self.ui.lineEdit_firstName.text()
            self.last_name = self.ui.lineEdit_lastName.text()
            self.mobile = self.ui.lineEdit_mobile.text()
            self.national_code = self.ui.lineEdit_nationalCode.text()
            self.Email = self.ui.lineEdit_Email.text()
            return True

    def upload_permission(self):
        ''' this method is used for image uploading'''
        file_name = QFileDialog.getOpenFileName(self, 'select image', 'C\\', 'image files (*.jpg *.png *.jpeg)')
        self.permission_img_path = file_name[0]
        pixmap = QPixmap(self.permission_img_path)
        self.ui.label_permission.setPixmap(QPixmap(pixmap))
        self.ui.label_permission.setScaledContents(True)

    def pin_my_location(self):
        map_widget = MapWindow(self)
        map_widget.show()

    @QtCore.pyqtSlot()
    def signup_finish(self):
        '''method doc'''   
                
        if self.ui.lineEdit_company_name.text() == '':
            self.ui.lbl_warning_msg_2.setText('وارد کردن نام شرکت الزامی است ')
            return False

        # elif self.ui.comboBox_guild.currentText() == '':
        #     self.ui.lbl_warning_msg_2.setText('صنف مربوط به فروشگاه/شرکت/موسسه خود را انتخاب کنید')
        #     return False

        # elif self.ui.lineEdit_address.text() == '':
        #     self.ui.lbl_warning_msg_2.setText('وارد کردن نشانی دقیق الزامی است')
        #     return False

        # elif self.ui.lineEdit_phone.text() == '':
        #     self.ui.lbl_warning_msg_2.setText('وارد کردن تلفن ثابت اجباری است در صورت عدم وجود تلفن ثابت، شماره جایگزین وارد کنید')
        #     return False

        # elif self.permission_img_path.text() == '':
        #     self.ui.lbl_warning_msg_2.setText('بارگذاری مجوز فعالیت الزامی است')
        #     return False

            # ('انتخاب موقعیت کسب و کار روی نقشه الزامی است')

        else:
            signup_conf_obj = signup_conf()
            signup_conf_obj.exec_()
            self.accept()

class signup_conf(QDialog):
    '''docstring'''
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Signup_confirmation()
        self.ui.setupUi(self)
        self.ui.lineEdit_firstName.setText(Signup.first_name)
        self.ui.btn_confirm.clicked.connect(self)
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_obj = Login()

    if login_obj.exec_() == QDialog.Accepted:
        main = Main()
        main.show()
        sys.exit(app.exec_())
    sys.exit(app.exec_())
