''' Вікно для питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QTableWidget, QListWidget, QListWidgetItem,
       QLineEdit, QFormLayout,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QButtonGroup, QRadioButton, 
       QPushButton, QLabel, QSpinBox)
 
app = QApplication([])
 
# віджети, які потрібно розмістити
btn_Menu = QPushButton('Меню') # кнопка повернення в меню
btn_Sleep = QPushButton('Відпочити') # кнопка забирає вікно, і повертає його після закінчення таймера
box_Minutes = QSpinBox() # кількість хвилин
box_Minutes.setValue(30)
btn_OK = QPushButton('Відповісти') # кнопка відповіді
lb_Question = QLabel('') # текст питання
 
# Панель з варіантами:
RadioGroupBox = QGroupBox("Варіанти відповідей") # група на екрані для перемикачів з відповідями
RadioGroup = QButtonGroup() # групування перемикачів, щоб управляти їх перемиканням і видимістю
 
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')
 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
# Панель з результатами:
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('') #правильно чи не правильно
lb_Correct = QLabel('') # текст правильної відповіді
 
#  Розміщення:
 
# Варіанти відповідей в два стовпця вередині групи:
layout_ans1 = QHBoxLayout()  
layout_ans2 = QVBoxLayout() # вертикальні будуть всередині горизонтальних
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) # дві відповіді в одному стовпці
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # дві в іншому
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # стовпці в одній строці
 
RadioGroupBox.setLayout(layout_ans1) # готова панель з вар відповідей  

# розміщення результатів
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
 
# разміщуємо усі віджети у вікні, вони розташовані в чотири рядки(4 горизонтальні лінії):
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()
 
layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1) # разрив між кнопками робимо по можливості довшим
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилин')) 
 
layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)#додаємо до 3 горизонтальної лінії вікно, 
#яке містить напис Варіанти відповідей і всі наві відповіді, тобто нашу рамку
layout_line3.addWidget(AnsGroupBox)#як і в попередньому, 
#тільки додаємо уже результат
 
layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2) # додавання кнопки до лінії і збільшення
layout_line4.addStretch(1)
 
# Тепер створюємо 4 рядки, розмістивши одна під одною:
#тобто створюємо 1 вертикальну лінію, в яку добавляємо наші 4 горизонтальні
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробіли 
 
# Результат работи цього модуля: віджети поміщенні всередині layout_card.
 
def show_result():
   ''' показать панель ответов '''
   RadioGroupBox.hide()
   AnsGroupBox.show()
   btn_OK.setText('Наступне питання')
 
def show_question():
   ''' показати панель запитань '''
   RadioGroupBox.show()
   AnsGroupBox.hide()
   btn_OK.setText('Відповісти')
   # скинути вибрану кнопку
   RadioGroup.setExclusive(False) # зняти обмеження, щоб можна було вкинути вибір радіо кнопки
   rbtn_1.setChecked(False)
   rbtn_2.setChecked(False)
   rbtn_3.setChecked(False)
   rbtn_4.setChecked(False)
   RadioGroup.setExclusive(True) # повернути обмеження, тепер тільки одна радіокнопка може бути вибрана
