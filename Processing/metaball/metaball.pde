final int win_x = 200;
final int win_y = 200;

final int n = 50;

float r = 10.;
float th = 1/(r*r);

float win_buf[][];
Blob blobs[] = new Blob[n];

PImage img;

void setup ()
{
  size(200, 200);
  //img = loadImage("texture2.png");
  //img.resize(79*3,79*3);
  //img.blend(0,0,79,79,0,0,79,79,ADD);
  
  for (int k=0; k<n; k++)
    blobs[k] = new Blob(
                 random(50,win_x-50),
                 random(50,win_y-50),
                 random(-2,2),
                 random(-2,2),
                 random(2,10)
               );
  
  win_buf = new float[win_x][win_y];
  
  for (int i=0; i<2*L+1; i++)
  for (int j=0; j<2*L+1; j++)
    part[i][j] = f(i-L, j-L);
  
}



void draw ()
{
  background(0);
  
  blobs[0].setP(mouseX, mouseY);
  
  for (int i=0; i<win_x; i++)
  for (int j=0; j<win_y; j++)
    win_buf[i][j] = 0.;
  
  for (int k=0; k<n; k++)
    blobs[k].render(win_buf);
  
  loadPixels();
  
  for (int i=0; i<win_x; i++)
  for (int j=0; j<win_y; j++)
  {
    if (win_buf[i][j] >= th)  pixels[i+j*win_x] = color(10,150,200);
    else                      pixels[i+j*win_x] = color(70);
  }
  
  updatePixels();
  
  for (int k=0; k<n; k++)
    blobs[k].upd();
}



float f (float x, float y)
{
  if (x==0 && y==0)
    return 1.;
  return 1. / (x*x + y*y);
}

float[] acc (float p[], float v[]){
  return new float[]{0,0};
}
