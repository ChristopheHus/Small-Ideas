import java.util.*;

PImage parTexture;

ArrayList<Particle> particles;

float dalpha = 0.01;
float dx = cos(dalpha);
float dy = sin(dalpha);

float angle;
boolean genPart;

void setup()
{
  size(800,600);
  
  parTexture = loadImage("particle.png");
  parTexture.resize(25,0);
  particles = new ArrayList<Particle> ();
  
  angle = 0.f;
  genPart = false;
}

void draw()
{
  if(genPart)
  {
    for (int i=0; i<20; i++)
    {
      float r = random(50);
      float theta =  2 * (int)random(6) * PI / 6 + random(PI/6) + angle;
      particles.add(new Particle(mouseX+r*cos(theta)+random(-1,1), mouseY+r*sin(theta), 4*cos(theta)+random(-1,1), 4*sin(theta), true, (int)random(70,150)));
    }
    angle += PI/6/12;
  }
  
  background(0);
  
  for (Particle p : particles)
    p.draw();
  
  stroke(255);
  textSize(12);
  text(particles.size(), 10, 10);
  text(frameRate, 10, 25);
  
  Iterator<Particle> iterator = particles.iterator();
  while(iterator.hasNext()){
    Particle p = iterator.next();
    
    float[] m = p.getP();
    float d = dist(0.f, 0.f, m[2], m[3]);
    float k = 1/100.;
    
    if(p.upd(-d*m[2]*k, -d*m[3]*k)){
        iterator.remove();
    }
  }
}

void mousePressed() {
  angle = 0.f;
  genPart = true;
}

void mouseReleased()
{
  genPart = false;
}
