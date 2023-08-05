# andrew-model
A sound-object labelling machine learning model for use as an [Audacity](audacity) script. Uses [VGGish](vggish) for feature extraction and a [Pytorch](pytorch) N-way classifier neural network for training.

This work is part of the [Eyes-Free Audio](eyes-free-audio) project between the [Interactive Audio Lab](audio-lab) and the [Inclusive Technology Lab](inclusive-tech-lab) at Northwestern University and is supported by NSF Award 1901456.

## Setup
- Run `pip3 install -r requirements.txt`.
- Download `vggish_model.ckpt` and `vggish_pca_params.npz` and place them in the `vggish` directory.
- Add any WAV files you want to use into `data/audio/`.

## Training
- Run `python3 src/model/train.py` for basic training on the FreeSound database.
- Run `python3 src/model/train.py FILE_PATH.csv` to specify a metadata file for training.
- Pytorch model files will be saved in `data/models` by default.

## Use with Audacity
- Save the Audacity file you're working with in the `data/audacity` folder.
- Select the track you want to label in Audacity.
- Run `python3 src/app.py`.
- In the pop-up window, select `labels.txt`.

## Use as a Package
- Run `sudo pip3 install andrewAudio`.
- `from andrewAudio import predict`.
- 

## Testing
- Tests can be found in the `test` directory.

[andrew-vst]: https://github.com/andrew-vst/andrew-plugin
[audacity]: https://www.audacityteam.org
[audio-lab]: http://music.cs.northwestern.edu
[eyes-free-audio]: https://interactiveaudiolab.github.io/project/eyes-free-interfaces.html
[inclusive-tech-lab]: https://inclusive.soc.northwestern.edu
[pytorch]: https://pytorch.org
[vggish]: https://github.com/tensorflow/models/tree/master/research/audioset
