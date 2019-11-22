float parts[][];


void setup ()
{
  size(800,600);
  
  parts = new float[4][4];
  
  for (int i=0; i<parts.length; i++)
  {
    parts[i][0] = random(0,800);
    parts[i][1] = random(0,600);
    parts[i][2] = random(-3,3);
    parts[i][3] = random(-3,3);
  }
  
  colorMode(HSB, 1);
}

void draw ()
{
  loadPixels();
  
  for (int i=0; i<width; i++)
  for (int j=0; j<height; j++)
  {
    float f[] = {0f,0f};
    
    for (int k=0; k<parts.length; k++)
    {
      calcF(i,j,k, f);
    }
    pixels[i + width*j] = color(hue(f), 1, value(f));
  }
  
  updatePixels();
  
  
  for (int k=0; k<parts.length; k++)
  {
    if (parts[k][0]+parts[k][2]<0 || parts[k][0]+parts[k][2]>=width)
      parts[k][2] = -parts[k][2];
    if (parts[k][1]+parts[k][3]<0 || parts[k][1]+parts[k][3]>=height)
      parts[k][3] = -parts[k][3];
    
    parts[k][0] += parts[k][2];
    parts[k][1] += parts[k][3];
  }
}

void calcF (int i, int j, int k, float[] f)
{
  float dx = parts[k][0]-i;
  float dy = parts[k][1]-j;
  
  float r = sqrt(dx*dx+dy*dy);
  
  f[0] += (- pow(5/r,6) + pow(5/r,2))*dx/r;
  f[1] += (- pow(5/r,6) + pow(5/r,2))*dy/r;
}

float hue (float f[])
{
  return (atan2(f[1], f[0])+PI)/PI/2;
}

float value(float f[])
{
  return pow(1/dist(0,0,f[0],f[1]),0.1);
}
