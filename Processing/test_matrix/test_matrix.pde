Space4 space;
boolean shift;

Matrix4 leftx, rightx, downx, upx;
boolean lx, rx, dx, ux;
Matrix4 lefty, righty, downy, upy;
boolean ly, ry, dy, uy;


float ar;
float tana2;
float X;
float Y;

void setup ()
{
  size(800,600);
  
  float alpha = 70f;
  float far = 10f;
  float near = 0.1f;
  
  space = new Space4(alpha, near, far);
  space.setCam(0,0,-3,-3,0,0,0);
  
  shift = false;
  lx = false;
  rx = false;
  dx = false;
  ux = false;
  ly = false;
  ry = false;
  dy = false;
  uy = false;
  
  leftx = new Matrix4(
    new float[][]{
        {cos(0.01), 0f, sin(0.01), 0f, 0f},
        {0f, 1f, 0f, 0f, 0f},
        {-sin(0.01), 0f, cos(0.01), 0f, 0f},
        {0f, 0f, 0f, 1f, 0f},
        {0f, 0f, 0f, 0f, 1f}
      }
  );
  rightx = new Matrix4(
    new float[][]{
        {cos(0.01), 0f, -sin(0.01), 0f, 0f},
        {0f, 1f, 0f, 0f, 0f},
        {sin(0.01), 0f, cos(0.01), 0f, 0f},
        {0f, 0f, 0f, 1f, 0f},
        {0f, 0f, 0f, 0f, 1f}
      }
  );
  downx = new Matrix4(
    new float[][]{
        {cos(0.01), 0f, 0f, sin(0.01), 0f},
        {0f, 1f, 0f, 0f, 0f},
        {0f, 0f, 1f, 0f, 0f},
        {-sin(0.01), 0f, 0f, cos(0.01), 0f},
        {0f, 0f, 0f, 0f, 1f}
      }
  );
  upx = new Matrix4(
    new float[][]{
        {cos(0.01), 0f, 0f, -sin(0.01), 0f},
        {0f, 1f, 0f, 0f, 0f},
        {0f, 0f, 1f, 0f, 0f},
        {sin(0.01), 0f, 0f, cos(0.01), 0f},
        {0f, 0f, 0f, 0f, 1f}
      }
  );
  lefty = new Matrix4(
    new float[][]{
        {1f, 0f, 0f, 0f, 0f},
        {0f, cos(0.01), sin(0.01), 0f, 0f},
        {0, -sin(0.01), cos(0.01), 0f, 0f},
        {0f, 0f, 0f, 1f, 0f},
        {0f, 0f, 0f, 0f, 1f}
      }
  );
  righty = new Matrix4(
    new float[][]{
        {1f, 0f, 0f, 0f, 0f},
        {0f, cos(0.01), -sin(0.01), 0f, 0f},
        {0, sin(0.01), cos(0.01), 0f, 0f},
        {0f, 0f, 0f, 1f, 0f},
        {0f, 0f, 0f, 0f, 1f}
      }
  );
  downy = new Matrix4(
    new float[][]{
        {1f, 0f, 0f, 0f, 0f},
        {0f, cos(0.01), 0f, sin(0.01), 0f},
        {0, 0f, 1f, 0f, 0f},
        {0f, -sin(0.01), 0f, cos(0.01), 0f},
        {0f, 0f, 0f, 0f, 1f}
      }
  );
  upy = new Matrix4(
    new float[][]{
        {1f, 0f, 0f, 0f, 0f},
        {0f, cos(0.01), 0f, -sin(0.01), 0f},
        {0, 0f, 1f, 0f, 0f},
        {0f, sin(0.01), 0f, cos(0.01), 0f},
        {0f, 0f, 0f, 0f, 1f}
      }
  );
  
  //genTesseract();
  //genSimplex();
}



void draw ()
{
  background(0);
  
  Space2 s = space.projection();
  
  s.render();
  
  if (lx) space.apply(leftx);
  if (rx) space.apply(rightx);
  if (dx) space.apply(upx);
  if (ux) space.apply(downx);
  
  lx = false;
  rx = false;
  dx = false;
  ux = false;
  
  if (ly) space.apply(lefty);
  if (ry) space.apply(righty);
  if (dy) space.apply(upy);
  if (uy) space.apply(downy);
  
  ly = false;
  ry = false;
  dy = false;
  uy = false;
}


void keyPressed()
{
  if (key==CODED)
  {    
    switch(keyCode)
    {
    case SHIFT:
      shift = true;
      break;
    case UP:
      if (shift)
        uy = true;
      else
        ux = true;
      break;
    case DOWN:
      if (shift)
        dy = true;
      else
        dx = true;
      break;
    case LEFT:
      if (shift)
        ly = true;
      else
        lx = true;
      break;
    case RIGHT:
      if (shift)
        ry = true;
      else
        rx = true;
      break;
    }
  }
  else if (key=='a')
  {
    space.clear();
    genSimplex();
  }
  else if (key=='z')
  {
    space.clear();
    genTesseract();
  }
}

void keyReleased ()
{
  if (key==CODED)
    if (keyCode==SHIFT)
      shift = false;
}


void genTesseract ()
{
  for (int l=0; l<2; l++)
  for (int i=0; i<2; i++)
  for (int j=0; j<2; j++)
  for (int k=0; k<2; k++)
  {
    space.addPoint(new Vec4(new float[]{i*2-1, j*2-1, k*2-1, l*2-1, 1f}));
  }
  
  for (int i=0; i<4; i++) //<>//
  {
    space.addCouple(new int[]{2*i, 2*i+1});
    space.addCouple(new int[]{2*i+8, 2*i+9});
    space.addCouple(new int[]{i, i+4});
    space.addCouple(new int[]{i+8, i+12});
    space.addCouple(new int[]{((-2*i+9)*i-4)*i/3, ((-2*i+9)*i-4)*i/3+2});
    space.addCouple(new int[]{((-2*i+9)*i-4)*i/3+8, ((-2*i+9)*i-4)*i/3+10});
  }
  for (int i=0; i<8; i++)
  {
    space.addCouple(new int[]{i, i+8});
  }
}


void genSimplex ()
{
  space.addPoint(new Vec4(new float[]{0, 0, 0, 0, 1}));
  space.addPoint(new Vec4(new float[]{1, 0, 0, 0, 1}));
  space.addPoint(new Vec4(new float[]{.5, 0, .5*sqrt(3), 0, 1}));
  space.addPoint(new Vec4(new float[]{.5, sqrt(2./3.), .5/sqrt(3), 0, 1}));
  space.addPoint(new Vec4(new float[]{.5, sqrt(2./3.), .5/sqrt(3), .5*sqrt(5./2.), 1}));
  
  
  float a = sqrt(5./2.);
  space.apply(new Matrix4(new float[][]{
    {a, 0, 0, 0, -.5*a},
    {0, a, 0, 0, -.5*a/sqrt(3)},
    {0, 0, a, 0, -.5*a/sqrt(6)},
    {0, 0, 0, a, -.5*a/sqrt(10)},
    {0, 0, 0, 0, 1}
  }));
  
  
  for (int i=0; i<4; i++)
  for (int j=i+1; j<5;j++)
    space.addCouple(new int[]{i, j});
}
