# Drinks-API
>3000 alcoholic drinks api

For a random drink (note use batch rquest for large requests)
https://lg3gc7zrov3dqe5jsui4xuvgqe0lrujz.lambda-url.eu-west-1.on.aws/?drink=RANDOM


base_url = "https://lg3gc7zrov3dqe5jsui4xuvgqe0lrujz.lambda-url.eu-west-1.on.aws/?"

<strong>Commands:</strong>

Returns all the drinks

<code> base_url+"drink=ALL"</code>

Returns a random drink

<code>base_url+"drink=RANDOM"</code>

Returns a specific drink or empty array if non exists

<code>base_url+"drink=<<DRINK>>"</code>


<strong>Batch request:</strong>

<code>base_url+"drink=[<<DRINK>>,<<DRINK>>,...,<<DRINK>>]"</code>

---

<h2>NEW FEATURES</h2>

<strong>Random by type</strong>

<code>base_url+"drink=RANDOMTYPE(<<TYPE HERE>>)"</code>


<strong>See all types</strong>

<code>base_url+"drink=SEETYPES"</code>

---

**Please be courtious when using the api**
