import pyttsx3
engine = pyttsx3.init()
# Settings
rate = engine.getProperty('rate')                
engine.setProperty('rate', 109) 

# Start
engine.say("Bienvenido al bot de voz creado por Andres")
engine.runAndWait()

engine.say("Escribe lo que quieres poner pendejo")
engine.runAndWait()
text = input()

engine.say(text)
engine.runAndWait()

question = input("¿Quieres guardar la voz en un archivo mp3? ")
if question.lower() == "si":
    print("Grabaccion gaurdada!")
    engine.save_to_file(text, "grabaccion.mp3")
    engine.runAndWait()
else:
    print("no se a guardado")




engine.stop()