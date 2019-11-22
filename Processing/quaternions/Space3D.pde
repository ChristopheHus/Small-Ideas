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
  
  private Matrix3 camMat;
  private float camX, camY, camZ;
  private float camA, camB;
  
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
  
  public void addPoint(float x, float y, float z)
  {
    points.add(new Vec3(x,y,z,1));
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
    
    genCamMat();
    
    for (Vec3 v : points)
    {
      tmp = proj.mult(camMat.mult(v));
      tmp.x /= tmp.t;
      tmp.y /= tmp.t;
      tmp.z /= tmp.t;
      
      p.add(new Vec2(tmp.x, tmp.y, 1f));
    }
    
    return new Space2 (p, vertices);
  }
  
  public void setCam(float x, float y, float z, float a, float b)
  {
    camX = x;
    camY = y;
    camZ = z;
    
    camA = a;
    camB = b;
  }
  
  
  private void genCamMat ()
  {
    float cA = cos(PI*camA), cB = cos(PI*camB);
    float sA = -sin(PI*camA), sB = -sin(PI*camB);
    
    
    camMat = new Matrix3(new float[][]{
      {cB, 0, -sB, 0},
      {0, 1, 0, 0},
      {sB, 0, cB, 0},
      {0, 0, 0, 1}
    }).mult(new Matrix3(new float[][]{
      {cA, -sA, 0, 0},
      {sA, cA, 0, 0},
      {0, 0, 1, 0},
      {0, 0, 0, 1}
    })).mult(new Matrix3(new float[][]{
      {1, 0, 0, -camX},
      {0, 1, 0, -camY},
      {0, 0, 1, -camZ},
      {0, 0, 0, 1}
    }));
    
  }
}


class Quaternion
{
  float[] v;
  float t;
  
  public Quaternion (float x, float y, float z, float w)
  {
    t = w;
    v = new float[]{x,y,z};
  }
  
  public Quaternion exp()
  {
    float d = sqrt(t*t + v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
    float c = cos(d), s = sin(d);
    
    return new Quaternion (s*v[0]/d, s*v[1]/d, s*v[2]/d, c);
  }
  
  public Quaternion mult(Quaternion q)
  {
    return new Quaternion (
      t*q.t - v[0]*q.v[0] - v[1]*q.v[1] - v[2]*q.v[2],
      t*q.v[0] + v[0]*q.t + v[1]*q.v[2] - v[2]*q.v[1],
      t*q.v[1] - v[0]*q.v[2] + v[1]*q.t + v[2]*q.v[0],
      t*q.v[2] - v[0]*q.v[1] - v[1]*q.v[0] + v[2]*q.t
    );
  }
  
  public Matrix3 toMat()
  {
    return new Matrix3(new float[][]{
      {1-2*v[1]*v[1]-2*v[2]*v[2], 2*v[0]*v[1]-2*v[2]*t, 2*v[0]*v[2]+2*v[1]*t, 0},
      {2*v[0]*v[1]+2*v[2]*t, 1-2*v[0]*v[0]-2*v[2]*v[2], 2*v[1]*v[2]-2*v[0]*t, 0},
      {2*v[0]*v[2]-2*v[1]*t, 2*v[1]*v[2]+2*v[0]*t, 1-2*v[0]*v[0]-2*v[1]*v[1], 0},
      {0, 0, 0, 1}
    });
  }
}
