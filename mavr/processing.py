def get_ps(path_to_dat, diff=0, acf=False, save=False, showing=False):
    from numpy import memmap, zeros, fft
    from os.path import basename
    serie = memmap(path_to_dat, dtype='uint16')
    frames = serie.size()/512/512
    serie = serie.reshape((frames, 512, 512))
    ps = zeros((512,512))
    for num in range(frames):
        if diff and num<frames-diff:
            ps += abs(fft.fft2(serie[i] - serie[i+diff]))
        else:
            ps += abs(fft.fft2(serie[i]))
    ps /= frames            
    if showing:
        from matplotlib.pyplot import imshow, show
        imshow(ps, cmap='gray')
        show()
    acf = abs(fft.ifft2(ps))
    if save:
        if save == 'fits':
            from astropy.io import fits
            fits.tofile(path_to_dat+'_ps.fits', ps)
            fits.tofile(path_to_dat+'_acf.fits', acf)
        else:
            print('Unknown format: {}'.format(save))
    else:
        return fft.fftshift(ps), fft.fftshift(acf)    