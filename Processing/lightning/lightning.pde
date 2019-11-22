import java.util.*;

void setup ()
{
  size (800, 600);
  
  background(0);
  blendMode(ADD);
  
  elements.add(new Lightning(100,300, 700,300, 40));
  
  noLoop();
}

void draw ()
{
  for (Lightning l : elements)
    l.draw();
}
