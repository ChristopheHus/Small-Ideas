Space3 space;
Matrix3 rot;


void setup ()
{
  size(800,600);
  
  space = new Space3(70, 0.1, 10);
  
  space.addPoint(0,0,0);
  space.addPoint(1,0,0);
  
  space.setCam(0,1,-2,-.5,-.1);
  
  Quaternion q = new Quaternion(0,0,PI/3,0).exp();
  space.addPoint(q.toMat().mult(new Vec3(new float[]{1, 0, 0, 1})));
  
  q = new Quaternion(0,PI/3,0,0).exp();
  space.addPoint(q.toMat().mult(new Vec3(new float[]{1, 0, 0, 1})));
  
  /*q = new Quaternion(0,PI/3,PI/3,0).exp();
  space.addPoint(q.toMat().mult(new Vec3(new float[]{1, 0, 0, 1})));*/
  
  space.addCouple(new int[]{0,1});
  space.addCouple(new int[]{0,2});
  space.addCouple(new int[]{0,3});
  //space.addCouple(new int[]{0,4});
  
  System.out.println(space.points.get(1).x);
  System.out.println(space.points.get(1).y);
  
  rot = new Matrix3(new float[][]{
    {cos(0.01), 0, -sin(0.01), 0},
    {0, 1, 0, 0},
    {sin(0.01), 0, cos(0.01), 0},
    {0, 0, 0, 1}
  });
}


void draw ()
{
  background(0);
  
  space.apply(rot);
  
  Space2 s = space.projection();
  s.render();
}
