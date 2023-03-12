


class NaturalStones:
    def __init__(
            self, 
            name, 
            physical_properties,
            density,
            schmidt_hardness,
            indirect_tensile,
            uniaxial_comp_str,
            bohme_nokta,
            ultrasonic):
        self.name =  name
        self.physical_properties = physical_properties
        self.density = density
        self.schmidt_hardness = schmidt_hardness
        self.indirect_tensile = indirect_tensile
        self.uniaxial_comp_str = uniaxial_comp_str
        self.bohme_nokta = bohme_nokta
        self.ultrasonic = ultrasonic

    def __str__(self):
        return \
            f"""Name: {self.name}
            Physical Properties: {self.physical_properties}
            Density: {self.density}
            Schmidt Hammer Hardness: {self.schmidt_hardness}
            Indirect Tensile: {self.indirect_tensile}
            Uniaxial Compressive Strength: {self.uniaxial_comp_str}
            Bohme Point Load Test: {self.bohme_nokta}
            Ultrasonic: {self.ultrasonic}
            """
    


kristal_vitrik = NaturalStones("Kristal Vitrik Tüf")
vitrik_litik = NaturalStones("Vitrik Litik Tüf")
lamprofir = NaturalStones("Lamprofir")