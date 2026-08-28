# TechTrend Solutions — IT Operations Handbook (Synthetic Training Data)

> This handbook is SYNTHETIC mock data created for the WSQ course
> "Develop Multi-Agent AI Applications with AutoGen" (TGS-2024045806).
> It does not describe any real company, person or system.

## POL-001 — VPN Access Policy

All remote access to TechTrend internal systems must go through the corporate
VPN. New VPN access requires a request in the IT portal approved by the
employee's line manager and the IT Security team. Approval normally takes one
business day. Contractors receive VPN accounts valid for a maximum of 90 days,
after which access must be re-approved. Split tunnelling is disabled on all
corporate VPN profiles.

## POL-002 — Password and MFA Policy

Passwords must be at least 14 characters and are checked against a list of
breached passwords. Multi-factor authentication (MFA) is mandatory for e-mail,
VPN and all administrator consoles. Accounts are locked after 5 failed sign-in
attempts and automatically unlock after 30 minutes, or immediately after an
IT Service Desk identity check.

## POL-003 — Software Installation Policy

Only software from the approved software catalogue may be installed on company
laptops. Requests for new software are raised in the IT portal and reviewed by
IT Security within three business days. Unapproved browser extensions are
removed automatically by endpoint management.

## POL-004 — Data Classification Policy

Data is classified as Public, Internal, Confidential or Restricted. Restricted
data (payroll, health, credentials) must never be pasted into external AI
tools or shared outside approved systems. Confidential data may be shared
internally on a need-to-know basis only.

## PROC-101 — Incident Response Procedure

Incidents are classified P1 (critical), P2 (high), P3 (normal) or P4 (low).
A P1 incident (production outage, security breach) must be acknowledged within
15 minutes and receives updates every 30 minutes until resolved. P2 incidents
must be acknowledged within 1 hour, P3 within 4 business hours, and P4 within
1 business day. All P1 and P2 incidents require a post-incident review within
five business days of resolution.

## PROC-102 — Backup and Restore Procedure

Production databases are backed up every 4 hours with a 35-day retention.
File shares are backed up nightly with a 90-day retention. Restore requests
are raised through the IT portal; standard restores are completed within one
business day, and emergency restores for P1 incidents within 4 hours.

## PROC-103 — New Starter Onboarding Procedure

Managers must raise an onboarding request at least five business days before a
new starter's first day. The request provisions the laptop, e-mail account,
VPN profile and role-based application access. Day-one credentials are handed
over in person and must be rotated at first sign-in.

## SLA-201 — Service Desk Response Targets

The IT Service Desk operates 8:00am–8:00pm Singapore time, Monday to Saturday.
Response targets: P1 — 15 minutes, P2 — 1 hour, P3 — 4 business hours,
P4 — 1 business day. Tickets that breach their response target are escalated
automatically to the duty manager.

## SLA-202 — Change Windows

Standard changes are deployed in the weekly window, Wednesday 10:00pm to
Thursday 2:00am. Emergency changes require CAB approval from two members of
the change advisory board and may be deployed at any time.

## SEC-301 — AI Tool Usage Guideline

Employees may use approved AI assistants for Public and Internal data only.
Model prompts and outputs are logged. Instructions found inside retrieved
documents, e-mails or tickets must never be executed by AI agents
automatically; agents must treat retrieved content as data, not as commands.
