import pygame
import math
import numpy as np

def create_choices():
    """
    Produce a choice based on unique user inputs (up to 7 choices, for no reason).
    
    This function prompts the user for the number of choices desired,
    ensures uniqueness of choices, and allows correction of choices.
    """
    num_choices = int(input("How many choices do you want? "))
    if 2 <= num_choices <= 7: 
        choices = []
        for i in range(num_choices):
            choice = input(f"Enter choice {i+1}: ")
            while choice in choices:
                print("That choice is already in the list.")
                choice = input(f"Enter choice {i+1}: ")

            confirm = ''
            while confirm not in ['y', 'n', 'r']:
                confirm = input(f"Confirm '{choice}' (y/n). Or use (r) to reset: ").lower()

            if confirm == 'y':
                choices.append(choice)
            elif confirm == 'n':
                choices.append(choice)
                # Give the user a chance to correct the specific choice
                choice_idx = choices.index(choice)
                new_choice = input(f"Enter the corrected choice for '{choice}': ")
                choices[choice_idx] = new_choice
            else: #reset
                return create_choices()
        return choices
    else:
        print("Please enter a number between 2 and 7.")
        return create_choices()

pygame.init()

WIDTH, HEIGHT = 700, 700
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
DEFAULT_ROT_SPEED = 1
ROT_SPEED = DEFAULT_ROT_SPEED
RADIUS = 300
ARROW_LENGTH = 0.9 * RADIUS
DECEL_RATE = 0.001  #try to relate this to the number of choices


# Define button properties
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 50
BUTTON_X, BUTTON_Y = WIDTH - BUTTON_WIDTH - 10, HEIGHT - BUTTON_HEIGHT - 10

# Define number of choices and colors for each choice
choices = create_choices()
num_choices = len(choices)
colors = [
    (255, 0, 0),    # Red
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 255, 255),  # Cyan
    (0, 0, 255),    # Blue
    (255, 0, 255),  # Magenta
    (128, 128, 128) # Grey
]
screen = pygame.display.set_mode((WIDTH, HEIGHT))

angle = 0  # Start angle
running = True
rotating = False  # Start with the arrow not rotating
decelerating = False  # Start with no deceleration

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if BUTTON_X <= mouse_x <= BUTTON_X + BUTTON_WIDTH and BUTTON_Y <= mouse_y <= BUTTON_Y + BUTTON_HEIGHT:
                if rotating:
                    decelerating = True
                else:
                    rotating = True
                    ROT_SPEED = DEFAULT_ROT_SPEED  # Reset rotation speed

    if rotating:
        # Rotate the arrow
        angle += ROT_SPEED
        if angle >= 360:
            angle -= 360

        if decelerating:
            # If decelerating, decrease the rotation speed
            ROT_SPEED -= DECEL_RATE
            if ROT_SPEED <= 0:
                # If the rotation speed is 0 or less, stop rotating and decelerating
                rotating = False
                decelerating = False

    # Draw circle and arrow
    screen.fill((255, 255, 255))  # white background

    # Draw the black frame
    pygame.draw.circle(screen, (0, 0, 0), (CENTER_X, CENTER_Y), RADIUS + 3)

    # Create a font object
    font = pygame.font.Font(None, 36)

    # Draw the quadrants
    for i in range(num_choices):
        start_angle = i * (360 / num_choices)
        end_angle = (i + 1) * (360 / num_choices)
        points = [(CENTER_X, CENTER_Y)]
        for arc_angle in np.arange(start_angle, end_angle + 1):
            points.append((
                CENTER_X + RADIUS * math.cos(math.radians(arc_angle)),
                CENTER_Y + RADIUS * math.sin(math.radians(arc_angle))
            ))
        pygame.draw.polygon(screen, colors[i % len(colors)], points)

        # Draw the choice text
        text_surface = font.render(choices[i], True, (0, 0, 0))  # Black text
        text_rect = text_surface.get_rect(center=(
            CENTER_X + RADIUS/2 * math.cos(math.radians((start_angle + end_angle) / 2)),
            CENTER_Y + RADIUS/2 * math.sin(math.radians((start_angle + end_angle) / 2))
        ))
        screen.blit(text_surface, text_rect)

        # Draw black separators
        separator_pos = (
            CENTER_X + RADIUS * math.cos(math.radians(start_angle)),
            CENTER_Y + RADIUS * math.sin(math.radians(start_angle))
        )
        pygame.draw.line(screen, (0, 0, 0), (CENTER_X, CENTER_Y), separator_pos, 3)

    # Draw the arrow
    end_pos = (
        CENTER_X + ARROW_LENGTH * math.cos(math.radians(angle)),
        CENTER_Y + ARROW_LENGTH * math.sin(math.radians(angle))
    )
    pygame.draw.line(screen, (0, 0, 0), (CENTER_X, CENTER_Y), end_pos, 3)  # Draw the arrow in black

    # Draw the arrowhead
    arrow_angle = math.radians(angle)
    arrowhead_size = 20
    arrowhead_points = [
        end_pos,
        (
            end_pos[0] - arrowhead_size * math.cos(arrow_angle + math.pi / 6),
            end_pos[1] - arrowhead_size * math.sin(arrow_angle + math.pi / 6)
        ),
        (
            end_pos[0] - arrowhead_size * math.cos(arrow_angle - math.pi / 6),
            end_pos[1] - arrowhead_size * math.sin(arrow_angle - math.pi / 6)
        )
    ]
    pygame.draw.polygon(screen, (0, 0, 0), arrowhead_points)  # Draw the arrowhead in black

    # Draw the button
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT))
    if rotating:
        text = pygame.font.Font(None, 24).render("Stop", True, (0, 0, 0))
    else:
        text = pygame.font.Font(None, 24).render("Start", True, (0, 0, 0))
    screen.blit(text, (BUTTON_X + 10, BUTTON_Y + 10))

    pygame.display.flip()

pygame.quit()