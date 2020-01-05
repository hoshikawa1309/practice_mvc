from views import console

class Command(object):

    def __init__(self , speak_color = 'green'):
        self.speaker_color = speak_color

    def show(self):
        #template = console.get_template('me.txt' , self.speaker_color)
        template = console.get_template('venv/template/me.txt')
        print(template)