class Particle
{
  float mx, my;
  float mvx, mvy;
  boolean mG;
  ColorFunction mcf;
  int life, lifeMax;
  
  
  Particle (float x, float y, float vx, float vy, boolean useG, int lifeTime, ColorFunction fnct)
  {
    mx = x;
    my = y;
    mvx = vx;
    mvy = vy;
    mG = useG;
    mcf = fnct;
    life = lifeTime;
    lifeMax = lifeTime;
  }
  
  void render ()
  {
    
  }
}
