Drinks-API
3000 alcoholic drinks api

For a random drink (note use batch rquest for large requests) 
https://lg3gc7zrov3dqe5jsui4xuvgqe0lrujz.lambda-url.eu-west-1.on.aws/?drink=RANDOM

base_url = 
"https://lg3gc7zrov3dqe5jsui4xuvgqe0lrujz.lambda-url.eu-west-1.on.aws/?"

Commands:

Returns all the drinks

 base_url+"drink=ALL"

Returns a random drink

base_url+"drink=RANDOM"

Returns a specific drink or empty array if non exists

base_url+"drink=<>"

Batch request:

base_url+"drink=[<>,<>,...,<>]"

NEW FEATURES
Random by type

base_url+"drink=RANDOMTYPE(<>)"

See all types

base_url+"drink=SEETYPES"

Please be courtious when using the api
