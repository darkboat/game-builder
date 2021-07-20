import pygame

class Game:
    def __init__(self, values):
        self.values = values
        self.screen = None

        self.loopFunctions= []
        self.events = []

        self.isRunning = True

        self.hasEventHandler = False
        self.handleFunction = ""

    def initEventHandler(self, function):
        self.hasEventHandler = True
        self.handleFunction = function
    
    def start(self):
        self.screen = pygame.display.set_mode((self.values["SCREENWIDTH"], self.values["SCREENHEIGHT"]))

        while self.isRunning:
            for func in self.loopFunctions:
                func()

            events = pygame.event.get()

            for event in events:
                if self.hasEventHandler:
                    self.handleFunction(event)

                for ev in self.events:
                    if event.type == ev[0] or ev[0] == "": ev[1](event)

                if event.type == pygame.QUIT:
                    self.isRunning = False

    def stop(self):
        self.isRunning = False

# game = Game({
#     "SCREENWIDTH": 800,
#     "SCREENHEIGHT": 800
# })

# def handleEvents(event):
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_ESCAPE:
#             game.stop()

# game.initEventHandler(handleEvents)

# game.start()