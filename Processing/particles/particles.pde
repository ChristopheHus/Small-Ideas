Emitter e;
Vortex v1, v2;
float time;
PShader blur;
PGraphics src;
PGraphics pass1, pass2;

void setup ()
{
  size(800,600, P2D);
  
  src = createGraphics(width, height, P2D); 
 
  pass1 = createGraphics(width, height, P2D);
  pass1.noSmooth();  
 
  pass2 = createGraphics(width, height, P2D);
  pass2.noSmooth();
  
  e = new Emitter(400,300,5, 5000, 5);
  v1 = new Vortex (400,400, 20, 7, 1000);
  v2 = new Vortex (500,200, 5, 20, 1000);
  time = millis()/1000f;
  //time = 0;
  calcMotion(time);
  
  blur = loadShader("blur.glsl");
  
  blur.set("blurRad", 20);
  blur.set("sigma", 10.);
}


void draw ()
{
  src.beginDraw();
  src.background(0,0);
  
  src.loadPixels();
  e.draw(src);
  src.updatePixels();
  src.endDraw();
  
  blur.set("blurVec", 1., 0.);
  pass1.beginDraw();
  pass1.background(0);
  pass1.image(src, 0, 0);
  pass1.shader(blur);
  pass1.endDraw();
  
  blur.set("blurVec", 0., 1.);
  pass2.beginDraw();
  pass2.image(pass1, 0, 0);
  pass2.shader(blur);
  pass2.endDraw();
  
  background(0);
  image(pass2, 0, 0);
  image(src, 0, 0);
  
  float t = millis()/1000f-time;
  e.update(t);
  time = millis()/1000f;
  
  //e.use(v1);
  //e.use(v2);
  
  
  calcMotion(time);
  
  fill(255, 0, 0);
  text(frameRate, 10, 10);
}

void calcMotion(float t)
{
  v1.x = e.x;
  v1.y = e.y;
  v1.speed += random(-.3,.3);
  //time += .015;
  e.setpos(400+200*cos(time)+50*sin(sqrt(3)*t),300+200*sin(sqrt(2)*t));//millis()/1000f 500
  //e.setpos(mouseX,mouseY);
}
