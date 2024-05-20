from captcha.image import ImageCaptcha
import random

letras = 'abcdefghijklmnopqrstuvwxyz'
maisculas = letras.upper()
numeros = '0123456789'
todos = letras + maisculas + numeros
tamanho = 5

image = ImageCaptcha(width = 280, height = 90)
captcha_texto =  "".join(random.sample(todos, tamanho))
data = image.generate(captcha_texto)
image.write(captcha_texto, 'Captcha.png')

input('Captcha criado com sucesso!\nAperte ENTER para sair...')