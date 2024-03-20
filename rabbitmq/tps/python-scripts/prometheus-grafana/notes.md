### Activer les plugins

```shell
docker exec -it rabbitmq-2 rabbitmq-plugins list|grep prometheus
```

```shell
docker exec -it rabbitmq-2 rabbitmq-plugins enable rabbitmq_prometheus
```

### Test url metriques

```shell
curl 127.0.0.1:29591/metrics
``````
