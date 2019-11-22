


void setup ()
{
  size (800,600);
}


void draw ()
{
  background (0);
  stroke(255,0,0);
  noFill();
  
  for (int i=0; i<200; i++)
    point(i,i);
  
}