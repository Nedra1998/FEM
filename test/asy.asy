settings.outformat="png";
settings.render=4;
settings.prc = false;
import graph3;

size(12cm,0);
currentprojection=orthographic(3,2,4);
currentlight=(5,3,0);

real crs(pair z) {
  return (8*z.x+z.y*z.x^2*16);
}
real dok(pair z) {
  return (z.y*z.x^2*24);
}
draw(surface(dok, (0,0),(1,1),nx=32,Spline),green);
draw(surface(crs, (0,0),(1,1),nx=32,Spline),blue);
