code="$(cat code.txt)"

for i in $(seq 16); do
    code="$(echo "$code" | base64 --decode)"
done

echo "$code" | uudecode -o /dev/stdout
