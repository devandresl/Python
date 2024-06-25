from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# an = driver.get(input("Porfavor escribe la url del sitio a analizar, recuerda poner https://: "))
driver.get("https://devandresl.github.io/Portafolio/")

# title
titulo = driver.title
print(f'El titulo del encabezado de la pagina es: {titulo}')

driver.implicitly_wait(1)
# h1 , h2 y h3
h1 = driver.find_elements(By.TAG_NAME,"h1"); h2 = driver.find_elements(By.TAG_NAME,"h2");h3 = driver.find_elements(By.TAG_NAME,"h3")
if not h1:
    print("NO EXISTE UN H1")
else:
    for cadaH1 in h1:
        print("¡Se a encontrado un h1!: " + cadaH1.text)

if not h2:
    print("NO SE ENCONTRARON H2")
else:
    for cadaH2 in h2:
        print("¡Se a encontrado un H2!: " + cadaH2.text)

if not h3:
    print("NO SE ENCONTRARON H3")
else:
    for cadaH3 in h3:
        print("¡Se a encontrado un H3!: " + cadaH3.text)

driver.implicitly_wait(1)
# h4 y h5
pregunta = input("¿Quiera saber si hay algun h4 o h5? ")
if pregunta.lower() == "si":
    h4 = driver.find_elements(By.TAG_NAME,"h4");h5 = driver.find_elements(By.TAG_NAME,"h5")
    if not h4:
        print("No e encontrado ningun H4")
    else:
        for cadaH4 in h4:
         print("¡Se a encontrado un H4!: " + cadaH4.text)

    if not h5:
         print("No e encontrado ningun H5")
    else:
        for cadaH5 in h5:
         print("¡Se a encontrado un H5!: " + cadaH5.text)

driver.implicitly_wait(1)
    
driver.quit()