import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle, Color, Ellipse
from plyer import filechooser


# red = [1,1,0,1,]
# green = [0,1,0,1]
# blue =  [0,0,1,1]
# purple = [1,0,1,1]


# class ButtonApp(App):
#     def build(self):
#         layout = BoxLayout(padding=10, spacing=10, orientation='vertical')
#         colors = [red, green, blue, purple]
#         for i in range(len(colors)):
#             color = random.choice(colors)
#             btn = Button(text=f"Button #{i}",
#                          background_color=color
#                          )
#             colors.remove(color)
#             btn.bind(on_press=self.on_press_button)
#             layout.add_widget(btn)
#         return layout
#     def on_press_button(self, instance):
#         print(f"Вы нажали на кнопку {instance}")

# class MainApp(App):
#     def build(self):
#         self.operators = ["/", "*", "+", "-"]
#         self.last_was_operator = None
#         self.last_button = None
#         main_layout = BoxLayout(orientation="vertical")
#         self.solution = TextInput(
#             multiline=False, readonly=True, halign="right", font_size=55
#         )
#         main_layout.add_widget(self.solution)
#         buttons = [
#             ["7", "8", "9", "/"],
#             ["4", "5", "6", "*"],
#             ["1", "2", "3", "-"],
#             [".", "0", "C", "+"]
#         ]
#         for row in buttons:
#             h_layout = BoxLayout()
#             for label in row:
#                 button = Button(
#                     text=label,
#                     pos_hint={"center_x": 0.5, "center_y": 0.5}
#                 )
#                 button.bind(on_press=self.on_button_press)
#                 h_layout.add_widget(button)
#             main_layout.add_widget(h_layout)
#         equals_button = Button(
#             text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
#         )
#         equals_button.bind(on_press=self.on_solution)
#         main_layout.add_widget(equals_button)

#         return main_layout
    
#     def on_button_press(self, instance):
#         current = self.solution.text
#         button_text = instance.text

#         if button_text == "C":
#             self.solution.text = ""
#         else:
#             if current and (self.last_was_operator and button_text in self.operators):
#                 return
#             elif current == "" and button_text in self.operators:
#                 return
#             else:
#                 new_text = current + button_text
#                 self.solution.text = new_text
#         self.last_button = button_text
#         self.last_was_operator = self.last_button in self.operators

#     def on_solution(self, instance):
#         text = self.solution.text
#         if text:
#             solution = str(eval(self.solution.text))
#             self.solution.text = solution

# class Filechooser(App):
#     def build(self):
#         Window.bind(on_drop_file=self.onFileDrop)
    
#     def onFileDrop(self, window, file_path, *args):
#         print(file_path)
# class Filechooser(BoxLayout):
#    def select(self, *args):
#       try:
#          self.img.source = args[1][0]
#       except:
#          print ('error')
         
# class FileIconApp(App):
#    def build(self):
#       return Filechooser()

# # run the App
# if __name__ == '__main__':
#    FileIconApp().run()

class Root(BoxLayout):

   def __init__(self, **kwargs):
      super().__init__()

   def file_chooser(self, *args):
      filechooser.open_file(on_selection=self.selected)

   def selected(self, selection):
      print(selection)

   def onFileDrop(self, window, file_path, *args):
      print(file_path)

class EngineParser(App):
   pass

if __name__ == "__main__":
   app = EngineParser()
   app.run()
