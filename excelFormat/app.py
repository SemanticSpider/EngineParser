from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.button import Button
from kivymd.uix.button import MDButton
from plyer import filechooser
import os

class LoadCard(MDCard):

    loadFile = StringProperty()
    label = StringProperty()
    cardColor = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.5
        Window.bind(on_drop_file=self.selectFile)
        
    # Метод, вызываемый при нажатии на кнопку загрузки файла
    def changeFile(self):        
        # Выбор фалйа в filechooser
        choose = filechooser.open_file(on_selection=self.selectFile)

    # Обработчик события выбора файла в filechooser, записывает путь к выбранному файлу в поле loadFile
    def selectFile(self, *args):
        # Получаем путь к файлу
        if(type(args[0]) == list):
            # Из filechooser
            self.loadFile = args[0][0] if len(args[0]) != 0 else self.loadFile
        else:
            # Из Drag-n-Drop
            self.loadFile = args[1].decode(encoding="utf-8")
        
        # Осуществляем проверку Excel расширения
        if self.loadFile and self.loadFile.endswith((".xls", ".xlt", ".xlsx", ".xlsm", ".xltx", ".xltm")):
            self.cardColor = [0.0, 0.5019607843137255, 0.0, 0.3]
            self.label = "Файл {} загружен!".format(self.loadFile.split('\\').pop())
        elif self.loadFile == "":
            pass        
        else: 
            self.cardColor = [1.0, 0.0, 0.0, 0.5]
            self.label = "Принимаются только файлы excel!"
            self.loadFile = ""
        print(self.loadFile)

    # Ограничиваем дефолтное поведение карточки, чтобы убрать автоматическое изменение цвета
    def set_properties_widget(self):
        super().set_properties_widget()
        self.md_bg_color = self.cardColor
        return True
    
class LoadDirectory(MDBoxLayout):

    labelText = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with open(os.path.dirname(os.path.realpath(__file__)) + "\\loadDirectory.txt", "a+") as loadDir:
            loadDir.seek(0, 0)
            self.labelText = loadDir.read()
    
    def chooseDirectory(self):

        def selectDirectory(selectedDirectory):
            self.labelText = selectedDirectory = selectedDirectory[0] if(len(selectedDirectory)) != 0 else self.labelText
            with open(os.path.dirname(os.path.realpath(__file__)) + "\\loadDirectory.txt", "w") as loadDir:
                loadDir.write(self.labelText)

        directory = filechooser.choose_dir(on_selection=selectDirectory)

class LaunchButton(MDButton):
    def launchParse(self):
        print(self)

# Класс окна
class Root(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class EngineParser(MDApp):

    # Дефолтные настройки приложения
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.maximize()
 
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.screen = Root()

        loadCard = LoadCard(loadFile = "", label="Загрузите файл", cardColor=self.theme_cls.backgroundColor)        
        loadDirectory = LoadDirectory()
        launchButton = LaunchButton()

        self.screen.add_widget(loadCard)
        self.screen.add_widget(loadDirectory)
        self.screen.add_widget(launchButton)
        # print([widget for widget in self.screen.children if widget.name == "LoadCard"][0].buttonText)
        return self.screen

if __name__ == "__main__":
   app = EngineParser()
   app.run()