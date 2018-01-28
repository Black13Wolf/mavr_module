def obs_set():
    pass

def night():
    pass

def star():
    pass
    
def spool(main_path, output_dir, output_name=False, name='spool'):
    from os import walk, path
    from numpy import memmap, where

    if not output_name:
        output_name = path.basename(main_path)
    spools=[]
    for root, dirs, files in walk(path.join(main_path, name)):
        for d in dirs:
            if d.startswith('Spool'):
                spools.append(d)
    spool_num = 0
    for spool in spools:
        spool_num += 1
        files = list(walk(path.join(main_path, name, spool)))[0][2]
        for f in files:
            datfile = memmap(path.join(main_path, name, spool, f), dtype='uint16')
            if any(datfile == 0):
                for i in where(datfile == 0)[0]:
                    if datfile[i:i+10].sum()==0:
                        if i:
                            with open(path.join(output_dir, output_name+'.dat'), 'ab') as f:
                                f.write(datfile[:i])
                        break
                else:
                    with open(path.join(output_dir, output_name+'.dat'), 'ab') as f:
                        f.write(datfile)
            else:
                with open(path.join(output_dir, output_name+'.dat'), 'ab') as f:
                    f.write(datfile)
        
def tif_serie(self):
    pass

def tif_big(self):
    pass