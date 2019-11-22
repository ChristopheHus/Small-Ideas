import java.util.*;

class Emitter 
{
  public float x, y;
  public float prevx, prevy;
  public float rad;
  float emSpeed, pSpeed;
  Particle particles;
  
  PImage img;
  
  Emitter (float posx, float posy, float area, float emissionSpeed, float particleSpeed)
  {
    x = posx;
    y = posy;
    prevx = posx;
    prevy = posy;
    rad = area/2f;
    emSpeed = emissionSpeed;
    pSpeed = particleSpeed;
    particles = new Particle(0,0,0);
    
    img = createImage(width, height, RGB);
  }
  
  void setEmissionSpeed (float speed)
  {
    emSpeed = speed;
  }
  
  void setpos(float x, float y)
  {
    this.x = x;
    this.y = y;
  }
  
  void draw (PGraphics src)
  {
    particles.draws(src);
  }
  
  void update(float dt)
  {
    particles.updates(dt);
    
    float im = emSpeed*dt;
    for (float i=0; i<1; i+=1/im)
    {
      float angle = random(0,2*PI), a2 = random(0,2*PI);
      float r = random(0,rad), r2 = random(0, pSpeed);
      
      float px = prevx * i + x * (1-i);
      float py = prevy * i + y * (1-i);
      
      Particle n = particles.next;
      particles.next = new Particle(px+cos(angle)*r, py+sin(angle)*r, r2*cos(a2), r2*sin(a2), 10);
      particles.next.next = n;
    }
    
    prevx = x;
    prevy = y;
  }
  
  void use(Vortex v)
  {
    v.apply(particles);
  }
}
