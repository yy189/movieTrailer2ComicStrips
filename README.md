Movie Trailers to Comic Strips of Specific Artistic Styles

Functions of the scripts:

pyscenedetect_command.md: use PySceneDetect to extract content-aware frames;

jpeg_res.py: pick the top 6153 photos from flickr30k dataset sorted by abs(width/height-1920/1080) value;

resize_frames.py: use FFmpeg to resize all input images to 256x256

train & test CartoonGAN or use a pretrained model to generate frames of specific artistic styles

img2comicstrips.py: lay out the result frames like in comic strips, insert subtitles at the right place and also page numbers.

Some results:
![paprika styled trailer of crazy on the outside](https://github.com/yy189/movieTrailers2ComicStrips/result_paprika.jpg)

![hayao styled trailer of inception](https://github.com/yy189/movieTrailers2ComicStrips/result_hayao.jpg)