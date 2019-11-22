void setup()
{
  size(800,600);
  
  noLoop();
}

void draw ()
{
  // -100, 0.75 0.35
  // 80 1.5 0.8
  // 260 0.75 0.35
  
  System.out.println(red(toGrey(color(100,100,100))));
  
  loadPixels();
  
  float a = 1.5;
  float b = 0.8;
  
  for(int i=0; i<400; i++)
  {
    float s = -100*(400-i)/400. + 80*i/400.;
    float l = .35/a*(400-i)/400. + .8/a*i/400.;
    float h = 1./b*(400-i)/400. + 1.3/b*i/400.;
    
    color c = getCubeHelix(h,s,l,1.);
    color c2 = toGrey(c);
    for (int j=0; j<300; j++)
    {
      pixels[i+j*width] = c;
      pixels[i+(j+300)*width] = c2;
    }
  }
  
  
  for(int i=400; i<800; i++)
  {
    float s = 80*(800-i)/400. + 260*(i-400)/400.;
    float l = .8/a*(800-i)/400. + .35/a*(i-400)/400.;
    float h = 1.3/b*(800-i)/400. + 1./b*(i-400)/400.;
    
    color c = getCubeHelix(h,s,l,1.);
    color c2 = toGrey(c);
    for (int j=0; j<300; j++)
    {
      pixels[i+j*width] = c;
      pixels[i+(j+300)*width] = c2;
    }
  }
  
  for(int i=0; i<800; i++)
  for(int j=500; j<600; j++)
  {
    pixels[i+j*width] = color(0);
  }
  
  
  updatePixels();
}

color getCubeHelix(float h, float s, float l, float gamma)
{
  float lp = pow(l, gamma);
  float a = 2*h*lp*(1-lp);
  float p = 2*PI*(s+140)/360;
  
  float cp = cos(p);
  float sp = sin(p);
  
  float r = lp   +   a  *  (cp * (-0.027444022037703) + sp * (0.958546250158684));
  float g = lp   +   a  *  (cp * (-0.092323445726082) + sp * (-0.284936986554441));
  float b = lp   +   a  *  (cp * (0.995350795962739));
  
  r = linToS(r);
  g = linToS(g);
  b = linToS(b);
  
  return color(max(0,min(255,r*255)), max(0,min(255,g*255)), max(0,min(255,b*255)));
}

color toGrey (color c)
{
  float r = sToLin(red(c)/255.);
  float g = sToLin(green(c)/255.);
  float b = sToLin(blue(c)/255.);
  
  float grey = .2126*r + .7152*g + .0722*b;
  
  return color(linToS(grey)*255);
}

float sToLin (float v)
{
  if(v<=0.04045)
    return v/12.92;
  
  return pow((v+0.055)/1.055, 2.4);
}

float linToS(float v)
{
  if(v<=0.0031308)
    return 12.92*v;
  
  return 1.055 * pow(v,1/2.4) - .055;
}
