int n;
float rate = 10.;
int sp = 5;
final int m = 70;
int[][] colors;

void setup ()
{
  size(800, 600);
  n = 0;
  
  colors = new int[m][3];
  
  for (int i=0; i<m; i++)
  {
    float[] c = getColor((float)i/m);
    
    colors[i][0] = (int)(255*sqrt(c[0]));
    colors[i][1] = (int)(255*sqrt(c[1]));
    colors[i][2] = (int)(255*sqrt(c[2]));
  }
}


void draw ()
{
  background(0);
  
  for (int i=1; i<m; i++)
  {
    stroke(
            colors[i][0],
            colors[i][1],
            colors[i][2]
          );
    
    line(
          200*x1(n+i*sp)+400,
          200*y1(n+i*sp)+300,
          200*x2(n+i*sp)+400,
          200*y2(n+i*sp)+300
         );
  }
  
  n++;
}


float x1 (int k)
{
  return 4/5.*cos(k/(13*rate))+1/5.*sin(k/(7*rate)+.2);
}

float y1 (int k)
{
  return 2./3.*sin(k/(17*rate)) + 1/3.*sin(k/(2*rate));
}


float x2 (int k)
{
  return sin(k/(7*rate));
}

float y2 (int k)
{
  return (cos(k/(3*rate) + 2.) + sin(k/(5*rate))) / 2;
}


float[] getColor (float t)
{
  float[] c = new float[3];
  
  t = t*6;
  
  if (t<1)
  {
    c[0] = 1.;
    c[1] = t;
    c[2] = 0.;
  }
  else if (t<2)
  {
    c[0] = 2-t;
    c[1] = 1.;
    c[2] = 0.;
  }
  else if (t<3)
  {
    c[0] = 0.;
    c[1] = 1.;
    c[2] = t-2;
  }
  else if (t<4)
  {
    c[0] = 0.;
    c[1] = 4-t;
    c[2] = 1.;
  }
  else if (t<5)
  {
    c[0] = t-4;
    c[1] = 0.;
    c[2] = 1.;
  }
  else
  {
    c[0] = 1.;
    c[1] = 0.;
    c[2] = 6-t;
  }
  
  return c;
}