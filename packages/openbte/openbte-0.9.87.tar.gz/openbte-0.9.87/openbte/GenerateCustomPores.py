import numpy as np
import math
from shapely.geometry import Point
from shapely.geometry import MultiPolygon
from shapely.geometry import Polygon

def GenerateCustomPores(argv):
    
  Lx = float(argv['lx'])
  Ly = float(argv['ly'])
  frame_tmp = []
  frame_tmp.append([float(-Lx)/2,float(Ly)/2])
  frame_tmp.append([float(Lx)/2,float(Ly)/2])
  frame_tmp.append([float(Lx)/2,float(-Ly)/2])
  frame_tmp.append([float(-Lx)/2,float(-Ly)/2])
  frame = Polygon(frame_tmp)

  #Periodicity------------
  pbc = []
  pbc.append([0,0])
  if argv.setdefault('automatic_periodic',True):
   pbc.append([Lx,0])
   pbc.append([-Lx,0])
   pbc.append([0,Ly])
   pbc.append([0,-Ly])
   pbc.append([Lx,Ly])
   pbc.append([-Lx,-Ly])
   pbc.append([-Lx,Ly])
   pbc.append([Lx,-Ly])
   #---------------------

  if 'polygons' in argv:
   tmp = argv['polygons']
  else:
   f = open(argv['polyfile'],'r')
   a = [0]; tmp = []
   while not len(a) == 0:
    a = f.readline().split()
    if not len(a) == 0:
      poly = [float(i) for i in a]
      tmp.append(poly)
   #tmp = np.loadtxt(argv['polyfile'])
   #quit()
   #if np.ndim(tmp) == 1: tmp = [tmp]

 

  polygons = []
  for k in range(len(tmp)):
   poly_tmp = tmp[k]   
   poly = []
  
   for n in range(int(len(poly_tmp)/2)):
    x = poly_tmp[n*2]
    y = poly_tmp[n*2+1]
    poly.append([x,y])
   polygons.append(poly)


  polygons_new = []
  #shifting
  for poly in polygons:
   new_poly = []
   for p in poly:
    p[0] *= Lx  
    p[1] *= Ly 
    p[0] -= Lx/2.0
    p[1] -= Ly/2.0


  #Store only the intersecting polygons
  final = []
  for poly in polygons:
    for kp in range(len(pbc)):
     tmp = []
     for p in poly:
      cx = p[0] + pbc[kp][0]
      cy = p[1] + pbc[kp][1]
      tmp.append([cx,cy])
     p1 = Polygon(tmp)
     if p1.intersects(frame): 
      final.append(tmp)


  return np.array(frame_tmp),np.array(final)
  

