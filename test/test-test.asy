settings.prc = false;
settings.outformat="png";
settings.render=2;
import graph3;
import grid3;
size(12cm,0);

path3 phi1 = (0,0,0) -- (1,0,1) -- (0,1,0) -- cycle;
path3 phi2 = (0,0,1) -- (1,0,0) -- (0,1,0) -- cycle;
path3 phi3 = (0,0,0) -- (1,0,0) -- (0,1,1) -- cycle;

draw(surface(phi1),blue+opacity(0.7), light=nolight);
draw(surface(phi2),red+opacity(0.7), light=nolight);
draw(surface(phi3),green+opacity(0.7), light=nolight);