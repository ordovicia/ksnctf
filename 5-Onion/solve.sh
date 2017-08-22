code="$(cat code.txt)"

for i in $(seq 16); do
    code="$(echo "$code" | base64 -d)"
done

echo "$code" | uudecode -o /dev/stdout
