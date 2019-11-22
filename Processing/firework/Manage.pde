public class ParticleManager
{
  private Particle particles[];
  private int k;
  
  
  public ParticleManager (int n)
  {
    particles = new Particle[n];
    k = 0;
  }
  
  public void draw ()
  {
    for (int i=0; i<particles.length; i++)
      if (particles[i] != null)
        particles[i].draw();
  }
  
  public void upd (float dt)
  {
    for (int i=0; i<particles.length; i++)
      if (particles[i] != null)
        particles[i].upd(dt);
    
    for (int i=0; i<particles.length; i++)
      if (particles[i]!=null && particles[i].isDead())
        particles[i] = null;
  }
  
  public boolean add (Particle p)
  {
    int kk = k;
    
    while(particles[k]!= null)
    {
      k = (k==particles.length-1)? 0 : k+1;
      if (k==kk)
        return false;
    }
    
    particles[k] = p;
    k++;
    
    return true;
  }
  
  public void remove (int id)
  {
    particles[id] = null;
  }
  
  public void remove (Particle p)
  {
    for (int i=0; i<particles.length; i++)
    if (particles[i].equals(p))
    {
      particles[i] = null;
      return;
    }
  }
  
  public Particle get (int id)
  {
    return particles[id];
  }
}
