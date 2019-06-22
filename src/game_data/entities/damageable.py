

# parent class to all entities that can be damaged (player, monsters, breakable obstacles)
class Damageable:

    def take_damage(self, dmg, dmg_type):

        # reduces taken damage by appropriate defence
        post_def_damage = dmg - self.defences[dmg_type]

        # still, the damage taken from an attack cannot be less than 1
        post_def_damage = 1 if post_def_damage < 1 else post_def_damage

        # the damage is applied
        self.curr_hp -= post_def_damage

    def heal(self, heal):

        # the healing is applied
        self.curr_hp += heal

        # current hp cannot exceed maximum hp
        self.curr_hp = self.max_hp if self.curr_hp > self.max_hp else self.curr_hp

    def is_dead(self):
        return self.curr_hp <= 0

    # constructor
    def __init__(self, hp=100, physical_def=0, fire_def=0, cold_def=0, lightning_def=0,
                 holy_def=0, shadow_def=0, acid_def=0):

        # entity's hit points, value of <= 0 means that the entity has been killed/destroyed
        # and should be marked as expired
        self.max_hp = hp
        self.curr_hp = hp

        # entity's defences against various types of damage
        self.defences = [
            physical_def,        # 0
            fire_def,            # 1
            cold_def,            # 2
            lightning_def,       # 3
            holy_def,            # 4
            shadow_def,          # 5
            acid_def             # 6
        ]


