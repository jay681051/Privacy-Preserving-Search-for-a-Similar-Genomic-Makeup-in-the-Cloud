def higherarchial_index_gen(bfpath, number_of_patients,  patients_snp_matrx, ):
  r=random.generation()
  tbf = pybloomfilter.BloomFilter.open(bfpath+"template.bloom")
  SNPs={}
  X = np.zeros([number_of_patients, 20101326], dtype=int)
  for i in range(number_of_patients):
    bf = tbf.copy_template(bfpath+str(i)+".bloom")
    SNPs[i]=patients_snp_matrx[i]
    for j in SNPs[i]:
      bf.add(j)
    bf.close()
    tmp = bitarray.bitarray()
    bf_new = tbf.copy_template(bfpath+str(i)+".bloom")
    with open(bfpath+str(i)+".bloom", 'rb') as fh:
      tmp.fromfile(fh)
      try:
        tmp=tmp[-20101326:]
        idx=tmp.index(1, 0, 20101326)
        while idx<20101326:
          alpha=prf(k+str(pos))
          alpha=prf(alpha+str(r))
          bf_new.add(alpha)
          idx = tmp.index(1, idx+1, 20101326)
      except:
          print("error in index generation ")
    bf_new.close()
    X[i]=bf_new.tobitarry()
  Z = hierarchy.linkage(X, method='ward', metric="euclidean", optimal_ordering=True )
  rootnode, nodelist =hierarchy.to_tree(Z,rd=True)
  return rootnode, nodelist

def search(rootnode, query, threshold)
rootnodes=[]
rootnodes.append(rootnode)
stach=[]
result=[]
for rootnode in rootnodes:
  stack.append(rootnode)
  while len(stack)>0:
    index= len(stack)
    tempnode = stack.pop(index-1)
    if not tempnode.is_leaf():
      left=tempnode.left
      right=tempnode.right
      id = left.id
      score=np.dot(query, patients[id])
      if score > threshold:
        stack.append(left)
      id = right.id
      score = np.dot(query, patients[id])
      if score > threshold:
        stack.append(right)
    else:
      result.append(tempnode.id)
return result 
