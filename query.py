def single_posistion_query(k, pos):
 	alpha=int(hashlib.sha3(str(pos)+k).hexdigest(), 16) % (10 ** 8)
 	return alpha 


def construct_bf(size, err_rate, f):
	bf=pybloomfilter.BloomFilter(size, err_rate, f+".bloom")
        try:
            data =pd.read_table('/'.join([dir, f]), sep="\t", comment='#', header=None, low_memory=False, names=["sid", "chrom", "pos","gt"])
            sid=data['sid']
            gt=data['gt']
            for i in range(len(sid)):
                m=sid[i]+gt[i]
                bf.add(m)
        except Exception:
        	print("Error")
	