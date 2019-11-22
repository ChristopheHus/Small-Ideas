public static final int L = 100;
float part[][] = new float[2*L+1][2*L+1];


class Blob {
  private float m_p[];
  private float m_v[];
  
  private float m_size;
  
  
  public Blob (float x, float y, float vx, float vy, float size) {
    m_p = new float[]{x,y};
    m_v = new float[]{vx,vy};
    m_size = size;
  }
  
  public void upd () {
    float a[] = acc(m_p,m_v);
    
    m_v[0] += a[0];
    m_v[1] += a[1];
    
    m_p[0] += m_v[0];
    m_p[1] += m_v[1];
    
    // Test m_p
    if (m_p[0]<m_size) {m_p[0] = m_size-m_p[0]; m_v[0] = -m_v[0];}
    else if (m_p[0]>=win_x-m_size){ m_p[0] = 2*win_x-2-m_size-m_p[0]; m_v[0] = -m_v[0];}
    
    if (m_p[1]<m_size) {m_p[1] = m_size-m_p[1]; m_v[1] = -m_v[1];}
    else if (m_p[1]>=win_y-m_size){ m_p[1] = 2*win_y-2-m_size-m_p[1]; m_v[1] = -m_v[1];}
  }
  
  public void render (float arr[][]) {
    for (int i=max(0,(int)m_p[0]-(int)(L*m_size/10)); i<win_x&&i<(int)m_p[0]+(int)(L*m_size/10); i++)
    for (int j=max(0,(int)m_p[1]-(int)(L*m_size/10)); j<win_y&&j<(int)m_p[1]+(int)(L*m_size/10); j++)
      arr[i][j] += part[i-(int)m_p[0]+L][j-(int)m_p[1]+L] * m_size/10;
  }
  
  public void setP (float x, float y) {
    m_p[0]=x;
    m_p[1]=y;
  }
}
