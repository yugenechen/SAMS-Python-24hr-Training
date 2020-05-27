def ColorReview():
    """Displays all colors availqable to pygame us.  It shoulbcycle through
        all colors auotmoatically.  Remember there are three numbers that
        create a color, so you'll need to cylce through them all, in all
        combinations, to see all the colors.  Also, remeber to make the game
        easy to close by listening for user input.
    """
    import pygame
    import sys
    from datetime import datetime

    pygame.init()
    startTime = datetime.now()
    xMax = 1370
    yMax = 735
    width = 5
    height = 6
    pageMax = int(xMax * yMax / (width * height))
    screen = pygame.display.set_mode((xMax, yMax))
    screen.fill((0, 0, 0))
    pygame.display.update()
    R = 0; G = 0; B = 0
    myColors = []
    i = 0
    x = 0
    y = 0
    for R in range(256):
        for G in range(256):
            for B in range(256):
                myColors.append((R, G, B))
                i += 1
    print('Finished base Colors!!!')
    for i in range(0, len(myColors)):
        color = myColors[i]
        x += width
        if x > xMax:
            x = 0
            y +=height
            if y >= yMax - height:
                y = 0
#        if (y== 0) and (x==0):
        if not x:
        # Print a line at a time to the screen
            pygame.display.update()
        #if (not y and not x):
        # Pause 1/2 a sec once a whole screen is completely printed
        #    pygame.time.wait(500)
        # print('Waiting 1/2 sec, color:'+ str(i) + ', y:' + str(y).strip('.0') +
        #      '  Row: ' + str((y/height)%(yMax/height)), i%pageMax)
        pygame.draw.rect(screen, color, (x, y, width, height))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                endTime = datetime.now()
                print("StartTime: " + startTime.strftime('%m/%d/%Y  %H:%M:%S'),
                      "   EndTime = ", endTime.strftime('%m/%d/%Y  %H:%M:%S')
                      )
                sys.exit("Normal Exit initiated by user.")
    endTime = datetime.now()
    print("StartTime: "+ startTime.strftime('%m/%d/%Y  %H:%M:%S'),
          "   EndTime = ", endTime.strftime('%m/%d/%Y  %H:%M:%S')
          )
    pygame.quit()
    sys.exit("Normal Exit Programm completed execution.")

"""
    # Draw a rectangle shape
    # Initialize rectangle
    step = 5
    xStart = 0; yStart = 0
    x = xStart; y = yStart
    width = 5; height = 5

    For i in range():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("Normal Exit initiated by user.")
                # Re-draw the object moved over a little
                x += 5
                if x >= 640:
                    x = xStart
                    y += step
                    if y>=480:
                        y = yStart
                pygame.draw.rect(screen, RED, (x, y, width, height))
                pygame.display.update()
                print("RED: ", x, y, width, height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("Normal Exit initiated by user.")
        elif pygame.key.get_pressed()[pygame.K_1]:
            colorChg = "R"
        elif pygame.key.get_pressed()[pygame.K_2]:
            colorChg = "G"
        elif pygame.key.get_pressed()[pygame.K_3]:
            colorChg = "B"
        elif (pygame.key.get_pressed()[pygame.K_PAGEDOWN] or
              pygame.key.get_pressed()[pygame.K_DOWN]):
            colorChg += 20
        elif (pygame.key.get_pressed()[pygame.K_PAGEUP] or
              pygame.key.get_pressed()[pygame.K_UP]):
            pass
"""