# Workflow

## Objective

Convert customer orders into validated, ready to ship network infrastructure.

## End to End Flow

1. Order Intake  
2. Structured Input Creation  
3. Source of Truth Population (NetBox or equivalent)  
4. Configuration Generation  
5. Deployment (automation)  
6. QA Validation  
7. Ship  

---

## Step Breakdown

### 1. Order Intake
Customer demand enters the system (often unstructured).

### 2. Structured Input Creation
Key fields are normalized into a predictable format.

Example:
- customer
- site
- device profile
- platform

### 3. Source of Truth
Structured data is stored in a system like NetBox.

This defines:
- devices
- roles
- IP assignments
- platform

### 4. Configuration Generation
Configurations are generated from data using templates.

No manual typing of configs.

### 5. Deployment
Automation tools apply configurations to devices.

### 6. QA Validation
System level validation is performed:
- connectivity
- expected interfaces
- basic policy behavior

Results are captured for feedback.

### 7. Ship
Only validated kits move forward.

---

## Key Principle

Keep management access stable while validating service plane behavior.

---

## Outcome

- repeatable builds
- consistent configurations
- reduced rework
- measurable quality
