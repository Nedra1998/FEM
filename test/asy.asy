settings.outformat="png";
settings.render=8;
settings.prc = false;
import graph3;

size(12cm,0);

pair p1=(0,0);
pair p2=(0,1);
pair p3=(1,0);

/* triple phi1(pair z) { */
/*   return (z.x, 1, z.y); */
 /* return (z.x*p1.x+z.y*p2.x+(1-z.x-z.y)*p3.x, z.x*p1.y+z.y*p2.y+(1-z.x-z.y)*p3.y, z.x); */
/* } */
real phi1(pair z) {
  real l1 = ((p2.y-p3.y)*(z.x-p3.x)+(p3.x-p2.x)*(z.y-p3.y))/((p2.y-p3.y)*(p1.x-p3.x)+(p3.x-p2.x)*(p1.y-p3.y));
  real l2 = ((p3.y-p1.y)*(z.x-p3.x)+(p1.x-p3.x)*(z.y-p3.y))/((p2.y-p3.y)*(p1.x-p3.x)+(p3.x-p2.x)*(p1.y-p3.y));
  real l3 = 1-l1-l2;
  return l1;
}
real phi2(pair z) {
  real l1 = ((p2.y-p3.y)*(z.x-p3.x)+(p3.x-p2.x)*(z.y-p3.y))/((p2.y-p3.y)*(p1.x-p3.x)+(p3.x-p2.x)*(p1.y-p3.y));
  real l2 = ((p3.y-p1.y)*(z.x-p3.x)+(p1.x-p3.x)*(z.y-p3.y))/((p2.y-p3.y)*(p1.x-p3.x)+(p3.x-p2.x)*(p1.y-p3.y));
  real l3 = 1-l1-l2;
  return l2;
}
real phi3(pair z) {
  real l1 = ((p2.y-p3.y)*(z.x-p3.x)+(p3.x-p2.x)*(z.y-p3.y))/((p2.y-p3.y)*(p1.x-p3.x)+(p3.x-p2.x)*(p1.y-p3.y));
  real l2 = ((p3.y-p1.y)*(z.x-p3.x)+(p1.x-p3.x)*(z.y-p3.y))/((p2.y-p3.y)*(p1.x-p3.x)+(p3.x-p2.x)*(p1.y-p3.y));
  real l3 = 1-l1-l2;
  return l3;
}
draw(surface(phi1,(0,0),(1,1),nx=32,Spline),
                   green+opacity(0.7),green);
draw(surface(phi2,(0,0),(1,1),nx=32,Spline),
                   red+opacity(0.7),red);
draw(surface(phi3,(0,0),(1,1),nx=32,Spline),
                   blue+opacity(0.7),blue);
