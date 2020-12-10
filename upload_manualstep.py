#! /usr/bin/env python3

from fairworkflows import FairStep
import rdflib

PPLAN = rdflib.Namespace('http://purl.org/net/p-plan#')


def main():
    # Make a new 'empty' step
    step = FairStep()

    # Specify various characteristics needed to describe it
    step.label = 'Taking pictures'
    step.description = 'Take a picture of the object'
    step.is_manual_task = True

    # Add other statements, about the step itself
    step.set_attribute(predicate=rdflib.URIRef('http://example.org/needsEquipment'),
                       value=rdflib.URIRef('http://example.org/photocamera'))

    # Set the URIs of the inputs and outputs to this step
    step.inputs = ['http://example.org/objecttype']
    step.outputs = ['http://example.org/photo']

    # Publish the step as a nanopublication for others to find
    result = step.publish_as_nanopub(use_test_server=True)

    print(result)


if __name__ == '__main__':
    main()
