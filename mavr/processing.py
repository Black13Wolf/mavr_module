def get_ps(path_to_dat, diff=0, showing=False):
    from numpy import memmap
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
    
def get_acf(path):
    pass