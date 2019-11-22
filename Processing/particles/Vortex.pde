class Vortex
{
  float x,y;
  float speed, scale;
  float lifetime, lifemax;
  
  Vortex (float posx, float posy, float speed, float scale, float life)
  {
    x = posx;
    y = posy;
    
    this.speed = speed;
    this.scale = scale;
    lifetime = life;
    lifemax = life;
  }
  
  void apply(Particle part)
  {
    Particle p = part.next;
    
    while(p != null)
    {
      float dx = p.x - x;
      float dy = p.y - y;
      
      float coef = 1 / (1+(dx*dx+dy*dy)/scale);//4*lifetime/lifemax*(lifemax-lifetime)/lifemax
      
      p.vx += (-dy*speed-p.vx)*coef;
      p.vy += (dx*speed-p.vy)*coef;
      
      p = p.next;
    }
  }
  
  void update(float dt)
  {
    lifetime -= dt;
  }
  
  boolean isDead()
  {
    return lifetime<0 || x<-width || x>2*width || y<-height || y>2*height;
  }
}
