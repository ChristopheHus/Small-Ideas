float lambda;

int w = 1000;
int h = 1000;
int ox = 0;
int oy = 0;
int terW = 300;
int terH = 300;

float scl = 7;

float ww = w * scl;
float hh = h * scl;

float dx = 0;
float dy = 0;

float noise[][] = new float[w][h];

boolean keys[];

ColorSlide cs = new ColorSlide(color(71,200,79), color(255,255,255));


void setup ()
{
  size(800,600,P3D);
  keys = new boolean[]{false, false, false, false};
  
  lambda = 1.2;
  
  cs.add(color(15,164,27), .4);
  cs.add(color(145,115,62), .95);
  
  
  for (int k=0; k<7; k++)
  {
    float n[][] = genNoise(7-k, w, h);
    
    for (int i=0; i<w; i++)
    for (int j=0; j<h; j++)
      noise[i][j] += pow(0.5,k)*n[i][j];
  }
}


void draw ()
{
  background(0);
  
  translate(width/2, height/2);
  rotateX(PI/3);
  translate(-terW*scl/2, -terH*scl*3/4);
  
  //stroke(255);
  noStroke();
  //noFill();
  for (int y=0; y<terH-1; y++)
  {
    beginShape(TRIANGLE_STRIP);
    for (int x=0; x<terW; x++)
    {
      if (
        x+ox<w && x+ox>=0 &&
        y+1+oy<w && y+oy>=0
      )
      {
        fill(cs.get(noise[x+ox][y+oy]));
        vertex(x*scl,y*scl,100*noise[x+ox][y+oy]);
        fill(cs.get(noise[x+ox][y+oy+1]));
        vertex(x*scl,(y+1)*scl,100*noise[x+ox][y+oy+1]);
      }
    }
    endShape();
  }
  
  
  if (keys[0])
    oy-=5;
  if (keys[1])
    oy+=5;
  if (keys[2])
    ox-=5;
  if (keys[3])
    ox+=5;
}


void keyPressed()
{
  switch(keyCode)
  {
    case UP:
      keys[0] = true;
      break;
    case DOWN:
      keys[1] = true;
      break;
    case LEFT:
      keys[2] = true;
      break;
    case RIGHT:
      keys[3] = true;
      break;
  }
}

void keyReleased()
{
  switch(keyCode)
  {
    case UP:
      keys[0] = false;
      break;
    case DOWN:
      keys[1] = false;
      break;
    case LEFT:
      keys[2] = false;
      break;
    case RIGHT:
      keys[3] = false;
      break;
  }
}

float[][] genNoise(int N, int lX, int lY)
{
  int l = (int) pow(2,N);
  
  int n = lX/l + 2; // si 2^n on génère une ligne de trop volontairement
  int m = lY/l + 2;
  
  float[][] noise = new float[lX][lY];
  
  PVector vects[][] = new PVector[n][m];
  
  for (int i=0; i<n; i++)
  for (int j=0; j<m; j++)
  {
    float t = random(0,2*PI);
    vects[i][j] = new PVector(cos(t), sin(t), -log(random(0,1))/lambda);
  }
  
  for (int i=0; i<lX; i++)
  for (int j=0; j<lY; j++)
  {
    int X = i/l;
    int Y = j/l;
    float x = (float)(i%l)/l;
    float y = (float)(j%l)/l;
    
    float u = (vects[X][Y].x * x + vects[X][Y].y * y) * vects[X][Y].z;
    float v = (vects[X+1][Y].x * (x-1) + vects[X+1][Y].y * y) * vects[X+1][Y].z;
    float a = lerp(u, v, s_curve(x));
    u = (vects[X][Y+1].x * x + vects[X][Y+1].y * (y-1)) * vects[X][Y+1].z;
    v = (vects[X+1][Y+1].x * (x-1) + vects[X+1][Y+1].y * (y-1)) * vects[X+1][Y+1].z;
    float b = lerp(u, v, s_curve(x));
    noise[i][j] = lerp(a, b, s_curve(y));
  }
  
  return noise;
}

float s_curve(float x)
{
  return x*x*(3-2*x);
}
