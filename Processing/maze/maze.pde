import java.util.Stack;
import java.util.Collections;

int line[];
int walls[][];
int next;
Stack<int[]> s = new Stack<int[]>();

void setup ()
{
  size (800, 600);
  
  line = new int[width];
  walls = new int[width][height];
  next = width;
  
  for (int j=0; j<height; j++)
  for (int i=0; i<width; i++)
    walls[i][j] = 0xF;
  
  for (int i=0; i<width; i++)
    line[i] = i;
  
  noLoop();
}

void draw ()
{  
  for(int y=0; y<height-1; y++)
  {
    for (int i=0; i<width-1; i++)
    {
      if (line[i]!=line[i+1] && random(2)<1)
      {
         walls[i][y] &= 0x17;
         walls[i+1][y] &= 0x1D;
         
         line[i+1] = line[i];
      }
    }
    
    int index = 0;
    int c;
    ArrayList<Integer> vals = new ArrayList<Integer>();
    while(index>-1)
    {
      c = line[index];
      vals.clear();
      int j = index;
      index = -1;
      for (int i=j; i<width; i++)
      {
        if (line[i]==c)
        {
          walls[i][y] |= 0x10;
          vals.add(i);
        }
        else
        {
          if (index==-1 && (walls[i][y]&0x10)==0)
          {
            index = i;
          }
        }
      }
      
      int r = (int)random(1, vals.size());
      Collections.shuffle(vals);
      
      for (int i=0; i<r; i++)
      {
        walls[vals.get(i)][y] &= 0x1B;
        walls[vals.get(i)][y+1] &= 0x1E;
      }
      for (int i=r; i<vals.size(); i++)
      {
        line[vals.get(i)] = next++;
      }
    }
  }
  
  for (int i=0; i<width-1; i++)
  {
    if (line[i]!=line[i+1])
    {
       walls[i][height-1] &= 0x7;
       walls[i+1][height-1] &= 0xD;
    }
  }
  
  
  loadPixels();
  
  for (int j=0; j<height; j++)
  for (int i=0; i<width; i++)
    pixels[i+j*width] = 0;
  flood(0,0);
  
  updatePixels();
  
  System.out.println("end");
}

void flood (int x, int y)
{
  s.push(new int[]{x, y, 0});
  
  while (!s.empty())
  {
    int i = s.peek()[0];
    int j = s.peek()[1];
    int c = s.pop()[2];
    pixels[i+j*width] = color(c/4);
    c = (c+1)%(4*255);
    
    if (i<width-1 && (walls[i][j] & 0x8)==0 && pixels[i+1+j*width]==0)
      s.push(new int[]{i+1, j, c});
    if (j<height-1 && (walls[i][j] & 0x4)==0 && pixels[i+(j+1)*width]==0)
      s.push(new int[]{i, j+1, c});
    if (i>0 && (walls[i][j] & 0x2)==0 && pixels[i-1+j*width]==0)
      s.push(new int[]{i-1, j, c});
    if (j>0 && (walls[i][j] & 0x1)==0 && pixels[i+(j-1)*width]==0)
      s.push(new int[]{i, j-1, c});
  }
}
