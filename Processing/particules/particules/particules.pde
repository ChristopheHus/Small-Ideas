
Particle particles = new Particle(0,0,0,0,1,0,0);
int n = 0;

void setup ()
{
  size(800, 600);
  
  noStroke();
  
}



void draw ()
{
  background (0);
  //if (n<1000)
  for (int i=0; i<20; i++)
  {
    float theta = random(0, 2*PI);
    float r = random(150,250);
    
    particles.push(new Particle(400+r*cos(theta), 300+r*sin(theta), random(-.5,.5), random(-.5,.5), (int)random(50,200), random(10.,20.), 0));//random(15., 30.), random(-.5,.5)
    
  }
  
  fill(255);
  textSize(32);
  text(Integer.toString(np), 10, 30);
  
  particles.dr();
  particles.upd();
  
  //n++;
  
}


float[] acc (float x, float y)
{
  float r = sqrt((x-400)*(x-400)+(y-300)*(y-300));
  float theta = atan2(y-300,x-400);
  
  //stroke(255);
  //line(400, 300, 400+50*cos(theta), 300+50*sin(theta));
  
  float b = 0.0001;//0.992;
  
  float[] f = {-b*r*cos(theta), -b*r*sin(theta)};
  
  
  return f;
}