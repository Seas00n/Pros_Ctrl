from PIL import Image
import glob

gif_path = "/media/yuxuan/My Passport/testFootPlate/gif/"

fig_list = sorted(glob.glob(gif_path+"*.png"),key=lambda name:int(name[len(gif_path):-4]))

imageDim = []

for f in range(len(fig_list)):
    imageDim.append(Image.open(fig_list[f]))

duration = [20]*len(fig_list)
duration[-1] = 20

imageDim[0].save(gif_path+"1.gif",
                 save_all=True,
                 append_images=imageDim[1:],
                 duration=duration,
                 loop=False)
