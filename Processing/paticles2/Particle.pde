class Particle
{
  private float mx;
  private float my;
  private float mvx;
  private float mvy;
  private boolean ginfluence;
  private int lifetime;
  
  public Particle (float x, float y, float vx, float vy, boolean gravity, int life)
  {
    mx = x;
    my = y;
    mvx = vx;
    mvy = vy;
    ginfluence = gravity;
    lifetime = life;
  }
  
  public void draw ()
  {
    imageMode(CENTER);
    
    tint(color(220, min(180,2*lifetime), 0, min(255,2*lifetime)));
    image(parTexture, mx, my);
    /*strokeWeight(30);
    stroke(255, min(255,6*lifetime), 0, min(255,2*lifetime));
    point(mx, my);*/
  }
  
  public boolean upd ()
  {
    if (ginfluence)
      return upd((dx-1)*mvx - dy*mvy, dy*mvx + (dx-1)*mvy);
    
    return upd(0.f, 0.f);
  }
  
  public boolean upd (float fx, float fy)
  {
    mvx += fx;
    mvy += fy;
    
    mx += mvx;
    my += mvy;
    
    lifetime--;
    
    return mx<-10 || my<-1 || mx>width+10 || my>height+10 || lifetime<0;
  }
  
  public float[] getP()
  {
    return new float[]{mx, my, mvx, mvy};
  }
}
