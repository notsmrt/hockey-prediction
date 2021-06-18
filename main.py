#hockey framework
rw = 3
rl = -3
w = 4
l = -3
from NBAGameSimulator import *
import numpy as np
gsw = Team('toronto',[2,5,2,4,3,3,rl,l],[2,1,1,0,4,3,rw,w])
cle = Team('montreal',[2,1,1,0,4,3,rw,w],[2,5,2,4,3,3,rl,l])
msim = MatchupSimulator(gsw,cle)
msim.gamesSim(100000)
#basketball framework
rw = 15
rl = -15
w = 40
l = -30
from NBAGameSimulator import *
import numpy as np
gsw = Team('trail blazers',[133,130,128,129,114,rl],[96,104,93,107,118,rl])
cle = Team('cavaliers',[96,104,93,107,118,rl],[133,130,128,129,114,rl])
msim = MatchupSimulator(gsw,cle)
msim.gamesSim(100000)
