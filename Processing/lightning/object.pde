ArrayList<Lightning> elements = new ArrayList<Lightning>();

class Lightning
{
  final PImage left = loadImage("left.png");
  final PImage center = loadImage("center.png");
  final PImage right = loadImage("right.png");
  
  static final float alpha = 0.2f;
  
  float mEnds[] = new float[4];
  float mPts[];
  float mH[];
  
  
  public Lightning (float x1, float y1, float x2, float y2, int N)
  {
    mEnds[0] = x1;
    mEnds[1] = y1;
    mEnds[2] = x2;
    mEnds[3] = y2;
    
    mPts = new float[N];
    
    mPts[0] = 0.f;
    mPts[1] = 1.f;
    for (int i=2; i<N; i++)
    {
      float r = random(1);
      int j=i-1;
      
      while(mPts[j]>r)
      {
        mPts[j+1] = mPts[j];
        j--;
      }
      mPts[j+1] = r;
    }
    
    mH = new float[N];
    mH[0] = 0.f;
    mH[N-1] = 0.f;
    float tempH[] = new float[N];
    tempH[0] = 0.f;
    tempH[N-1] = 0.f;
    for (int i=1; i<N-1; i++)
      tempH[i] = random(-1,1);
    
    float l = dist(mEnds[0],mEnds[1],mEnds[2],mEnds[3]);
    for (int i=1; i<N-1; i++)
    {
      mH[i] = tempH[i] * (1 - (exp(alpha*(mPts[i-1]-mPts[i])) + exp(alpha*(mPts[i]-mPts[i+1]))) / 2.f)
                + tempH[i-1] * exp(alpha*(mPts[i-1]-mPts[i]))/2.f
                + tempH[i+1] * exp(alpha*(mPts[i]-mPts[i+1]))/2.f;
     /*mH[i] = (2*tempH[i] + tempH[i-1] + tempH[i+1]) / 4.f;*/
     
      if (random(10)>9){
        float x = interpolation(mEnds[0], mEnds[2], mPts[i]) - mH[i] * (mEnds[3]-mEnds[1]) / l * 10,
              y = interpolation(mEnds[1], mEnds[3], mPts[i]) + mH[i] * (mEnds[2]-mEnds[0]) / l * 10;
        float theta = random(-PI/6,PI/6);
        elements.add(new Lightning(x, y, cos(theta)*(mEnds[2]-x)+sin(theta)*(mEnds[3]-y) + x, cos(theta)*(mEnds[3]-y)-sin(theta)*(mEnds[2]-x) + y, N-i));
      }
    }
  }
  
  public void draw()
  {
    imageMode(CENTER);
    
    float l = dist(mEnds[0],mEnds[1],mEnds[2],mEnds[3]);
    
    for (int i=1; i<mPts.length; i++)
    {
      drawSeg(
        interpolation(mEnds[0],mEnds[2], mPts[i-1]) - mH[i-1] * (mEnds[3]-mEnds[1]) / l * 10,
        interpolation(mEnds[1],mEnds[3], mPts[i-1]) + mH[i-1] * (mEnds[2]-mEnds[0]) / l * 10,
        interpolation(mEnds[0],mEnds[2], mPts[i]) - mH[i] * (mEnds[3]-mEnds[1]) / l * 10,
        interpolation(mEnds[1],mEnds[3], mPts[i]) + mH[i] * (mEnds[2]-mEnds[0]) / l * 10
      );
    }
  }
  
  private void drawSeg(float x1, float y1, float x2, float y2)
  {
    pushMatrix();
    
    translate(x1, y1);
    rotate(atan2(y2-y1, x2-x1));
    
    pushMatrix();
    scale(dist(x1, y1, x2, y2), 0.02);
    image(center, 0.5f, 0);
    popMatrix();
    
    scale(0.02, 0.02);
    image(left, -40, 0);
    image(right, dist(x1, y1, x2, y2)/0.02+36.4, 0);
    
    popMatrix();
  }
  
  private float interpolation (float y1, float y2, float x)
  {
    return (y2-y1) * x + y1;
  }
  
  private int sgn (float x)
  {
    if (x>0)
      return 1;
    else if (x<0)
      return -1;
    else
      return 0;
  }
}
