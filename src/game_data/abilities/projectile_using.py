from src.controllers.entity_handlers import AC_PROJECTILES


# part-parent class to all projectile-based skills and entities
class ProjectileUsing:

    def build_projectile(self, origin_entity, direction):
        return self.ProjectileClass()  # should be overridden

    def launch_projectile(self, origin_entity, direction):

        # builds projectiles with its main attributes like velocity and effect
        p = self.build_projectile(origin_entity, direction)

        # moves the new projectile to the location of its origin entity
        p.move_to(origin_entity.x, origin_entity.y)

        # instantly travels set spawn distance
        p.travel_air(direction, self.spawn_distance)

        # adds projectile to handlers
        AC_PROJECTILES.append(p)

    # constructor
    def __init__(self, projectile_class, spawn_distance=0.5):

        # class of the built projectiles
        self.ProjectileClass = projectile_class

        # a distance form origin entity to start location of the projectile
        self.spawn_distance = spawn_distance
