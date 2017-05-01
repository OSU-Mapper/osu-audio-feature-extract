#

version=1

if ([ "$#" -ne 1 ] && [ "$#" -ne 2 ] )|| ! [ -d "$1" ]; then
  echo "Usage: $0 DIRECTORY" >&2
  exit 1
fi

if [ "$#" -eq 2 ]; then
    echo "Using maximum: $2 (for test)"
    count=$2
fi 

mkdir -p "Data/Trainables" 

for path in $1/* ;do
    name=$(ls "$path"/*.osu | head -n 1)
    mp3name=$(python script/audioname.py "$name")
    mp3path="$path/$mp3name"
    echo ">>> Extracting: $mp3path"
    python script/audioquarter_segment.py "$mp3path" "$path/timing_points.v$version.csv" "$path/audio_features.v$version.csv"
    for osuPath in "$path"/*.osu; do
        osuDiff=$(python script/osuDiff.py "$osuPath")
        python script/timeToBeat.py "$osuPath" "$path/audio_features.v$version.csv" "$path/$osuDiff.trainable-features.v$version.csv" 
    done

    if [ "$#" -eq 2 ]; then
        count=$((count - 1))
        if (("$count" <= "0")) 
        then
            break;
        fi
    fi
done
