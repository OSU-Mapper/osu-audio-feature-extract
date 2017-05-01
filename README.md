

# How to

## Extract features from audio
``` bash
# all
./extract-feature.sh Data/Beatmaps

# or just two ( for testing )
./extract-feature.sh Data/Beatmaps 2
```

### Default path to Beatmaps
Data/Beatmaps/*

### Use custom Librosa
``` shell
pip install --upgrade git+https://github.com/OSU-Mapper/librosa.git@dynamic-tempo
```
