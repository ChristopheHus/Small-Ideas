float x,y;
float vx,vy;
float fx, fy;


void setup ()
{
  size(800, 600);
  
  x = width/2;
  y = height/2;
  
  vx = 0;
  vy = 0;
  
  fx = 0;
  fy = 0;
}


void draw ()
{
  background(50);
  noStroke();
  stroke(255);
  ellipse(x,y, 50, min(50,2*(height-y)));
  
  fx = 0;
  fy = 0.2;
  
  if (x<25){
    vx = -vx;
    x=25;
  }
  else if (x>width-25){
    vx = -vx;
    x=width-25;
  }
  if (y<25){
    vy = -vy;
    y=25;
  }
  else if (y>height-25){
    fy += 2*(height-25-y);
  }
  
  vx += fx;
  vy += fy;
  
  x += vx;
  y += vy;
}
