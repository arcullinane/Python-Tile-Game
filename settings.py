import pygame as pg
vec = pg.math.Vector2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = "manBlue_gun.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 30, 30)
BARREL_OFFSET = vec(30, 10)

# Weapon settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500, 'bullet_lifetime': 1000, 'rate': 250, 'kickback': 200, 'spread': 5, 'damage': 10, 'bullet_size': 'lg', 'bullet_count': 1}
WEAPONS['shotgun'] = {'bullet_speed': 400, 'bullet_lifetime': 500, 'rate': 900, 'kickback': 300, 'spread': 20, 'damage': 5, 'bullet_size': 'sm', 'bullet_count': 12}

#Mob settings
MOB_IMG = "zoimbie1_hold.png"
MOB_SPEEDS = [75, 100, 125, 150, 150]
MOB_HIT_RECT = pg.Rect(0, 0, 35, 35)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 100
DETECT_RADIUS = 400

#Wall image
WALL_IMG = "element_green_square.png"

#Effect images
MUZZLE_FLASHES = ["whitePuff15.png", "whitePuff16.png", "whitePuff17.png", "whitePuff18.png"]
FLASH_DURATION = 40
SPLAT_IMG = "splat green.png"
DAMAGE_ALPHA = [i for i in range(0, 255, 32)]

#Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

#items
ITEM_IMAGES = {"health": "health_pack.png", "shotgun": "obj_shotgun.png"}
HEALT_PACK_AMOUNT = 20
BOB_RANGE = 20
BOB_SPEED = 2
