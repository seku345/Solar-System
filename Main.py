# Библиотеки
from pygame import *
from math import *
from win32api import GetSystemMetrics

# Класс планет
class Planet(sprite.Sprite):

    ...

# Главная функция
def main():
    
    # Настройка экрана
    H = GetSystemMetrics(0)
    V = GetSystemMetrics(1)

    window = display.set_mode((0, 0), FULLSCREEN)
    display.set_caption('Planet Simulation')
    background = transform.scale(image.load('Sprites/Background.jpg'), (H, V))

    clock = time.Clock()

    # Основной цикл
    run = True
    while run:

        # Кадры в секунду
        clock.tick(60)
        display.update()

        # Фон
        window.blit(background, (0, 0))

        # Обработка событий
        for e in event.get():

            # Закрытие окна
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                run = False

# Запуск
if __name__ == '__main__':
    main()