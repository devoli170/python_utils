[[ -z "$1" ]] && { echo "Parameter 1 is empty" ; exit 1; }
DIR="$1"
echo ${GITHUB_REF##*/}
git diff --name-only ${GITHUB_REF##*/}... | awk -F/ '{print FS $1}' | grep -q -w $DIR && echo true || echo false