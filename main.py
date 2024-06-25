import pygame 

pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((400, 500))
 
pygame.display.set_caption('Voce foi Hackeado')
 
running = True

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    blit_text(screen, "Voce foi Hackeada!\nMas nao se preocupe!\nEsse programa nao faz nada!", (50, 100), my_font, (255, 0, 255))

    pygame.display.flip()