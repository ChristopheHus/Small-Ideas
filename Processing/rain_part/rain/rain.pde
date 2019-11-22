import java.util.*;

Manager m;

void setup ()
{
  size(800,600);
  m = new Manager();
  
  for (int i=0; i<100; i++)
    m.add(new Circle(random(50,750),random(50,550),random(0.005,0.05)));
  
  
  colorMode(RGB);
}

void draw ()
{
  background(0);
  
  m.render();
  m.update();
  
  m.add(new Circle(mouseX,mouseY,random(0.005,0.05)));
  /*for (int i=0; i<2; i++)
    m.add(new Circle(random(50,750),random(50,550),random(0.005,0.05)));*/
}
