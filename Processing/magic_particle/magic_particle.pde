PImage p;
int i=0;

void setup ()
{
  size(800,600);
  
  p = loadImage("particles/aura.png");
  
}

void draw ()
{
  background(30,128,70);
  
  //blend(p,0,0, p.width,p.height, 0,0, p.width, p.height, MULTIPLY);
  
  tint(255,255,255, sqrt(40000 + 25535*sin(i/30f)));
  image(p,100,100);
  i++;
}
