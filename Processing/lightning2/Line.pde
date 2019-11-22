class Line
{
  float[] p1, p2;
  
  public Line (float x1, float y1, float x2, float y2)
  {
    p1 = new float[]{x1,y1};
    p2 = new float[]{x2,y2};
  }
  
  public Line (float p1[], float p2[])
  {
    this.p1 = p1;
    this.p2 = p2;
  }
  
  public void draw ()
  {
    line(p1[0],p1[1],p2[0],p2[1]);
  }
  
  public float[] getPoint (float t)
  {
    return new float[]{(1-t)*p1[0]+t*p2[0], (1-t)*p1[1]+t*p2[1]};
  }
  
  public Line getPerp (float t)
  {
    float p[] = getPoint (t);
    
    return new Line(p[0],p[1], p[0]+p1[1]-p2[1], p[1]+p2[0]-p1[0]);
  }
  
  public float[] getp1()
  {
    return p1;
  }
  
  public float[] getp2()
  {
    return p2;
  }
}
