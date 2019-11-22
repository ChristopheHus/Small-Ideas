void setup() {
  size(201,201);
  
  int xc = 100;
  int yc = 100;
  
  double a = sqrt(255) / 100;
  
  
  System.out.println((int)(255/d2(100*a,0)));
  
  background(0);
  loadPixels();
  
  for (int i=0; i<201; i++)
  for (int j=0; j<201; j++)
  {
    pixels[i+j*width] = color((int)(255/d2((i-xc)*a,(j-yc)*a)),(int)(255/d2((i-xc)*a,(j-yc)*a)),(int)(255/d2((i-xc)*a,(j-yc)*a)));
  }
  
  updatePixels();
}

void draw(){}


double d2 (double x, double y){
  if (x==0 && y==0)
    return 1;
  return x*x + y*y;
}