ParticleManager pm;

float t;

void setup ()
{
  size(800,600);
  
  //blendMode(MAX);
  
  pm = new ParticleManager(10000);
  pm.add(new FireWork(new PVector(200,600), new PVector(0f, -300f)));
  
  t = millis()/1000f;
}


void draw ()
{
  background(0);
  stroke(255);
  
  text(frameRate, 10, 10);
  
  pm.draw();
  
  float dt = millis()/1000f - t;
  t = millis()/1000f;
  
  pm.upd(dt);
}
