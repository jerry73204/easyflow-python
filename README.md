# easyflow for Python

It is Python binding of
[easyflow](https://github.com/jerry73204/easyflow) project, which
makes is easy to launch interconnected processes in one
`dataflow.json5` file.

## Installation

Install this package using pip.

```bash
pip install -U git+https://github.com/jerry73204/easyflow-python.git
```

## Usage

Here walks through the simple pub/sub example in the
[directory](example/pubsub).

On the publisher side, it creates a sender according to the dataflow file.

```python
flow = pyeasyflow.load_dataflow('dataflow.json5')
sender = flow.build_sender('publisher')
sender.send(b'DATA')
```

The subscriber side creates a listener from the same dataflow file.

```python
flow = pyeasyflow.load_dataflow('dataflow.json5')

def callback(payload):
    print(payload)
        
listener = flow.listen('subscriber', callback)
```

Launch two scripts simultaneously.

```bash
cd example/pubsub

parallel -j0 --tty <<EOF
./pub.py
./sub.py
EOF
```
