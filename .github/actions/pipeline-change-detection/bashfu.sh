[[ -z "$1" ]] && { echo "Parameter 1 is empty" ; exit 1; }
DIR="$1"
git diff --name-only HEAD HEAD~1 | awk -F/ '{print FS $1}' | grep -q -w $DIR && echo True || echo False