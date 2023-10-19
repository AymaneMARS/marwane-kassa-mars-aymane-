class Weapon:
    def __init__(self, ammunitions, weapon_range):
        self.ammunitions = ammunitions
        self.range = weapon_range

    def fire_at(self, x, y, z):
        if self.ammunitions == 0:
            raise NoAmmunitionError("Plus de munitions disponibles.")
        self.ammunitions -= 1

class AntiSurfaceMissileLauncher(Weapon):
    def __init__(self, x, y, z=0, ammunitions=50, weapon_range=100):
        super().__init__(ammunitions, weapon_range)
        self.surface_coordinates = (x, y, z)

    def fire_at(self, x, y, z):
        super().fire_at(x, y, z)
        if z != 0:
            raise OutOfRangeError("Les coordonnées z ne sont pas valides pour un missile anti-surface.")

class AntiAirMissileLauncher(Weapon):
    def __init__(self, x, y, z, ammunitions=40, weapon_range=20):
        super().__init__(ammunitions, weapon_range)
        if z <= 0:
            raise ValueError("La coordonnée z doit être supérieure à 0 pour une missile anti-air")
        self.surface_coordinates = (x, y, z)

    def fire_at(self, x, y, z):
        super().fire_at(x, y, z)
        if z <= 0:
            raise OutOfRangeError("Les coordonnées z ne sont pas valides pour un missile anti-air.")

class LanceTropilles(Weapon):
    def __init__(self, x, y, z, ammunitions=24, weapon_range=40):
        super().__init__(ammunitions,weapon_range)
        if z>0:
            raise ValueError("La coordonnée z doit être inferieure ou egale a 0 pour une lance tropilles")
        self.surface_coordinates = (x, y, z)

    def fire_at(self, x, y, z):
        super().fire_at(x, y, z)
        if z > 0:
            raise OutOfRangeError("Les coordonnées z ne sont pas valides pour une torpille.")





