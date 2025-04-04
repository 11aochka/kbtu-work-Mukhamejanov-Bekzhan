import pygame
import math

def main():
    """
    Main function to initialize Pygame and run the drawing application.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Increased screen size for better usability
    pygame.display.set_caption("Drawing Application") # Set Window Title
    clock = pygame.time.Clock()

    # Initialize drawing surface (canvas)
    canvas = pygame.Surface(screen.get_size())
    canvas.fill((0, 0, 0))  # Black background

    # Initial values for drawing
    radius = 5  # Reduced default radius
    mode = 'blue'
    tool = 'pen'
    points = []
    start_pos = None
    drawing = False

    # --- Helper Functions ---

    def get_color(color_mode):
        """
        Returns the RGB color tuple based on the given color mode.
        Defaults to white if the mode is invalid.
        """
        colors = {
            'blue': (0, 0, 255),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'black': (0, 0, 0),
            'white': (255, 255, 255) #Added White
        }
        return colors.get(color_mode, (255, 255, 255))

    def draw_line_between(surface, index, start, end, width, color_mode):
        """
        Draws a line between two points with a given width and color.
        The color can vary slightly based on the index for a dynamic effect.
        """
        color = get_color(color_mode)
        pygame.draw.line(surface, color, start, end, width * 2) # Increased line thickness

    def draw_right_triangle(surface, start, end, color):
        """
        Draws a right triangle using the start and end points to define the vertices.
        """
        points = [
            start,
            (end[0], start[1]),
            end
        ]
        pygame.draw.polygon(surface, color, points, 2)

    def draw_equilateral_triangle(surface, start, end, color):
        """
        Draws an equilateral triangle using the start and end points.  Calculates the third point.
        """
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        side_length = math.sqrt(dx**2 + dy**2)
        height = side_length * (math.sqrt(3) / 2)
        mid_x = (start[0] + end[0]) / 2
        apex_y = start[1] - height if end[1] > start[1] else start[1] + height # Corrected apex calculation.

        points = [
            start,
            end,
            (int(mid_x), int(apex_y))
        ]
        pygame.draw.polygon(surface, color, points, 2)

    def draw_rhombus(surface, start, end, color):
        """
        Draws a rhombus using the start and end points to define its diagonals.
        """
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        points = [
            (start[0], mid_y),
            (mid_x, start[1]),
            (end[0], mid_y),
            (mid_x, end[1])
        ]
        pygame.draw.polygon(surface, color, points, 2)

    def draw_square(surface, start, end, color):
        """Draws a square"""
        size = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
        rect = pygame.Rect(start[0], start[1], size, size)
        pygame.draw.rect(surface, color, rect, 2)
    # --- Main Game Loop ---

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                # --- Exit Shortcuts ---
                if (event.key == pygame.K_w and ctrl_held) or \
                   (event.key == pygame.K_F4 and alt_held) or \
                   event.key == pygame.K_ESCAPE:
                    return

                # --- Color Selection ---
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_w: #Added White
                    mode = 'white'

                # --- Tool Selection ---
                elif event.key == pygame.K_p:
                    tool = 'pen'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_m:
                    tool = 'rectangle'
                elif event.key == pygame.K_s:
                    tool = 'square'
                elif event.key == pygame.K_t:
                    tool = 'right_triangle'
                elif event.key == pygame.K_q:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_h:
                    tool = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    start_pos = event.pos
                    drawing = True
                    if tool == 'pen' or tool == 'eraser':
                        points = [event.pos]
                elif event.button == 3:  # Right click
                    radius = max(1, radius - 1)  # Prevent negative radius

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start_pos:
                    drawing = False
                    end_pos = event.pos
                    color = get_color(mode)  # Get color once for the shape

                    # --- Shape Drawing ---
                    if tool == 'circle':
                        center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                        radius_circle = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 / 2)
                        pygame.draw.circle(canvas, color, center, radius_circle, 2)
                    elif tool == 'rectangle':
                        rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                         abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                        pygame.draw.rect(canvas, color, rect, 2)
                    elif tool == 'square':
                        draw_square(canvas, start_pos, end_pos, color)
                    elif tool == 'right_triangle':
                        draw_right_triangle(canvas, start_pos, end_pos, color)
                    elif tool == 'equilateral_triangle':
                        draw_equilateral_triangle(canvas, start_pos, end_pos, color)
                    elif tool == 'rhombus':
                        draw_rhombus(canvas, start_pos, end_pos, color)
                    start_pos = None  # Reset start position after drawing

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if drawing and (tool == 'pen' or tool == 'eraser'):
                    points.append(position)
                    draw_line_between(canvas, len(points) - 2, points[-2], points[-1], radius,
                                      mode if tool == 'pen' else 'black')

        # --- Drawing on the screen ---
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(canvas, (0, 0))  # Draw the canvas onto the screen

        # --- Shape Preview ---
        if drawing and start_pos:
            current_pos = pygame.mouse.get_pos()
            color = get_color(mode) # Get the color for the preview
            if tool == 'circle':
                center = ((start_pos[0] + current_pos[0]) // 2, (start_pos[1] + current_pos[1]) // 2)
                radius_circle = int(((current_pos[0] - start_pos[0]) ** 2 + (current_pos[1] - start_pos[1]) ** 2) ** 0.5 / 2)
                pygame.draw.circle(screen, color, center, radius_circle, 2)
            elif tool == 'rectangle':
                rect = pygame.Rect(min(start_pos[0], current_pos[0]), min(start_pos[1], current_pos[1]),
                                     abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, color, rect, 2)
            elif tool == 'square':
                draw_square(screen, start_pos, current_pos, color)
            elif tool == 'right_triangle':
                draw_right_triangle(screen, start_pos, current_pos, color)
            elif tool == 'equilateral_triangle':
                draw_equilateral_triangle(screen, start_pos, current_pos, color)
            elif tool == 'rhombus':
                draw_rhombus(screen, start_pos, current_pos, color)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
