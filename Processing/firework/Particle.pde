abstract class Particle
{
  protected PVector mp;
  protected PVector mv;
  protected float mm;
  
  private final static float g = 100f;
  
  public Particle (PVector position, PVector velocity, float mass)
  {
    mp = position;
    mv = velocity;
    mm = mass;
  }
  
  public abstract void draw ();
  
  public void upd(float dt)
  {
    mv.y += g * mm * dt;
    
    mp.x += mv.x * dt;
    mp.y += mv.y * dt;
  }
  
  public abstract boolean isDead();
}


class FireWork extends Particle
{
  protected PVector trail[];
  private final int L = 20;
  
  public FireWork (PVector position, PVector velocity)
  {
    super(position, velocity, 1f);
    
    trail = new PVector[L];
    
    for (int i=0; i<L; i++)
      trail[i] = new PVector(position.x, position.y);
  }
  
  public void draw ()
  {    
    stroke(255);
    strokeWeight(4);
    line(mp.x, mp.y, trail[0].x, trail[0].y);
    for (int i=1; i<L; i++)
    {
      stroke(255*(L-i)/L);
      line(trail[i-1].x, trail[i-1].y, trail[i].x, trail[i].y);
    }
    
    
    stroke(255);    
    strokeWeight(10);
    point(mp.x,mp.y);
  }
  
  public void upd(float dt)
  {
    for (int i=L-1; i>0; i--)
    {
      trail[i].x = trail[i-1].x;
      trail[i].y = trail[i-1].y;
    }
    trail[0].x = mp.x;
    trail[0].y = mp.y;
    
    super.upd(dt);
    
    if (isDead())
    {
      colorMode(HSB, 100);
      float angle = PI / 8;
      float hue = random(0,100);
      
      for (int i=0; i<16; i++)
      {
        pm.add(new ExplosionParticle(new PVector(mp.x, mp.y), new PVector((100-15*(i%2))*cos(angle*i),(100-15*(i%2))*sin(angle*i)), color(hue, 100, 100-10*(i%2))));
        pm.add(new ExplosionParticle(new PVector(mp.x, mp.y), new PVector(70*cos(angle*(i+.5)),70*sin(angle*(i+.5))), color(hue, 100, 80)));
      }
    }
  }
  
  public boolean isDead()
  {
    return mp.y > trail[0].y;
  }
}


class ExplosionParticle extends Particle
{
  protected color mc;
  protected float lifetime;
  
  public ExplosionParticle (PVector position, PVector velocity, color col)
  {
    super (position, velocity, 0.1f);
    
    mc = col;
    lifetime = 2f;
  }
  
  public void draw()
  {
    strokeWeight(4);
    stroke((0xffffff&mc) + ((int)(255*(lifetime>2f?1f:lifetime/2f))<<24));
    point(mp.x, mp.y);
  }
  
  public void upd(float dt)
  {
    mv.mult ((1-mv.mag()*dt/70));
    
    super.upd(dt);
    lifetime -= dt;
  }
  
  public boolean isDead()
  {
    return lifetime < 0f;
  }
}
