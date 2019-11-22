class Vec2
{
  public float x, y, t;
  
  public Vec2 (float x, float y, float t)
  {
    this.x = x;
    this.y = y;
    this.t = t;
  }
  
  public Vec2(float[] v)
  {
    x = v[0];
    y = v[1];
    t = v[2];
  }
}


class Matrix2
{
  public float[][] values;
  
  public Matrix2(float[][] matrix)
  {
    values = matrix;
  }
  
  public Matrix2 mult(Matrix2 m)
  {
    float[][] r = new float[3][3];
    
    for (int i=0; i<3; i++)
    for (int j=0; j<3; j++)
    {
      for (int k=0; k<3; k++)
      {
        r[i][j] += values[i][k] * m.values[k][j];
      }
    }
    
    values = r;
    
    return this;
  }
  
  public Vec2 mult(Vec2 v)
  {
    float[] r = new float[3];
    
    for (int i=0; i<3; i++)
    {
      r[i] += values[i][0] * v.x;
      r[i] += values[i][1] * v.y;
      r[i] += values[i][2] * v.t;
    }
    
    return new Vec2(r);
  }
}



class Space2
{
  ArrayList<Vec2> points;
  ArrayList<int[]> vertices;
  
  public Space2 (ArrayList<Vec2> points, ArrayList<int[]> vertices)
  {
    this.points = points;
    this.vertices = vertices;
  }
  
  public void apply(Matrix2 m)
  {
    for (int i=0; i<points.size(); i++)
    {
      points.set(i, m.mult(points.get(i)));
    }
  }
  
  public void render ()
  {
    stroke(120);
    strokeWeight(1);
    for (int[] v : vertices)
    {
      line(
        (points.get(v[0]).x+1f)*width/2f,
        (-points.get(v[0]).y+1f)*height/2f,
        (points.get(v[1]).x+1f)*width/2f,
        (-points.get(v[1]).y+1f)*height/2f
      );
    }
    
    stroke(255);
    strokeWeight(4);
    for (Vec2 v : points)
      point((v.x+1f)*width/2f,(-v.y+1f)*height/2f);
  }
}
