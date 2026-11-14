import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Nova Drift Build Planner")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()
    dt = 0
    black = pygame.Color(0, 0, 0)

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic
        
        # Render & Display
        screen.fill(black)
        image = pygame.image.load("icons\\Volley.webp")
        image = pygame.transform.scale(image, (90, 105))
        screen.blit(image, (100, 100))
        pygame.display.flip()
        dt = clock.tick(12)

    pygame.quit()


if __name__ == "__main__":
    main()