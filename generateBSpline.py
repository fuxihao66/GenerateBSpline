import numpy as np
def Interpolate(p0, p1, a):
    return p0 * (1. - a) + p1 * a
vertexRange = 5.
segmentNum = 20
step = 0.1
strandNum = 100
startVertex = [ np.array([0., 0., -vertexRange], dtype=np.float32), 
                np.array([0., 0., -vertexRange], dtype=np.float32)]



guideCurveVertex = []
guideCurveVertex.append(startVertex[0])
for i in range(segmentNum):
    guideCurveVertex.append(Interpolate(startVertex[0], startVertex[1], (i+1.)/float(segmentNum))

totalCurveVertex = []
index = 0
for i in range(strandNum):
    for j in range(strandNum):
        totalCurveVertex.append(list())
        for j in range(segmentNum):
            totalCurveVertex[index].append(guideCurveVertex - np.array([step*i, step*j, 0.], dtype=np.float32)) 
        index += 1