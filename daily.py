import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pet Collector")

# Background
bg = pygame.image.load("pet_bg.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# Font
font = pygame.font.SysFont("Arial", 40)

# Player
player = pygame.Rect(400, 300, 50, 50)

# Pets
pets = []

for i in range(5):
    pet = pygame.Rect(
        random.randint(0, WIDTH - 40),
        random.randint(0, HEIGHT - 40),
        40,
        40
    )
    pets.append(pet)

running = True

while running:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # Keep player inside screen
    player.x = max(0, min(player.x, WIDTH - player.width))
    player.y = max(0, min(player.y, HEIGHT - player.height))

    pygame.draw.rect(screen, (0, 0, 255), player)

    for pet in pets[:]:
        pygame.draw.rect(screen, (255, 0, 0), pet)

        if player.colliderect(pet):
            pets.remove(pet)

    # Display win message
    if len(pets) == 0:
        text = font.render("You Win!", True, (255, 255, 255))

        x = (WIDTH - text.get_width()) // 2
        y = (HEIGHT - text.get_height()) // 2

        screen.blit(text, (x, y))

    pygame.display.update()

pygame.quit()