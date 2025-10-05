import pygame
import math
import datetime


# Initialiser Pygame
pygame.init()

# Skærmopsætning
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Analogt Ur")
screen.fill((255, 255, 255)) # Hvid baggrund.


# Font til digital visning og dato
pygame.font.init()
digital_font = pygame.font.SysFont("Arial", 24)     # Lille tekst midt i uret
date_font = pygame.font.SysFont("Arial", 20)        # Endnu mindre til datoen

# Ur-center
center = (screen_size[0] // 2, screen_size[1] // 2)

# Radiusser
inner_radius = 150 # Hvor linjerne starter 
outer_radius = 200 # Hvor linjerne slutter


# Funktion: tegn en viser
def draw_hand(screen, angle_deg, length, color, width):
    angle_rad = math.radians(angle_deg - 90)  # -90 gør at 0° peger opad
    end_x = center[0] + length * math.cos(angle_rad)
    end_y = center[1] + length * math.sin(angle_rad)
    pygame.draw.line(screen, color, center, (end_x, end_y), width)

# Tegn 12 markeringer.
for angle in range(0, 360, 30):
    # Start og slutpunkt for hver streg. 
    start_x = center[0] + inner_radius * math.cos(math.radians(angle))
    start_y = center[1] + inner_radius * math.sin(math.radians(angle))
    end_x = center[0] + outer_radius * math.cos(math.radians(angle))
    end_y = center[1] + outer_radius * math.sin(math.radians(angle))

# Funktion: Tegn urskiven. 
def draw_clock_face(surface):
    surface.fill((255, 255, 255))
    pygame.draw.circle(surface, (0, 0, 0), center, outer_radius, 5)
    # Time-markeringer.
    for angle in range(0, 360, 30):
        start_x = center[0] + inner_radius * math.cos(math.radians(angle))
        start_y = center[1] + inner_radius * math.sin(math.radians(angle))
        end_x = center[0] + outer_radius * math.cos(math.radians(angle))
        end_y = center[1] + outer_radius * math.sin(math.radians(angle))
        # Tegn stregen. 
        pygame.draw.line(surface, (0, 0, 0), (start_x, start_y), (end_x, end_y), 3)

# Loop: Kør uret.
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hent nuværende tid og dato
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    # Beregn vinkler og visere.
    second_angle = second * 6                           # 360° / 60 sekunder
    minute_angle = minute * 6 + second * 0.1            # 6° per minut + lidt for sekunder
    hour_angle = hour * 30 + minute * 0.5               # 30° per time + lidt for minutter

    # Tegn urskive og visere.
    draw_clock_face(screen)
    draw_hand(screen, hour_angle, 100, (0, 0, 0), 6)
    draw_hand(screen, minute_angle, 140, (0, 0, 255), 4)
    draw_hand(screen, second_angle, 170, (255, 0, 0), 2)

# Digital tid midt i uret (HH:MMSS)
    time_str = now.strftime("%H:%M:%S")
    time_surface = digital_font.render(time_str, True, (0, 0, 0))
    time_rect = time_surface.get_rect(center=(center[0], center[1] + 60))
    screen.blit(time_surface, time_rect)

# Dato nederst på skærmen (DD-MM-YYY)
    date_str = now.strftime("%d-%m-%Y")
    date_surface = date_font.render(date_str, True, (0, 0, 0))
    date_rect = date_surface.get_rect(center=(center[0], screen_size[1] - 150))
    screen.blit(date_surface, date_rect)



    # Opdater skærm
    pygame.display.flip()
    clock.tick(60)  # 60 FPS



# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears