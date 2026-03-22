# Network Staging Factory

## Overview

This repository is a reference implementation for a scalable network staging and validation workflow.

The goal is to transform customer demand into standardized, repeatable, and validated network builds with minimal variation and measurable quality.

## Why This Matters

Traditional network staging often depends on manual interpretation, inconsistent documentation, and engineer specific decision making. That creates variation, rework, and operational risk.

This project models a better path:

- structured intake
- source of truth
- repeatable build workflows
- automated configuration generation
- measurable QA feedback loops

## Core Workflow

Order -> Structured Input -> Source of Truth -> Build -> Validate -> Ship

## Architectural Themes

- NetBox or equivalent as source of truth
- Python and templates for deterministic config generation
- Ansible as deployment and execution layer
- PyEZ for Juniper native, transactional device interaction
- separate management and service plane thinking
- QA results captured for feedback and leadership visibility
- AI as an assistive layer, not the primary control plane

## Execution Model

Configuration can be applied using multiple approaches depending on the use case:

- Ansible for standardized, repeatable workflows across devices
- PyEZ for Juniper environments where commit check, rollback, and transactional safety are required

This allows the system to balance consistency with vendor specific control where needed.

## Lean Orientation

This model is intentionally shaped by lean thinking:

- reduce variation
- eliminate non value added work
- standardize build processes
- tighten feedback loops
- improve flow and quality over time

## Transition Mindset

This is not intended to replace an existing build process overnight. It is designed to run in parallel with current documentation driven workflows and gradually reduce manual interpretation over time.

## Relation to Existing Work

This repository builds on concepts demonstrated in other repos:

- intent-packs for intent driven configuration concepts
- config-drift-detector for validation and drift analysis concepts

Those repos show component ideas. This repo shows how they can fit into a production staging system.

## Status

Working reference model and proof of concept under active development.

## Working Demo

This repo includes a simple working proof of concept:

1. Model a device in NetBox
2. Pull device data through the NetBox API
3. Render a configuration from a Jinja template
4. Output a deterministic config artifact

### Example

python scripts/generate_config.py lab-ex-01
cat generated-configs/lab-ex-01.conf

### Additional Execution Examples

PyEZ deploy example:

python scripts/deploy_config_pyez.py

PyEZ commit check example:

python scripts/pyez_commit_check.py

PyEZ config load pattern:

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

with Device(host="192.168.100.3", user="lab", passwd="lab") as dev:
    cu = Config(dev)
    cu.load(path="generated-configs/lab-ex-01.conf", format="text", merge=True)
    cu.commit_check()

### Sample Files

- examples/sample_order.json
- examples/sample_generated_config.conf

This is intentionally lightweight. The goal is to demonstrate flow and repeatability, not a full production implementation.
