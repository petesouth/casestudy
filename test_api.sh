curl \
 --header "Content-Type:application/json" \
 --header "Accept: application/json" \
 --request POST \
 --data '{"number": 66666}' \
 http://192.168.1.234:8080/api/v2/num_to_english/



curl \
http://192.168.1.234:8080/api/v2/num_to_english/?number=66666