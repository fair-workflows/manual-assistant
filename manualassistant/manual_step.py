from fairworkflows import FairStep


def get_manual_step(uri: str) -> FairStep:
    step = FairStep.from_nanopub(uri, use_test_server=True)

    assert step.is_manual_task, 'Step is not a manual task!'
    return step
