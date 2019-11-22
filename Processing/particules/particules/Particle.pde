int np = 0;


class Particle
{
  private static final float s3 = 1.7320508075688772935274463415059;
  
  private float x, y;
  private float vx, vy;
  private int life;
  private float size;
  private int type;
  
  private Particle prec, next;

  
  public void dr ()
  {
    if (next!=null)
      next.draw();
  }
  
  public void upd ()
  {
    if (next!=null)
      next.update();
  }
  
  public void push (Particle p)
  {
    p.prec = this;
    p.next = next;
    if (next!=null)
      next.prec = p;
    next = p;
    
    np ++;
  }
  
  public Particle (float x, float y, float vx, float vy, int life, float size, int type)
  {
    this.x = x;
    this.y = y;
    this.vx = vx;
    this.vy = vy;
    this.life = life;
    this.size = size;
    this.type = type;
  }
  
  public void draw ()
  {
    fill(255,life,0, life);
    switch(type)
    {
    case 1:
      rect(x,y,size,size);
      break;
    case 2:
      triangle(x,y-size/2,x+size*s3/4,y+size/4,x-size*s3/4,y+size/4);
      break;
    default:
      ellipse(x, y, size, size);    
    }
    
    if (next!=null)
      next.draw();
  }
  
  public void update ()
  {
    life --;
    float f[] = acc(x,y);
    vx += f[0];
    vy += f[1];
    
    x += vx;
    y += vy;
    
    if (isDead())
    {
      prec.next = next;
      if (next != null)
        next.prec = prec;
      np --;
    }
    
    if (next!=null)
      next.update();
  }
  
  public boolean isDead ()
  {
    return life==0 || x+size<0 || y+size<0 || x-size>800 || y-size>600;
  }
}