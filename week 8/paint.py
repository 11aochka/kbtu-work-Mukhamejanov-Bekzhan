import pygame

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((640, 480))
    canvas = pygame.Surface(screen.get_size())
    canvas.fill((0, 0, 0)) 
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'             
    tool = 'brush'            
    drawing = False           
    points = []                
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_w and ctrl_held) or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and alt_held) or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_l:
                    tool = 'rectangle'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_p:
                    tool = 'brush'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    if tool == 'brush':
                        points.append(event.pos)
                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    if tool == 'circle':
                        pygame.draw.circle(canvas, getColor(mode), event.pos, radius)
                    elif tool == 'rectangle':
                        rect = pygame.Rect(start_pos, (event.pos[0] - start_pos[0], event.pos[1] - start_pos[1]))
                        pygame.draw.rect(canvas, getColor(mode), rect)

            if event.type == pygame.MOUSEMOTION and drawing:
                position = event.pos
                if tool == 'brush':
                    points.append(position)
                    if len(points) >= 2:
                        drawLineBetween(canvas, len(points)-2, points[-2], points[-1], radius, mode)
                elif tool == 'eraser':
                    pygame.draw.circle(canvas, (0, 0, 0), position, radius)

        screen.blit(canvas, (0, 0))
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(surface, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(surface, color, (x, y), width)

def getColor(mode):
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    return (255, 255, 255)

main()
