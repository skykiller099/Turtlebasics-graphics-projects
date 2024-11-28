import turtle as t
import colorsys as cs

t.setup(800, 600)  
t.tracer(2)
t.bgcolor("black")
t.pensize(2)
t.speed(0)  

n = 100
h = 0

try:
    for i in range(500):
        for j in range(4):
            c = cs.hls_to_rgb(h, 0.5, 0.5)
            h += 1/n
            t.color(c)
            t.circle(49 + j*5, 90)
            t.forward(100)
            t.left(90)
        t.right(10)
    t.done() 
    
except t.Terminator:
    print("La fenêtre a été fermée de manière inattendue.")

except Exception as e:
    print(f"Une erreur s'est produite : {e}")

finally:
    print("Programme terminé.")
