import pybloomfilter
import os
import allel
def readData(dir):
    fs=os.listdir(dir)

    for f in fs:
        bf=tbf.copy_template(outdir+f+".bloom")
        try:
            input=''.join([dir, f])
            callset=allel.read_vcf(input, fields=['variants/CHROM','variants/POS', 'calldata/GT'], types={'calldata/GT':'i2'},
                                           fills={'calldata/GT':2})
            chrom=callset['variants/CHROM']
            pos=callset['variants/POS']
            gt=allel.GenotypeArray(callset['calldata/GT'])
            for i in range(len(chrom)):
                position='|'.join([chrom[i], str(pos[i])])
                gv=allel.GenotypeVector(gt[i])
                key1=0
                key2=0
                if gv[0][0] ==0|gv[0][0] ==1|gv[0][0] ==2 :
                    key1=gv[0][0]
                print("key1:"+str(key1))
                if gv[0][1] ==0|gv[0][1] ==1|gv[0][1] ==2:
                    key2=gv[0][1]
                sum=key1|key2
                key='|'.join([position, str(sum)])
                bf.add(key)
        except Exception as err:
            print(f)
            print(err)
        bf.close()


