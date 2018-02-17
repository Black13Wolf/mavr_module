def get_ps(path_to_dat, diff=0, acf=False, save=False, shape=(512,512), output=False, rmbgr_on=True):
    from numpy import memmap, zeros, fft, any
    from os.path import basename, join
    if output:
        output_file = join(output, basename(path_to_dat))
    else:
        output_file = path_to_dat
    serie = memmap(path_to_dat, dtype='uint16').astype('float32')
    frames = int(serie.size/512/512)
    serie = serie.reshape((frames, 512, 512))
    output_ps = zeros(shape)
    for num in range(frames):
        frame = zeros(shape)
        if diff and num<frames-diff:
            frame[:512, :512] += serie[num] - serie[num+diff]
        else:
            frame[:512, :512] += serie[num]
        output_ps += abs(fft.fft2(frame)**2)                                                                                                                                                                                                                                                                                                                                                                                            
    output_ps /= frames  
    if rmbgr_on: output_ps = rmbgr(fft.fftshift(output_ps), 100)
    #output_ps[500:524, 500:524] = 0 Устранение центрального пика СПМ. Сделать сглаживание в будущем.
    output_ps = fft.fftshift(output_ps)
          
    if acf: output_acf = abs(fft.ifft2(fft.fftshift(output_ps)))
    if save:
        if save == 'fits':
            from astropy.io import fits
            fits.writeto(output_file+'_ps_diff{}_shape{}.{}'.format(diff, shape, save), fft.fftshift(output_ps))
            if acf: fits.writeto(output_file+'_acf_diff{}_shape{}.{}'.format(diff, shape, save), fft.fftshift(output_acf))
        else:
            print('Unknown format: {}'.format(save))
    else:
        if acf:
            return fft.fftshift(output_ps), fft.fftshift(output_acf)
        else:
            return fft.fftshift(output_ps)
    
def rmbgr(middle_star, xlim): 
    from numpy import mean
    outbound = middle_star[0:xlim] 
    slice_out = mean(outbound, axis=0) 
    middle_star_clean = middle_star - slice_out 
    return middle_star_clean 

def partickle_searcher(frame):
    '''
        Функция будет анализировать кадр (или серию кадров) на поиск перекопов или частиц и выдавать номера кадров, допущенные к расчетам.
        не более 50 кадров можно выкинуть из серии 2000 кадров. То есть не более %2.5 от общего количества кадров в серии.
    '''
    pass