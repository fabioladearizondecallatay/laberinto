#para definir la dimension del laberinto 
rows = 5
columns = 5

#para deinir una list de espacios blancos 
maze = [[' ' for _ in range(columns)] for _ in range(rows)]

#define las coordenadas de las casillas donde hay muro 
wall_coordinates = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# para marcar una X donde hay un muro 
for i, j in wall_coordinates:
    maze[i][j] = 'X'

#para que aparezca, hacemos un print 
for row in maze:
    print(' '.join(row))

