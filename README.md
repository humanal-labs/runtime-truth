# Runtime Truth

**Don’t trust the tool response. Verify the state.**

Runtime Truth is a small WebMCP experiment for detecting a simple but important failure mode in agentic systems:

> A tool reports that an action succeeded, but the authoritative application state says otherwise.

## The Problem

As AI agents move from reading websites to taking real actions — booking, buying, submitting, requesting, changing state — a successful tool response is not always enough.

The agent may receive:

`SUCCESS`

while the underlying application state contains no corresponding result.

This creates an execution-state divergence:

**Declared execution state ≠ actual runtime state**

## Demo

Runtime Truth exposes a WebMCP tool:

`reserve_table`

The tool receives:

- `party_size`
- `time`

In the demo, the reservation endpoint deliberately reports success:

`Reservation ID: R-1042`

But the reservation is not persisted.

Runtime Truth then performs an independent check against the authoritative application state.

Result:

**Declared Result:** SUCCESS  
**Actual State:** RESERVATION NOT FOUND  
**Verification:** DIVERGENCE DETECTED

## How It Works

1. An agent calls the WebMCP tool.
2. The application performs the requested action.
3. The tool receives a declared result.
4. Runtime Truth independently checks the authoritative post-action state.
5. The declared result and observed state are compared.
6. A mismatch is surfaced as execution-state divergence.

The important part is that verification does not simply trust the tool response that produced the action.

## Why WebMCP?

WebMCP gives websites a structured way to expose actions directly to agents.

That makes agent interaction more reliable than depending entirely on visual navigation and UI automation.

But once agents can perform meaningful actions, another question becomes important:

**Did the action actually happen?**

Runtime Truth explores that question at the point immediately after execution.

## Independent Market Signal

The broader WebMCP conversation is beginning to surface the same reliability problem.

Greg Isenberg recently described an **“agent mystery shopper”** concept: testing whether agents can actually complete important website journeys such as purchases, bookings, and submissions.

Runtime Truth focuses on a narrower technical version of that problem:

> When an agent or tool declares success, verify that the expected state transition actually occurred.

This project was developed independently; the discussion is included as an external signal that agent completion verification may become increasingly important as agents perform real transactions on the web.

## Current Scope

Runtime Truth is intentionally minimal.

It does not attempt to solve every form of agent reliability or observability.

The current experiment tests one specific hypothesis:

> Independent post-action state verification can detect cases where declared tool success does not match authoritative runtime state.

## Built With

- WebMCP
- Python
- Flask
- JavaScript
- Render

## Live Demo

https://runtime-truth.onrender.com

## Core Principle

**Don’t trust the tool response. Verify the state.**
