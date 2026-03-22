# Transition Strategy

## Current State

Network builds rely on construction documents (often Word-based) interpreted by engineers during staging.

## Challenge

- interpretation varies between engineers
- manual steps introduce inconsistency
- difficult to automate reliably
- limited visibility into errors before shipment

## Approach

This model does not replace the current process immediately.

Instead, it introduces a parallel structured workflow.

---

## Phase 1 — Augment

- Continue using existing construction documents
- Extract key fields into structured input (JSON or similar)
- Use structured input to populate Source of Truth (NetBox)
- Generate configurations in parallel with current process

Goal:
Validate approach without disruption

---

## Phase 2 — Reduce Interpretation

- Engineers rely less on reading documents
- System-generated configs become primary reference
- Validation becomes standardized

Goal:
Reduce variation and rework

---

## Phase 3 — Shift Upstream

- Structured input replaces manual document interpretation
- Construction documents become output artifacts instead of inputs

Goal:
Fully standardized, automation-driven workflow

---

## Guiding Principle

Augment first. Replace later.

---

## Outcome

- smoother adoption
- reduced resistance
- measurable improvement without operational risk
