

# parent class to all skills available to the player
# should be inherited by any complete player skills
class PlayerAbility:

    # constructor
    def __init__(self, icon, name):

        # icon for display
        self.icon = icon

        # ability's name
        self.name = name

