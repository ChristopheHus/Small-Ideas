import java.util.Iterator;
import java.util.Collections;

class ColorValue implements Comparable<ColorValue>
{
  public color c;
  public float t;
  
  public ColorValue(color col, float val)
  {
    c = col;
    t = val;
  }
  
  public int compareTo(ColorValue o)
  {
    return (int)Math.signum(t-o.t);
  }
}


class ColorSlide
{
  ArrayList<ColorValue> colors;
  
  
  public ColorSlide(color init, color end)
  {
    colors = new ArrayList<ColorValue>();
    colors.add(new ColorValue(init,0));
    colors.add(new ColorValue(end,1));
  }
  
  public void add(color col, float val)
  {
    colors.add(new ColorValue(col,val));
    Collections.sort(colors);
  }
  
  public color get(float value)
  {
    if (value>=1)
      return colors.get(colors.size()-1).c;
    if (value<=0)
      return colors.get(0).c;
    
    Iterator<ColorValue> i = colors.iterator();
    ColorValue lastCV = colors.get(0);
    
    while(i.hasNext())
    {
      ColorValue tmp = i.next();
      if (tmp.t > value)
      {
        float coef = (value - lastCV.t) / (tmp.t - lastCV.t);
        float r = coef * red(tmp.c) + (1-coef) * red(lastCV.c);
        float g = coef * green(tmp.c) + (1-coef) * green(lastCV.c);
        float b = coef * blue(tmp.c) + (1-coef) * blue(lastCV.c);
        return color(r,g,b);
      }
      lastCV = tmp;
    }
    return color(0);
  }
}
