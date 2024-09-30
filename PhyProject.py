import pygame
from sys import exit
pygame.init()
pygame.font.init()
import math

grey = (128, 128, 128)
WHITE = (235, 211, 205)
RANDOM = (200, 200, 200)
blue = (5, 53, 80)
yellow = (255,255,0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
white = (255, 255, 255)

#lists 
Refractive_Indices = [0,1, 1.333, 1.45, 1.51,]
colours = [0, white, blue, yellow, RANDOM, grey]


print("*NOTE: Enter n_1 less than n_2 to avoid mathematical errors.")

#input section
Incident_Angle = int(input("Enter incident angle: " ))
Incident_Angle = int(Incident_Angle)
transmittance_angle = Incident_Angle

print("1. air\n2. water\n3. oil\n4. glass\n5. user value(n1)")

Medium_Choose_1 = int(input("Choose the number for first medium: "))

if Medium_Choose_1 == 5:
    your_value = input("enter the value for n1 you want: ") #if user chooses "5" (user input) to convert into n_1 for calculation
    n_1 = your_value
print("1. air\n2. water\n3. oil\n4. glass\n5. user value(n2)")

Medium_Choose_2 = int(input("Choose the number for second medium: "))

#calling value of list from user input

if Medium_Choose_2 == 5:
    value2 = input("enter the value for n2 you want: ")
    n_2 = value2

while True:
    if Medium_Choose_1  < 5:
        n_1 = Refractive_Indices[Medium_Choose_1]
        if Medium_Choose_2 < 5:
            n_2 = Refractive_Indices[Medium_Choose_2]
            break
    else:break

n_1 = float(n_1)
n_2 = float(n_2)

colour = colours[Medium_Choose_2]

#creating pygame window
WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("simulation")
WHITE = (235, 211, 205)
RANDOM = (200, 200, 200)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
FPS = 60
Line_One = pygame.Rect(170, HEIGHT/2 - 2 , 500, 2)
Line_Two = pygame.Rect(170, HEIGHT/2 + 112 , 500, 2)


n_3 = n_1
print(f"{n_1}\n{n_2}")

refractive_angle = math.asin((n_1/n_2) * (math.sin(Incident_Angle*math.pi/180 )))
#refractive_angle = int(math.radians(refractive_angle))

print("incident angle",Incident_Angle)
print("refractive angle",refractive_angle*180/math.pi)

#creating  a medium
medium = pygame.Surface((500, 110))
medium.fill(colour)

#intensity
if Incident_Angle == 0:
    reflection_percent = 100
else:
    reflection_percent = ((math.sin((Incident_Angle * math.pi / 180) - (refractive_angle)) / math.sin((Incident_Angle * math.pi / 180) + (refractive_angle )) )** 2) * 100


transmission_percent = 100 - reflection_percent

# defining display text
def display_text(text, x, y, size=32, color=(0, 0, 0)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    WIN.blit(text_surface, (x, y))

def text_display(text, x, y, size=32, color=(0, 0, 0)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    WIN.blit(text_surface, (x, y))

def draw_line_with_angle(start_pos, length, angle_degrees, width=2):
    angle_radians = math.radians(angle_degrees)
    end_pos = (
        start_pos[0] + length * math.cos(angle_radians),
        start_pos[1] - length * math.sin(angle_radians)
    )
    pygame.draw.line(WIN, (255, 0, 0), start_pos, end_pos, width)

# normal on the window
def normal():
    pygame.draw.line(WIN, RED, (300 , 320), (300 , 370), 2 )
    pygame.draw.line(WIN, RED, (300 , 320), (300 , 370), 2 )
    pygame.draw.line(medium, RED, (300 + 114 * math.tan(refractive_angle), HEIGHT/2 + 112 ), (300 + 114 * math.tan(refractive_angle), HEIGHT/2 + 120) , 2)

# text on window
def drawws():
    text_display("Physics simulation", 0, 50, size=50, color=(255, 0, 100))
    display_text(f"i)Incident angle is : {Incident_Angle}°", 435, 30, size=30, color=(255, 0, 100)) 
    display_text(f"ii)refracted angle is : {round(math.degrees(refractive_angle), 2)}°", 435, 60, size=30, color=(255, 0, 100))
    display_text(f"iii)intensity of reflected light is : {round(reflection_percent, 4)} ", 435, 90, size=30, color=(255, 0, 100))
    display_text(f"iv)intensity of transmitted light is : {round(transmission_percent, 4)}", 435, 120, size=30, color=(255, 0, 100)) 

# main window
def draw_window():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, Line_One)
    pygame.draw.rect(WIN, BLACK, Line_Two)
    
    WIN.blit(WIN,(0, 0))
    WIN.blit(medium, (170,HEIGHT/2 + 1))
    drawws()
    normal()
    draw_line_with_angle((300 , HEIGHT/2 - 2), 200, 90 + Incident_Angle, 3)
    draw_line_with_angle((300 , HEIGHT/2 - 2), 200, 90 - Incident_Angle, 3)
    draw_line_with_angle((300 + 114 * math.tan(refractive_angle), HEIGHT/2 + 112 ), 200, 270 +  Incident_Angle, 3)
    
    
    pygame.draw.line(WIN, RED, (300 , HEIGHT/2 - 2), ( 300 + 114 * math.tan(refractive_angle), HEIGHT/2 + 112 ), 2)
    pygame.display.update()

# calling 
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame .event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
        draw_window()
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()