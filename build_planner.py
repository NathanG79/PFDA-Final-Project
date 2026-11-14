import pygame



class Upgrade():

    def __init__(self, name="special\\The_Void", size_mult=1/3,
                 center_pos=(0,0)):
        self.name = name
        self.size = (270 * size_mult, 315 * size_mult)
        self.pos = (center_pos[0] - self.size[0],
                    center_pos[1] - self.size[1])
        self.image = self._init_image()

    def _init_image(self):
        image = pygame.image.load(f"icons\\{self.name}.webp")
        image = pygame.transform.scale(image, self.size)
        return image

    def draw(self, surface):
        surface.blit(self.image, self.pos)



def main():
    pygame.init()
    pygame.display.set_caption("Nova Drift Build Planner")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()
    dt = 0
    bg_color = pygame.Color(50, 50, 50)

    running = True
    volley = Upgrade("Volley", 1/3, (200, 200))
    mines = Upgrade("Mines", 1/3, (300, 150))
    scrolling = 0
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scrolling = 1
                elif event.button == 5:
                    scrolling = -1

        # Game logic
        
        # Render & Display
        screen.fill(bg_color)
        volley.draw(screen)
        mines.draw(screen)
        print(scrolling)
        pygame.display.flip()
        dt = clock.tick(12)
        scrolling = 0

    pygame.quit()


if __name__ == "__main__":
    main()