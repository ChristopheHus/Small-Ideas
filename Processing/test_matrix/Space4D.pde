class Vec4
{
  public float x, y, z, w, t;
  
  public Vec4 (float x, float y, float z, float w,float t)
  {
    this.x = x;
    this.y = y;
    this.z = z;
    this.w = w;
    this.t = t;
  }
  
  public Vec4 (float[] v)
  {
    x = v[0];
    y = v[1];
    z = v[2];
    w = v[3];
    t = v[4];
  }
}


class Matrix4
{
  public float[][] values;
  
  public Matrix4(float[][] matrix)
  {
    values = matrix;
  }
  
  public Matrix4 mult(Matrix4 m)
  {
    float[][] r = new float[5][5];
    
    for (int i=0; i<5; i++)
    for (int j=0; j<5; j++)
    {
      for (int k=0; k<5; k++)
      {
        r[i][j] += values[i][k] * m.values[k][j];
      }
    }
    
    values = r;
    
    return this;
  }
  
  public Vec4 mult(Vec4 v)
  {
    float[] r = new float[5];
    
    for (int i=0; i<5; i++)
    {
      r[i] += values[i][0] * v.x;
      r[i] += values[i][1] * v.y;
      r[i] += values[i][2] * v.z;
      r[i] += values[i][3] * v.w;
      r[i] += values[i][4] * v.t;
    }
    
    return new Vec4(r);
  }
}


class Space4
{
  ArrayList<Vec4> points;
  ArrayList<int[]> vertices;
  
  private Matrix3 proj;
  private float tana2m1;
  private float near;
  private float far;
  
  private Matrix4 camMat;
  private float camX, camY, camZ, camW;
  private float camA, camB, camC;
  
  public Space4 (float alpha, float near, float far)
  {
    this.points = new ArrayList<Vec4>();
    this.vertices = new ArrayList<int[]>();
    
    tana2m1 = 1 / tan(PI*alpha/360);
    this.near = near;
    this.far = far;
    
    calculateProj();
  }
  
  public Space4 (ArrayList<Vec4> points, ArrayList<int[]> vertices, float alpha, float near, float far)
  {
    this.points = points;
    this.vertices = vertices;
    
    tana2m1 = 1 / tan(alpha/2);
    this.near = near;
    this.far = far;
    
    calculateProj();
  }
  
  public void clear()
  {
    points.clear();
    vertices.clear();
  }
  
  public void addPoint(Vec4 p)
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
      {tana2m1*height/width,    0f,       0f,                        0f},
      {0f,         tana2m1,  0f,                        0f},
      {0f,         0f,       (near+far) / (far-near),   2*near*far / (near-far)},
      {0f,         0f,       1f,                        0f}
    });
  }
  
  public void apply(Matrix4 m)
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
    
    for (Vec4 v : points)
    {
      v = camMat.mult(v);
      tmp = proj.mult(
            new Vec3(v.x, v.y, sqrt(v.z*v.z + v.w*v.w), v.t)
      );
      tmp.x /= tmp.t;
      tmp.y /= tmp.t;
      
      p.add(new Vec2(tmp.x, tmp.y, 1f));
    }
    
    return new Space2 (p, vertices);
  }
  
  
  public void setCam(float x, float y, float z, float w, float a, float b, float c)
  {
    camX = x;
    camY = y;
    camZ = z;
    camW = w;
    
    camA = a;
    camB = b;
    camC = c;
  }
  
  
  private void genCamMat ()
  {
    float cA = cos(PI*camA), cB = cos(PI*camB), cC = cos(PI*camC);
    float sA = -sin(PI*camA), sB = -sin(PI*camB), sC = -sin(PI*camC);
    
    
    camMat = new Matrix4(new float[][]{
      {cC, 0, 0, -sC, 0},
      {0, 1, 0, 0, 0},
      {0, 0, 1, 0, 0},
      {sC, 0, 0, cC, 0},
      {0, 0, 0, 0, 1}
    }).mult(new Matrix4(new float[][]{
      {cB, 0, -sB, 0, 0},
      {0, 1, 0, 0, 0},
      {sB, 0, cB, 0, 0},
      {0, 0, 0, 1, 0},
      {0, 0, 0, 0, 1}
    })).mult(new Matrix4(new float[][]{
      {cA, -sA, 0, 0, 0},
      {sA, cA, 0, 0, 0},
      {0, 0, 1, 0, 0},
      {0, 0, 0, 1, 0},
      {0, 0, 0, 0, 1}
    })).mult(new Matrix4(new float[][]{
      {1, 0, 0, 0, -camX},
      {0, 1, 0, 0, -camY},
      {0, 0, 1, 0, -camZ},
      {0, 0, 0, 1, -camW},
      {0, 0, 0, 0, 1}
    }));
    
  }
}
