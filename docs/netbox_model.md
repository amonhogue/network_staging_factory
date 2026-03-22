# NetBox Model

## Objective

Provide a consistent structure for managing multiple customers, sites, and device types within a single source of truth.

---

## Core Principle

Organize by tenant. Standardize by design.

---

## Tenant

Each customer environment is represented as a tenant.

Examples:
- Tenant_A
- Tenant_B
- Tenant_C

This creates clean separation between environments.

---

## Site

Each deployment location is modeled as a site.

Examples:
- SITE_1001
- SITE_1002

Each site represents:
- a branch
- a store
- a deployment location

---

## Device Roles (Reusable)

Roles are standardized across all tenants.

Examples:
- edge_firewall
- sdwan_edge
- access_switch
- core_switch
- access_point

These roles define function, not vendor.

---

## Platforms (Vendor / OS)

Platforms define the operating system.

Examples:
- junos
- ios_xe
- unifi

This allows multi-vendor support without changing the system.

---

## Device Types (Hardware)

Device types define specific models.

Examples:
- firewall_model_x
- switch_model_y
- access_point_model_z

---

## IPAM Strategy

IP space is segmented per tenant.

Example:

Tenant_A:
10.100.0.0/16
  → /24 per site

Tenant_B:
10.200.0.0/16

This ensures:
- no overlap
- clean allocation
- scalability

---

## Lifecycle Management

Devices and sites are not deleted after deployment.

Instead, they move through lifecycle states:

- planned
- staging
- active
- decommissioned

---

## Key Benefit

This structure allows:

- multiple tenants in one system
- consistent automation logic
- reusable templates across vendors
- scalable growth without redesign

---

## Summary

NetBox is not just inventory.

It is the structured system that defines what should exist, so automation can build it consistently.
