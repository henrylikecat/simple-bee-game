import pgzrun,random
score=0
WIDTH=900
HEIGHT=800
TITLE="bee game!"
bee=Actor("bee")
bee.pos=450,400
flower=Actor("flower")
flower.pos=550,400
def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("flowers:"+str(score),color=(255, 0, 0),topright=(870,10))
def update():
    global score
    if keyboard.a:
        bee.x-=2
    if keyboard.d:
        bee.x+=2
    if keyboard.s:
        bee.y+=2
    if keyboard.w:
        bee.y-=2
    fc=bee.colliderect(flower)
    if fc:
        flower.x=random.randint(100,800)
        flower.y=random.randint(100,700)
        score+=1
pgzrun.go()