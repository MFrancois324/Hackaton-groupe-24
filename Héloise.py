
def move(pose): 
    """demande la direction souhaité par l'utilisateur et renvoie les nouvelle position du joueur en prenant en paramètre l'ancienne position"""
    x, y = pose 

    direction = input("Où voulez-vous aller ? (gauche= g, droite= d, haut= h, bas= b) ")

    if direction == "g": 
        x -= 1
    elif direction == "d": 
        x += 1
    elif direction == "h":
        y += 1
    elif direction == "b": 
        y -= 1
    else:
        print("Direction invalide.")

    return (x, y)


position = (1, 1) # Position initiale
new_pos = move(position)


print(f"Ancienne position : {position}")
print(f"Nouvelle position : {new_pos}")
