abstract class Particle
{
  protected float m_x, m_y;
  protected float m_vx, m_vy;
  
  protected float life;
  protected float dlife;
  
  public Particle (float posx, float posy, float vx, float vy, float dlife)
  {
    m_x = posx;
    m_y = posy;
    m_vx = vx;
    m_vy = vy;
    life = 1f;
    this.dlife = dlife;
  }
  
  
  public abstract void render ();
  public abstract boolean update ();
}

class Manager
{
  protected ArrayList<Particle> m_particles;
  
  public Manager ()
  {
    m_particles = new ArrayList<Particle> ();
  }
  
  public void add (Particle p)
  {
    m_particles.add(p);
  }
  
  public void remove(Particle p)
  {
    m_particles.remove(p);
  }
  
  public void render ()
  {
    for (Particle p : m_particles)
      p.render();
  }
  
  public void update ()
  {
    Iterator<Particle> iter =  m_particles.iterator();
    while(iter.hasNext()){
      Particle p = iter.next();
      if(!p.update()){
          iter.remove();
      }
    }
  }
}
