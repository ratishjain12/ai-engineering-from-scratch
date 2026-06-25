## Generators

A generator function is a special type of function that returns an iterator object

Instead of using return to send back a single value, generator functions use yield to produce a series of results over time

The function pauses its execution after yield, maintaining its state between iterations.

```python
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)

# output
1
2
3
4
5
```

useful for memory efficiency, streaming data, and clean stateful iteration.

### use cases

#### Streaming LLM output

- token/chunk streaming to frontend
- SSE/WebSocket streaming

#### File processing pipelines

- huge CSV/JSONL/log files
- OCR/doc extraction pipelines

#### Batch processing jobs

- moderation pipeline
- transcript processing
- log analytics
- retry queues
