import pgzrun,random
score=0
WIDTH=900
HEIGHT=800
TITLE="bee game!"
bee=Actor("bee")
bee.pos=450,400
flower=Actor("flower")
flower.pos=550,400
gamovr=False
def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("flowers:"+str(score),color=(255, 0, 0),topright=(870,10))
    if gamovr:
        screen.fill("red")
        screen.draw.text("GAME OVER TIMES UP YOUR FINAL SCORE IS:"+str(score),center=(WIDTH/2,HEIGHT/2),fontsize=50,color="yellow")
def update():
    global score
    if keyboard.a:
        bee.x-=8
    if keyboard.d:
        bee.x+=8
    if keyboard.s:
        bee.y+=8
    if keyboard.w:
        bee.y-=8
    fc=bee.colliderect(flower)
    if fc:
        flower.x=random.randint(100,800)
        flower.y=random.randint(100,700)
        score+=1
def timeup():
    global gamovr
    gamovr=True
clock.schedule(timeup,60.0)
pgzrun.go()
