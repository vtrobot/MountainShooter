import pygame 

print ('setup start')
pygame.init()

windows=pygame.display.set_mode(size=(640,480))
print ('setup end')

print ("start loop")

while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()


