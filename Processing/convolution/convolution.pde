class Complex
{
  float m_x, m_y;
  
  public Complex()
  {
    m_x = 0;
    m_y = 0;
  }
  
  public Complex(float x)
  {
    m_x = x;
    m_y = 0;
  }
  
  public Complex(float x, float y)
  {
    m_x = x;
    m_y = y;
  }
  
  public float re() {return m_x;}
  public float im() {return m_y;}
  
  public float abs() {return sqrt(m_x*m_x + m_y*m_y);}
  public float phase() {return atan2(m_y, m_x);}
  
  public Complex add(Complex o) {return new Complex(m_x+o.m_x, m_y+o.m_y);}
  public Complex sub(Complex o) {return new Complex(m_x-o.m_x, m_y-o.m_y);}
  public Complex mult(Complex o) {return new Complex(m_x*o.m_x - m_y*o.m_y, m_x*o.m_y + m_y*o.m_x);}
  public Complex div(Complex o) {return new Complex((m_x*o.m_x + m_y*o.m_y)/(o.m_x*o.m_x+o.m_y*o.m_y), (-m_x*o.m_y + m_y*o.m_x)/(o.m_x*o.m_x+o.m_y*o.m_y));}
  
  public void addOP(Complex o) {m_x = m_x+o.m_x; m_y = m_y+o.m_y;}
  public void subOP(Complex o) {m_x = m_x-o.m_x; m_y = m_y-o.m_y;}
  public void multOP(Complex o) {m_x = m_x*o.m_x - m_y*o.m_y; m_y = m_x*o.m_y + m_y*o.m_x;}
  public void divOP(Complex o) {m_x = (m_x*o.m_x + m_y*o.m_y)/(o.m_x*o.m_x+o.m_y*o.m_y); m_y = (-m_x*o.m_y + m_y*o.m_x)/(o.m_x*o.m_x+o.m_y*o.m_y);}
  
  public String toString() {return "(" + Float.toString(m_x) + ", " + Float.toString(m_y) + ")";}
}


PImage img;
PShader blur;
PGraphics pass1[], pass2[];


void setup ()
{
  size(926,622, P2D);
  img = loadImage("lena.jpg");
  
  pass1 = new PGraphics[1];
  pass2 = new PGraphics[1];
  
  pass1[0] = createGraphics(width, height, P2D);
  pass1[0].noSmooth();  
 
  pass2[0] = createGraphics(width, height, P2D);
  pass2[0].noSmooth();
  
  blur = loadShader("blur.glsl");
  
  blur.set("blurRad", 50);
  
  blur.set("blurVec", 1., 0.);
  pass1[0].beginDraw();
  pass1[0].shader(blur);
  pass1[0].image(img, 0, 0);
  pass1[0].endDraw();
  
  blur.set("blurVec", 0., 1.);
  pass2[0].beginDraw();
  pass2[0].shader(blur);
  pass2[0].image(pass1[0], 0, 0);
  pass2[0].endDraw();
  
  background(0);
  image(pass2[0], 0, 0);
  
  /*background(0);
  stroke(255);
  strokeWeight(4);
  point(480,300);*/
  
  
}

void draw ()
{
  
}
