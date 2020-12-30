# Key-Value-Data-Store
Language - Python 3.6.8<br>
<hr>
Features -><br>
  &nbsp;• A new key-value pair can be added to the data store using the create operation. The key is always a string capped at 32 chars. The value is always a JSON object capped at 16 KB.<br>
  &nbsp;• If <b>create</b> is invoked for an existing key, an appropriate error must be returned.<br>
  &nbsp;• A <b>read</b> operation on a key can be performed by providing the key and recieving the value in response, as a JSON object.<br>
  &nbsp;• A <b>delete</b> operation can be performed by providing the key.<br>
  &nbsp;• Every key supports setting a Time to live property [By default the TTL is 1 hour].<br>
  &nbsp;• The maximum size of the data store is 1 GB.<br>
  &nbsp;• The data store supprots multi threading and it is thread safe.<br>
  &nbsp;• As it is normal program which provides the data store, so it can accessed by only one client.<br>
