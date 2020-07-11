file = open('planets.txt', 'w', encoding='utf-8')
solar_planets = ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptun\n']
file.writelines(solar_planets)
file.close()
# create the planets.txt
