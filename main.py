from datetime import datetime
import math
import pygame
import config
import colors

pygame.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption('pyClock')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Lucida Console', 60)

angle_hours = 0

hour_hand = dict(zip(range(12), range(0, 360, 30)))
min_hand = dict(zip(range(60), range(0, 360, 6)))


def getClockPosition(clockDict: dict, clockHand: int) -> tuple[float, float]:
    x = config.WIDTH + config.clock_radius * math.cos(math.radians(clockDict[clockHand]) - math.pi / 2)
    y = config.HEIGHT + config.clock_radius * math.sin(math.radians(clockDict[clockHand]) - math.pi / 2)
    return x, y


def drawAnalogClock():
    pygame.draw.circle(screen, colors.WHITE, (config.WIDTH // 2, config.HEIGHT // 2), config.clock_radius,
                       config.clock_width)
    pygame.draw.line(screen, colors.WHITE, [config.WIDTH // 2, config.HEIGHT // 2],
                     getClockPosition(min_hand, secs), 1)
    pygame.draw.line(screen, colors.WHITE, [config.WIDTH // 2, config.HEIGHT // 2],
                     getClockPosition(min_hand, mins), 3)
    pygame.draw.line(screen, colors.WHITE, [config.WIDTH // 2, config.HEIGHT // 2],
                     getClockPosition(hour_hand, hours % 12), 5)
    pygame.display.update()


def drawDigitalClock():
    str_hours = '0' + str(hours) if hours < 10 else str(hours)
    str_mins = '0' + str(mins) if mins < 10 else str(mins)
    str_secs = '0' + str(secs) if secs < 10 else str(secs)
    clock_text = '{}:{}:{}'.format(str_hours, str_mins, str_secs)
    digital_clock = font.render(clock_text, True, colors.WHITE)
    digital_clock_rect = digital_clock.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2))
    screen.blit(digital_clock, digital_clock_rect)
    pygame.display.update()


isDigital = True
running = True
while running:

    current_time = datetime.now()
    hours, mins, secs = current_time.hour, current_time.minute, current_time.second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if isDigital:
                    isDigital = False
                else:
                    isDigital = True

    screen.fill(colors.BLACK)
    if isDigital:
        drawDigitalClock()
    else:
        drawAnalogClock()
    pygame.display.flip()
    clock.tick(config.FPS)

