import numpy as np
from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
global group


def init():
  group = PairingGroup('SS512')
  g=group.random(G1)
  h=group.random(ZR)
  gh=g**h
  p=group.order()
  pp=[g, h, gh, p]

  sg=group.serialize(g)
  sh=group.serialize(h)
  sgh = group.serialize(gh)
  pp = [sg, sh, sgh, p]
  np.save("groupParameter", pp)
  return pp


def readPrimitives():
  groupParameter = np.load("groupParameter.npy")
  sg = group.deserialize(groupParameter[0])
  sh = group.deserialize(groupParameter[1])
  sgh = group.deserialize(groupParameter[2])
  p = long(groupParameter[3])
  pp = [sg, sh, sgh, p]
  return pp

 