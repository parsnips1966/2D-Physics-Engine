import pygame, sys, pymunk

def create_apple(space):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = (400, 0)
    shape = pymunk.Circle(body, 80)
    space.add(body, shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        x = int(apple.body.position.x)
        y = int(apple.body.position.y)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 80)

def create_static_ball(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (500, 500)
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape

def draw_static_balls(balls):
    for ball in balls:
        x = int(ball.body.position.x)
        y = int(ball.body.position.y)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 50)

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 500)
apples = []
apples.append(create_apple(space))
balls = []
balls.append(create_static_ball(space))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((217, 217, 217))
    draw_apples(apples)
    draw_static_balls(balls)
    space.step(0.02)
    pygame.display.update()
    clock.tick(60)

