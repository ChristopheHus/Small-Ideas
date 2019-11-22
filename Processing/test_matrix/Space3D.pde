class Vec3
{
  public float x, y, z, t;
  
  public Vec3 (float x, float y, float z, float t)
  {
    this.x = x;
    this.y = y;
    this.z = z;
    this.t = t;
  }
  
  public Vec3(float[] v)
  {
    x = v[0];
    y = v[1];
    z = v[2];
    t = v[3];
  }
}


class Matrix3
{
  public float[][] values;
  
  public Matrix3(float[][] matrix)
  {
    values = matrix;
  }
  
  public Matrix3 mult(Matrix3 m)
  {
    float[][] r = new float[4][4];
    
    for (int i=0; i<4; i++)
    for (int j=0; j<4; j++)
    {
      for (int k=0; k<4; k++)
      {
        r[i][j] += values[i][k] * m.values[k][j];
      }
    }
    
    values = r;
    
    return this;
  }
  
  public Vec3 mult(Vec3 v)
  {
    float[] r = new float[4];
    
    for (int i=0; i<4; i++)
    {
      r[i] += values[i][0] * v.x;
      r[i] += values[i][1] * v.y;
      r[i] += values[i][2] * v.z;
      r[i] += values[i][3] * v.t;
    }
    
    return new Vec3(r);
  }
}


class Space3
{
  ArrayList<Vec3> points;
  ArrayList<int[]> vertices;
  
  private Matrix3 proj;
  private float tana2m1;
  private float near;
  private float far;
  
  public Space3 (float alpha, float near, float far)
  {
    this.points = new ArrayList<Vec3>();
    this.vertices = new ArrayList<int[]>();
    
    tana2m1 = 1 / tan(PI*alpha/360);
    this.near = near;
    this.far = far;
    
    calculateProj();
  }
  
  public Space3 (ArrayList<Vec3> points, ArrayList<int[]> vertices, float alpha, float near, float far)
  {
    this.points = points;
    this.vertices = vertices;
    
    tana2m1 = 1 / tan(alpha/2);
    this.near = near;
    this.far = far;
    
    calculateProj();
  }
  
  public void addPoint(Vec3 p)
  {
    points.add(p);
  }
  
  public void addCouple(int[] c)
  {
    vertices.add(c);
  }
  
  private void calculateProj ()
  {
    proj = new Matrix3(new float[][]{
      {tana2m1 * height / width, 0f,      0f,                        0f},
      {0f,                       tana2m1, 0f,                        0f},
      {0f,                       0f,      (near+far) / (far-near),   2*near*far / (near-far)},
      {0f,                       0f,      1f,                        0f}
    });
  }
  
  public void apply(Matrix3 m)
  {
    for (int i=0; i<points.size(); i++)
    {
      points.set(i, m.mult(points.get(i)));
    }
  }
  
  public Space2 projection ()
  {
    ArrayList<Vec2> p = new ArrayList<Vec2>();
    Vec3 tmp;
    for (Vec3 v : points)
    {
      tmp = proj.mult(v);
      tmp.x /= tmp.t;
      tmp.y /= tmp.t;
      tmp.z /= tmp.t;
      
      p.add(new Vec2(tmp.x, tmp.y, 1f));
    }
    
    return new Space2 (p, vertices);
  }
}
