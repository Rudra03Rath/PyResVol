def calculate_ooip(area, thickness, porosity, Sw, Bo):
    return (7758 * area * thickness * porosity * (1 - Sw)) / Bo
