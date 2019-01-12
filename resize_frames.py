import os

inpath = "./Inception/my_video_scenes"
outpath = "./Inception/resized"

# inpath = "./flickr"
# outpath = "./flickr_resized"

# inpath = "./paprika"
# outpath = "./paprika_resized"

os.system("mkdir " + outpath)

frame_list = sorted(os.listdir(inpath))
# length = int(frame_list[-1][-10:-7])
#
# for i in range(length):
#     os.system("ffmpeg -i " + inpath + "/" + frame_list[i] + " -vf scale=256:256 " + outpath + "/" + frame_list[i][-10:])

for frm in frame_list:
    os.system("ffmpeg -i " + inpath + "/" + frm + " -vf scale=256:256 " + outpath + "/_" + frm)


