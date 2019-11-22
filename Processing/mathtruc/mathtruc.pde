void setup()
{
  size(1000,500);
 
  noLoop();
}

void draw()
{
  background(0);
  
  
  loadPixels();
  
  for (int i=0; i<width/2; i++)
  for (int j=0; j<height; j++)
  {
    float x = (float)i/height * 20 - 10;
    float y = (float)j/height * 20 - 10;
    
    float l = sqrt(x*x + y*y);
    float alpha = atan2(y,x);
    
    pixels[i+j*width] = lumi(f(l), wheel((alpha+PI)*3/2/PI));
  }
  
  for (int i=width/2; i<width; i++)
  for (int j=0; j<height; j++)
  {
    float x = (float)(i-width/2)/height * 20 - 10;
    float y = (float)j/height * 20 - 10;
    
    
    float xp = 0;
    float yp = 0;
    
    if (x==0)
    {
      xp = Float.POSITIVE_INFINITY;
      yp = Float.POSITIVE_INFINITY;
    }
    else
    {
      xp = 1/x;
      yp = -y/x;
    }
    
    float l = sqrt(xp*xp + yp*yp);
    float alpha = atan2(yp,xp);
    
    pixels[i+j*width] = lumi(f(l), wheel((alpha+PI)*3/2/PI));
  }
  
  updatePixels();
}



color lumi(float t, color c)
{
  float r = colToLin(red(c)/255);
  float g = colToLin(green(c)/255);
  float b = colToLin(blue(c)/255);
  
  /*if (t<=0.5)
  {
    return color(
          255*linToCol(r*2*t),
          255*linToCol(g*2*t),
          255*linToCol(b*2*t));
  }
  else
  {
    return color(
          255*linToCol(r+(1-r)*pow(2*(t-.5),3)),
          255*linToCol(g+(1-g)*pow(2*(t-.5),3)),
          255*linToCol(b+(1-b)*pow(2*(t-.5),3)));
  }*/
  
  float a = luminosity(r,g,b);
  
  if (t<=a)
  {
    return color(
          255*linToCol(r*t/a),
          255*linToCol(g*t/a),
          255*linToCol(b*t/a));
  }
  else
  {
    return color(
          255*linToCol(r+(1-r)*(t-a)/(1-a)),
          255*linToCol(g+(1-g)*(t-a)/(1-a)),
          255*linToCol(b+(1-b)*(t-a)/(1-a)));
  }
}

color wheel(float t)
{
  if(t<1)
  {
    return color(255*linToCol(1-t), 255*linToCol(t),0);
  }
  else if (t<2)
  {
    return color(0, 255*linToCol(2-t),255*linToCol(t-1));
  }
  else
  {
    return color(255*linToCol(t-2), 0, 255*linToCol(3-t));
  }
}

float colToLin(float c)
{
  if (c<=0.04045)
    return c/12.92;
  else
    return pow((c+.055)/(1+.055), 2.4);
}

float linToCol (float c)
{
  if (c<=0.0031308)
    return 12.92*c;
  else
    return 1.055*pow(c,1/2.4)-.055;
}

float luminosity (float r, float g, float b)
{
  return 0.2126*r + 0.7152*g + 0.0722*b;
}

float f (float t)
{
  if (t==Float.POSITIVE_INFINITY)
  {
    return 1;
  }
  
  return 1 - pow(2,-t/10);
}
