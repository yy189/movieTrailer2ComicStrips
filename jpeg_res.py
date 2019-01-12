import os
import shutil

TOTAL = 6153

def jpeg_res(filname):
    with open(filname, 'rb') as img_file:
        img_file.seek(163)
        a = img_file.read(2)
        height = (a[0] << 8) + a[1]
        a = img_file.read(2)
        width = (a[0] << 8) + a[1]
    return (width, height)

def main():
    s = set()
    img_res_list = []

    img_list = os.listdir("./flickr30k_images/flickr30k_images")
    for img in img_list:
        res = jpeg_res("./flickr30k_images/flickr30k_images/" + img)
        img_res_list.append((img, res))
        if res[1] >= 256 and res[0] >= 256 and res not in s:
            s.add(res)
    res_list= sorted(list(s), key=lambda tup: (tup[0]/tup[1]-1920/1080 > 0, abs(tup[0]/tup[1]-1920/1080)))
    print(res_list)

    os.system("mkdir ./flickr")

    count = 0
    for res in res_list:
        for (i, r) in img_res_list:
            if r == res:
                shutil.copy("./flickr30k_images/flickr30k_images/" + i, "./flickr/" + i)
                count += 1
                print(count)
                if count == TOTAL:
                    return


if __name__ == "__main__":
    main()