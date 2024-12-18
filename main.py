from turtle import Screen
from PIL import Image
import time
import random
from aliens import Alien
from AlienAttackHeadquarter import Attack
from Spaceship import Spaceship
from Barriers import Barrier
from Scoreboard import Scoreboard
from SpaceCaptainAttack import Bullet


def initialize_attack():
    global attacks
    x = random.randint(-340, 340)
    y = 180
    attack = Attack(x, y)
    attacks.append(attack)


def detect_attack_barrier_clash():
    global attacks
    global barriers
    for attack in attacks:
        for barrier in barriers:
            if -20 < attack.xcor() - barrier.xcor() < 20 and attack.ycor() - barrier.ycor() < 20:
                barrier.hideturtle()
                barriers.remove(barrier)
                attack.hideturtle()
                attacks.remove(attack)


def detect_attack_spaceship_clash():
    global attacks
    global barriers
    global game_is_on
    for attack in attacks:
        if -20 < attack.xcor() - spaceship.xcor() < 20 and attack.ycor() - spaceship.ycor() < 20:
            return True


def detect_bullet_barrier_clash(bullet):
    global bullets
    global barriers
    for barrier in barriers:
        if -15 < bullet.xcor() - barrier.xcor() < 15 and barrier.ycor() - bullet.ycor() < 25:
            barrier.hideturtle()
            barriers.remove(barrier)
            bullet.hideturtle()
            bullets.remove(bullet)
            return True


def detect_bullet_attack_clash(bullet):
    global bullets
    global attacks
    for attack in attacks:
        if -15 < bullet.xcor() - attack.xcor() < 15 and attack.ycor() - bullet.ycor() < 25:
            attack.hideturtle()
            attacks.remove(attack)
            bullet.hideturtle()
            bullets.remove(bullet)
            return True


def detect_bullet_alien_clash(bullet):
    global bullets
    global aliens
    for alien in aliens:
        if -15 < bullet.xcor() - alien.xcor() < 15 and alien.ycor() - bullet.ycor() < 20:
            alien.hideturtle()
            aliens.remove(alien)
            bullet.hideturtle()
            bullets.remove(bullet)
            scoreboard.score += 1
            scoreboard.score_update()
            return True


def bullet_continuous_move(bullet):
    if not detect_bullet_barrier_clash(bullet) and not detect_bullet_alien_clash(
            bullet) and not detect_bullet_attack_clash(bullet):
        bullet.move_up()
        screen.update()
        screen.ontimer(lambda: bullet_continuous_move(bullet), 50)
    else:
        pass


def shoot():
    global bullets
    global spaceship
    bullet_y = spaceship.ycor() + 40
    bullet = Bullet(spaceship.xcor(), bullet_y)
    bullets.append(bullet)
    bullet_continuous_move(bullet)


img_alien = Image.open("peace-alien.gif")
img_alien = img_alien.resize((30, 30))
img_alien.save("peace-alien-small.gif")

img_drone = Image.open("drone.gif")
img_drone = img_drone.resize((20, 20))
img_drone.save("drone-small.gif")

img_spaceship = Image.open("tank.gif")
img_spaceship = img_spaceship.resize((60, 60))
img_spaceship.save("spaceship-small.gif")

screen = Screen()
screen.title("Space Invader Game")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.addshape("peace-alien-small.gif")
screen.addshape("drone-small.gif")
screen.addshape("spaceship-small.gif")
screen.listen()

scoreboard = Scoreboard()
spaceship = Spaceship()
screen.onkey(key="Right", fun=spaceship.move_right)
screen.onkey(key="Left", fun=spaceship.move_left)
screen.onkey(key="space", fun=shoot)

aliens = []
attacks = []
barriers = []
bullets = []

# initialize aliens
n = 0
alien_y = 280
latest_barrier_y = 80
for _ in range(3):
    alien_y -= 40
    alien_x = -420
    for _ in range(8):
        alien_x += 40
        alien = Alien(alien_x, alien_y)
        aliens.append(alien)
# initialize barriers
for _ in range(4):
    latest_barrier_x = -280
    latest_barrier_y -= 40
    for _ in range(14):
        barrier = Barrier(x=latest_barrier_x, y=latest_barrier_y)
        latest_barrier_x += 40
        barriers.append(barrier)

game_is_on = True
while game_is_on:
    screen.update()
    for _ in range(17):
        n += 1
        screen.update()
        time.sleep(0.5)
        for alien in aliens:
            alien.move_right()
        if n % 9 == 0:
            initialize_attack()
        for attack in attacks:
            attack.move_down()
        detect_attack_barrier_clash()
        if detect_attack_spaceship_clash():
            game_is_on = False
            scoreboard.game_over()
            break
        if not aliens:
            game_is_on = False
            scoreboard.announce_win()
            break
    if game_is_on:
        for _ in range(16):
            n += 1
            screen.update()
            time.sleep(0.5)
            for alien in aliens:
                alien.move_left()
            if n % 9 == 0:
                initialize_attack()
            for attack in attacks:
                attack.move_down()
            detect_attack_barrier_clash()
            if detect_attack_spaceship_clash():
                game_is_on = False
                scoreboard.game_over()
                break
            if not aliens:
                game_is_on = False
                scoreboard.announce_win()
                break

screen.exitonclick()
