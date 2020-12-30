# Key-Value-Data-Store
Language - Python 3.6.8

Features ->
  • A new key-value pair can be added to the data store using the create operation. The key is always a string capped at 32 chars. The value is always a JSON object capped at 16 KB.
  • If <b>create</b> is invoked for an existing key, an appropriate error must be returned.
  • A <b>read</b> operation on a key can be performed by providing the key and recieving the value in response, as a JSON object.
  • A <b>delete</b> operation can be performed by providing the key.
  • Every key supports setting a Time to live property [By default the TTL is 1 hour].
  • The maximum size of the data store is 1 GB.
  • The data store supprots multi threading and it is thread safe.
  • As it is normal program which provides the data store, so it can accessed by only one client.
