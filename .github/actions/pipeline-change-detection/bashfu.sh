[[ -z "$1" ]] && { echo "Parameter 1 is empty" ; exit 1; }
DIR="$1"
git diff --name-only ${GITHUB_REF_NAME}... | awk -F/ '{print FS $1}' | grep -q -w $DIR && echo true || echo false