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
        
def serie_tif(path_to_dir, output_dir):
    from PIL import Image
    from numpy import array, uint16
    from os import walk, path
    output_name = path.basename(path_to_dir)+'.dat'
    files = list(walk(path_to_dir))[0][2]
    for f in files:
        if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png') or f.endswith('.tif') or f.endswith('.gif'):
            img_path = path.join(path_to_dir, f)
            img = Image.open(img_path).convert('I')
            img = array(img).astype('uint16')
            with open(path.join(output_dir, output_name), 'ab') as output:
                output.write(img)

def big_tif(path_to_dir, output_dir):
    from PIL import Image
    from numpy import array, uint16
    from os import stat, path, walk
    output_name = path.basename(path_to_dir)
    serie = Image.open(path.join(path_to_dir,'spool.tif'))
    output_name = path.basename(path_to_dir)
    tiffs = list(walk(path_to_dir))[0][2]
    if stat(path.join(path_to_dir, 'spool.tif')).st_size == 8:
        print('{}: Ошибка в директории. Пересоберите вручную.'.format(main_path))
    elif len(tiffs) == 1:
        serie = Image.open(path.join(path_to_dir, 'spool.tif'))
        frames = serie.n_frames
        for i in range(frames):
            serie.seek(i)
            with open(path.join(output_dir, output_name+'.dat'), 'ab') as output:
                output.write(array(serie).astype('uint16'))
    else:
        for f in tiffs:
            if stat(path.join(path_to_dir, f)).st_size == 8:
                continue
            else:
                serie = Image.open(path.join(path_to_dir, f))
                frames = serie.n_frames
                for i in range(frames):
                    serie.seek(i)
                    with open(path.join(output_dir, output_name+'.dat'), 'ab') as output:
                        output.write(array(serie).astype('uint16'))