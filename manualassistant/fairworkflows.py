from fairworkflows import FairStep

STEP_URI = 'http://purl.org/np/RALgfqDcbpRvQ9HWXnPPtTzqeNvFBdBc7p4ZcbxqEg0fs#step'


def get_manual_step(uri):
    step = FairStep.from_nanopub(STEP_URI, use_test_server=True)
    step.validate()

    assert step.is_manual_task, 'Step is not a manual task!'
    return step
