class Particle
{
  public float x, y;
  public float vx, vy;
  
  float lifetime;
  float lifemax;
  
  Particle next;
  
  Particle (float posx, float posy, float life)
  {
    x = posx;
    y = posy;
    vx = 0f;
    vy = 0f;
    lifetime = life;
    lifemax = life;
    
    next = null;
  }
  
  Particle (float posx, float posy, float vx, float vy, float life)
  {
    x = posx;
    y = posy;
    this.vx = vx;
    this.vy = vy;
    lifetime = life;
    lifemax = life;
    
   next = null;
  }
  
  void draws(PGraphics src)
  {
    Particle p = next;
    
    while (p!=null)
    {
      p.draw(src);
      p = p.next;
    }
  }
  
  void updates(float dt)
  {
    Particle p = this;
    
    while (p!=null)
    {
      while (p.next!=null && p.next.isDead())
      {
        p.next = p.next.next;
      }
      p = p.next;
      if (p!=null)
      {
        p.update(dt);
      }
    }
  }
  
  
  
  void draw (PGraphics src)
  {
    if (y>=0 && x>=0 && y<height && x<width)
    {
      int i = (int)y*width + (int)x;
      int r = (int)red(src.pixels[i]);
      int g = (int)green(src.pixels[i]);
      int b = (int)blue(src.pixels[i]);
      
      r = (int)(r + (20+20*(1-lifetime/lifemax))*lifetime/lifemax);
      b = (int)(b + (40+30*lifetime/lifemax)*lifetime/lifemax);
      g = (int)(g + (20+20*(1-lifetime/lifemax))*lifetime/lifemax);
      
      
      src.pixels[i] = color(min(255,r),min(255,g),min(255,b));
    }
  }
  
  void update (float dt)
  {
    vx *= 1 - .005;
    vy *= 1 - .005;
    
    x += vx * dt;
    y += vy * dt;
    
    lifetime -= dt;
  }
  
  boolean isDead ()
  {
    return lifetime<0 || x<-100 || x>width+100 || y<-100 || y>height+100;
  }
}
