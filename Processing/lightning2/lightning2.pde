import java.util.Iterator;

ArrayList<Line> lines;


void setup ()
{
  size (800, 600);
  
  lines = new ArrayList<Line>();
  lines.add(new Line(200.,100.,600.,400.));
  
  noLoop ();
}

void draw ()
{
  background(0);
  
  stroke(255);
  
  for (int k=0; k<7; k++)
  {
    ArrayList<Line> ls = new ArrayList<Line>();
    Iterator<Line> i = lines.iterator();
    while (i.hasNext()) {
       Line l = i.next();
       
       float p[] = l.getPerp(randomGaussian()*(.2+.005*k)+.5).getPoint(randomGaussian()*.1);
       float p1[] = l.getp1();
       float p2[] = l.getp2();
       
       ls.add(new Line(p1,p));
       ls.add(new Line(p,p2));
       
       if (random(1)<.6/k)
       {
         float r = randomGaussian()*.15+.7;
         float p3[] = {p[0] + (p[0]-p1[0])*r, p[1] + (p[1]-p1[1])*r};
         
         ls.add(new Line(p, p3));
       }
       
       
       i.remove();
    }
    for(Line l : ls)
      lines.add(l);
  }
  
  
  
  for(Line l : lines)
  {
    l.draw();
  }
}
