# LMAB1
Code repository of shared methods for LMAB1 F2021.

## Existing routines

### montage.py
Create a montage give an image directory. Default row and column number are both set to 5 (= 25 fields); single component image size to 1104 (adjusted to the images provided in the class).
#### Usage
```bash
python3 montage.py WELL CHANNEL

# WELL is the name of the image directory, which is also the well ID; e.g. B02
# CHANNEL is the channel the montage will be performed on.
# 0 = Hoechst, 1 = Brightfield, 2 = PI, 3 = Composite of 0+2
```
#### Note
 - montage_CT1_B11_out contains sample output from Group 1 B11. You can obtain the same result by downloading Group 1 B11 image directory from box and run
 ```bash
 python3 montage.py B11 0
 python3 montage.py B11 2
 python3 montage.py B11 3
 ```
 for desired channel(s).
 - The output image is saved as "WELLdCHANNEL.png" (e.g. B02d2.png is the channel 2/PI montage of B02).
 - Image output for single channel is grayscaled and is RGB (PI-R, Hoechst-B). *The double channel ouptut is still a bit janky, so be doublecheck the result and see if it makes sense.*
 - This tool is meant for a quick visualization. Therefore,brightness normalization **is not implemented** across wells. You can try and implement it for your own use (or maybe share it by making a pull-request)!

