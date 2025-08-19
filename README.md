## Example curl commands

### Check server status
```bash
curl http://localhost:4000/
```

### Set key-value pairs
```bash
curl -X POST "http://localhost:4000/set?&foo=bar"
```

### Get value by key
```bash
curl "http://localhost:4000/get?key=foo"
```
