# rag-admin

**rag-admin** is an administrative CLI for managing a Retrieval-Augmented Generation (RAG) knowledge base.

It is designed for **operators and platform teams**, not end users.
The tool is **configuration-driven** and intentionally minimal.

---

## Core Principle

> **The configuration is the system.**

All behavior of the RAG ingestion and maintenance process is defined in a single declarative configuration file.

There is only one user-facing command:

```bash
rag-admin config