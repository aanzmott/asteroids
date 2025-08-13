"""
Entities package

This package contains all in-game objects.

Example usage:
    from entities import Player, Asteroid

    player = Player()
    asteroid = Asteroid()
"""

from .player import Player
from .asteroid import Asteroid
from .shot import Shot
from .asteroidfield import AsteroidField
# from .enemy import Enemy
# from .powerup import PowerUp
# from .particle import Particle

# __all__ = ["Player", "Asteroid", "Shot", "AsteroidField", "Enemy", "PowerUp", "Particle"]
__all__ = ["Player", "Asteroid", "Shot", "AsteroidField"]
