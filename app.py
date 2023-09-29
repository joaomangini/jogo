from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
import subprocess

class SnakeGameWidget(Widget):
    def __init__(self, **kwargs):
        super(SnakeGameWidget, self).__init__(**kwargs)
        self.game_running = False

    def start_game(self):
        if not self.game_running:
            subprocess.Popen(['python', 'cobrinha.py'])
            self.game_running = True

class SnakeApp(App):
    def build(self):
        game_widget = SnakeGameWidget()
        Clock.schedule_once(lambda dt: game_widget.start_game(), 0)
        return game_widget

if __name__ == "__main__":
    SnakeApp().run()
