import pygame
from pygame.locals import *
from API import ChatGPT

# Initialize pygame
pygame.init()
# Set up the screen
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Study Pal")
# Set up the clock
clock = pygame.time.Clock()
# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
TEXT_COLOR = (103, 192, 117)
INPUT_TEXT_COLOR = BLACK
LETTER_TEXT_COLOR = GREEN
# Set up the fonts
font_small = pygame.font.Font(None, 20)
font_medium = pygame.font.Font(None, 28)
# Set up the input box
input_box = pygame.Rect(20, 20, 600, 32)
input_box_color_inactive = GRAY
input_box_color_active = WHITE
input_text = ''
input_box_active = False
# Set up the letter box
letter_box = pygame.Rect(560, 80, 50, 50)
letter_box_color_inactive = GRAY
letter_box_color_active = WHITE
letter_text = ''
letter_box_active = False
# Set up the output box
output_box = pygame.Rect(20, 72, 600, 388)
output_box_color = WHITE
output_text = ''
score, questionnum, correct_choice = 0, 1, 0

# Set up the ChatGPT API
chat_gpt = ChatGPT(api_key="YOUR API KEY") #enter your API key here to use
def draw_text(screen, text, color, font, rect):
    words = [word.split(' ') for word in text.splitlines()]  
    space = font.size(' ')[0]  
    max_width, max_height = rect.w, rect.h  
    x, y = rect.x, rect.y  
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = rect.x 
                y += word_height  
            screen.blit(word_surface, (x, y))
            x += word_width + space
        x = rect.x  
        y += word_height  
       
# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if input_box_active:
                if event.key == K_RETURN:
                    # Get question and answer from ChatGPT API
                    prompt = input_text.strip()
                    options = ["A", "B", "C", "D"]
                    answer = chat_gpt.get_answer(prompt, "Correct Answer", options)
                    (y, z, r, f, p) = ChatGPT.whichquestion(questionnum, options, answer)
                    options = [z, r, f, p]
                    correct_answer = ChatGPT.checkanswer(questionnum, answer)
                    # Display question and options in output box
                    output_text += "\n" + "   " + y + "\n"
                    for i in options:
                        output_text += "     " + i + "\n"
                    output_text += "\n"
                    # Update input and output boxes
                    input_text = ''
                    input_box_active = False
            if letter_box_active:
                if event.key == K_RETURN:
                    letter_text = ''.join(filter(str.isalnum, letter_text))
                    # Get user's answer and check if it is correct
                    output_text = ''
                    if letter_text.strip().lower()==correct_answer.strip().lower():
                        output_text += "\n" + "   Correct!"
                        score += 1
                    else:
                        if correct_answer.strip().lower()=="a":
                            correct_choice = z
                        if correct_answer.strip().lower()=="b":
                            correct_choice = r
                        if correct_answer.strip().lower()=="c":
                            correct_choice = f
                        if correct_answer.strip().lower()=="d":
                            correct_choice = p
                        output_text += "\n" + "   Incorrect. The correct answer was: " + str(correct_choice)
                    # Update question number
                    questionnum += 1
                    # Update screen
                    screen.fill(BLACK)
                    letter_text = ''
                    letter_box_active = False

                    (y, z, r, f, p) = ChatGPT.whichquestion(questionnum, options, answer)
                    options = [z, r, f, p]
                    correct_answer = ChatGPT.checkanswer(questionnum, answer)
                    # Display question and options in output box
                    output_text += 2*"\n" + "   " + y + "\n"
                    for i in options:
                        output_text += "     " + i + "\n"
                    output_text += "\n"
                    # Update input and output boxes
                    input_text = ''
                    input_box_active = False

                    if questionnum==11:
                        output_text = ''
                        screen.fill(BLACK)
                        letter_text = ''
                        letter_box_active = False
                        output_text = "\n" + "   Great job! Your score was: " + str(score) + "\x5c10."

        if event.type == MOUSEBUTTONDOWN:
            # Check if the user clicked on the input box
            if input_box.collidepoint(event.pos):
                # Toggle input box active
                input_box_active = not input_box_active
                letter_box_active = False
            # Check if the user clicked on the letter box
            elif letter_box.collidepoint(event.pos):
                # Toggle letter box active
                letter_box_active = not letter_box_active
                input_box_active = False
            else:
                input_box_active = False
                letter_box_active = False
        # Update input text if the input box is active
        if input_box_active:
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        # Update letter text if the letter box is active
        if letter_box_active:
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    letter_text = letter_text[:-1]
                else:
                    letter_text += event.unicode
            
    # Draw input and output boxes
    input_box_color = input_box_color_active if input_box_active else input_box_color_inactive
    letter_box_color = letter_box_color_active if letter_box_active else letter_box_color_inactive
    pygame.draw.rect(screen, input_box_color, input_box, 2)
    pygame.draw.rect(screen, output_box_color, output_box, 2)
    pygame.draw.rect(screen, letter_box_color, letter_box, 2)
    # Render and draw input and output text
    input_text_render = font_medium.render(input_text, True, TEXT_COLOR)
    input_text_rect = input_text_render.get_rect()
    input_text_rect.x = input_box.x + 5
    input_text_rect.y = input_box.y + 5
    # Render the output box text
    output_text_render = font_medium.render(output_text, True, TEXT_COLOR)
    output_text_rect = output_text_render.get_rect()
    output_text_rect.x = output_box.x + 5
    output_text_rect.y = output_box.y + 5
    # Render and draw letter text
    letter_text_render = font_medium.render(letter_text, True, LETTER_TEXT_COLOR)
    letter_text_rect = letter_text_render.get_rect()
    letter_text_rect.x = letter_box.x + 5
    letter_text_rect.y = letter_box.y + 5
    # Draw the output box text using the draw_text function
    draw_text(screen, output_text, TEXT_COLOR, font_medium, output_box)
    # Blit the input box and letter box to the screen
    screen.blit(input_text_render, input_text_rect)
    screen.blit(letter_text_render, letter_text_rect)
    # Update the display
    pygame.display.flip()
    # Limit the frame rate
    clock.tick(60)