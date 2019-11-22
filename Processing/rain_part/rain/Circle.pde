public class Circle extends Particle
{
  private int t;
  
  public Circle(float x, float y, float dlife)
  {
    super(x, y, 0f, 0f, dlife);
    t = 0;
  }
  
  public void render()
  {
    stroke(255, 255*life);
    strokeWeight(2);
    noFill();
    ellipse(m_x,m_y, 2*t, 2*t);
  }
  
  
  public boolean update ()
  {
    t += 1;
    life -= dlife;
    return life>0;
  }
}
