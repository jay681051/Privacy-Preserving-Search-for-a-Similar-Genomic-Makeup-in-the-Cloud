def read(filePath, fileName):
  vectorizer = CountVectorizer()
  analyse = vectorizer.build_analyzer()
  with open(filePath+fileName, 'r') as fileContent:
    content=fileContent.read()
    words = analyse(content)
  return words


def phenotypeDataGen(filePath, words):
  dic=defaultdict(list)
  files = fnmatch.filter(os.listdir(filePath), '*.csv')
  for fileName in files:
    wordFromOneFile = read(fileName)
    commonwords = set(wordFromOneFile) & set(words)
    for word in commonwords:
      dic[word].append(fileName)
  sum=0
  for item in dic:
     sum+=len(dic.get(item))
  avg = sum/len(dic)

  newdic=defaultdict(list)
  
  for item in dic:
    if (len(dic.get(item))> avg+25) & (len(item) > 5) & (len(item)< 20):
      newdic[item] = list(dic[item])
  documents = dict()
  count=0
  for item in newdic.keys():
    l = newdic[item]
    for v in l:
      if (v not in documents.keys()) & (count < 1052):
        documents[v]=count
        count += 1

  matrix=np.zeros((1052, 1052))
  row=-1
  col=-1
  for w in newdic:
    row+=1
    files = newdic.get(w)
    for f in files:
      if f in documents.keys():
        col=documents[f]
        matrix[row, col]=1

  np.save("newdic", newdic)
  np.save("documents", documents)
  np.save("matrix", matrix)

