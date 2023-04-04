for i in $(cat < "inputs.txt")
do
curl -H "Content-Type: application/json" --request POST --data '{"teamname":"dark_army","password":"army7890", "plaintext":"'"$i"'"}' -k https://172.27.26.188:9000/eaeae >> outputs.txt
done
