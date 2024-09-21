from flask import Flask
from flask import render_template
from flask import request

from vosk import Model, KaldiRecognizer
import json
import pyaudio

app = Flask(__name__)


model = Model('vosk-model-small-ru-0.4')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

title = 'Neo'

commands_dict = {
    'commands':{
        'greeting':{'привет', 'привет мейсон', 'дарова', 'здравствуйте', 'здорово', 'мейсон', 'приветствую'},
        'create_task':{'добавить задачу', 'мейсон добавь задачу', 'задача', 'добавь задачу', 'мейсон задача', 'запиши задачу'},
        'exit':{'выход', 'выхад', 'мейсон пока', 'закончить работу', 'завершить работу', 'завершение', 'выйти', 'завершение работы'},
        'neyro':{'запусти протокол', 'протокол', 'мейсон запусти протокол'},
        'wiki':{'режим вики', 'википедия', 'открой википедию', 'режим википедии', 'открой вики'},
        'web':{'открой браузер', 'открой интернет'},
        'dollar':{'курс доллара', 'курс валют', 'валюты'},
        'heart': {'открой основу', 'основа', 'сердце'}
    }
}

def main():
    #eel.start("index.html", host='localhost', port=8000, block=True, size=(350, 350))

    print("M.A.Y.S.O.N. v1.2.1 - Готов к работе!")
    print("***************************************")
    print("M.A.Y.S.O.N.: " + "USER" + " скажите что-нибудь...")
    #web()

    while True:
        
        
        query = listen_command()
        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]()) 
    else:
        main()
        
                            
    #print("Bye")

def listen_command():   
    try:
        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if (rec.AcceptWaveform(data)) and (len(data) > 0):
                answer = json.loads(rec.Result())
                if answer['text']:
                    return answer['text']
        #with sr.Microphone() as mic:
            #recognizer.adjust_for_ambient_noise(source=mic, duration=0.1)
            #audio = recognizer.listen(source=mic)
            #query = recognizer.recognize_google(audio_data=audio, language="ru-RU").lower()
            #return query
        #stop_listening = recognizer.listen_in_background(mic)         
    except:
        print("Жду приказов!")


def greeting():
    USER = 'Макс'
    print("Hello, " + USER)


@app.route('/heart')
def heart():
  #return 'Hello, World!
    #title = request.form['name']
    #main()
    return render_template('heart.html')

def exit():
    print("Завершение работы")  
    quit()
    #return render_template('heart.html')

@app.route('/submit')
def submit():
  #return 'Hello, World!
    #title = request.form['name']
    #main()
    return render_template('heart.html')
    #return f'Hellow {title}'

@app.route('/')
def hello():
  #return 'Hello, World!
    #title = request.form['name']
    #main()
    return render_template('index.html')


if __name__ == '__main__':
  app.run()

  