#


for path in Data/Beatmaps/* ;do
    name=$(ls "$path"/*.osu | head -n 1)
    mp3name=$(python scripts/audioname.py "$name")
    mp3path="$path/$mp3name"
    echo "$mp3path"
done
