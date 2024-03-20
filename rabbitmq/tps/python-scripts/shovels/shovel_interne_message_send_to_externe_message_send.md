```shell
 rabbitmqadmin -u guest -p guest 
 declare parameter component=shovel name=shovel_interne_message_send_to_externe_message_send
 value='{
   "src-queue": "message.forward",
   "src-uri": ["amqp://"],
   "dest-uri": ["amqp://guest@guest@127.0.0.1:29572"],
   "dest-exchange": "message.forwarded"
 }'

```

```shell


rabbitmqctl set_policy
--vhost ddl
--priority 0
--apply-to queues
deadletter
"^((?!deadletter).).*"
'{
  "message-ttl": 2000,
  "overflow": "drop-head",
  "dead-letter-exchange": "deadletter.exchange",
  "dead-letter-routing-key": "*"
}'


```