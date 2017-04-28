#

if ! [ "$#" -eq 1 ] || ! [ -d "$1" ]; then
  echo "Usage: $0 DIRECTORY" >&2
  exit 1
fi

if [ "$#" -eq 2 ]; then
    echo "Using maximum: $1 (for test)"
    count=$1
fi 

for path in $0 ;do
    name=$(ls "$path"/*.osu | head -n 1)
    mp3name=$(python script/audioname.py "$name")
    mp3path="$path/$mp3name"
    echo ">>> Extracting: $mp3path"
    python audiobeat
done
