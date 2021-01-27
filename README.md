# FAIR Manual Assistant

How to run
```python
import manual_assistant
import fairworkflows

EXAMPLE_STEP_URI = 'http://test-server.nanopubs.lod.labs.vu.nl/RAFszXfE-J3sef_ZX_5LRMM6rHgBt7a1uQH-vZdxfy-RU'
step = FairStep.from_nanopub(EXAMPLE_STEP_URI)


# A manual step will block the execution and point the user to a webinterface to perform the manual step. The 
# execution will be continued when the manual step has been performed successfully.
outputs = manual_assistant.execute_manual_step(step)

> INFO:root:Starting Manual Step Assistant
> INFO:root:Please go to http://localhost:8000 to perform the manual step
> 127.0.0.1 - - [27/Jan/2021 11:22:34] "GET / HTTP/1.1" 200 -


# `execute_manual_step` also accepts plain URIs pointing to nanopubs:
outputs = manual_assistant.execute_manual_step(EXAMPLE_STEP_URI)

```

![Example](example.png)
