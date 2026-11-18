# security-tools

> A personal collection of lightweight offensive security scripts for scanning, enumeration, exploitation, web testing, password attacks, and privilege escalation.

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.x-brightgreen)
![Status](https://img.shields.io/badge/status-active-success)
![Category](https://img.shields.io/badge/category-offensive--security-red)

---

## ⚠️ Legal Disclaimer

These tools are provided **for educational purposes and authorized security testing only**. Use them exclusively on systems you own or have **explicit written permission** to test (e.g. CTF labs, TryHackMe, HackTheBox, your own infrastructure). Unauthorized use against systems you do not control is illegal and may violate computer-misuse laws. The author assumes **no liability** for any misuse or damage caused by these tools.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Tools](#tools)
  - [JWT Generator](#jwt-generator)
- [Requirements](#requirements)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

`security-tools` is a growing toolbox of small, focused scripts built while working through penetration-testing labs and CTF challenges. Each tool is intentionally minimal and single-purpose, making it easy to read, adapt, and drop into a wider workflow.

Planned coverage spans the common phases of an engagement:

| Phase | Purpose |
| --- | --- |
| Scanning | Host and service discovery |
| Enumeration | Extracting detail from exposed services |
| Web | Web-application testing helpers |
| Exploits | Proof-of-concept exploitation scripts |
| Password Attacks | Credential and token manipulation |
| Privilege Escalation | Local privilege-escalation helpers |

---

## Repository Structure

```
security-tools/
├── web/                    
│   └── JWT/
│       └── JWTGenerate.py
├── LICENSE
└── README.md
```

> The structure grows as new tools are added. Each top-level directory maps to a testing phase or target class.

---

## Tools

### JWT Generator

`web/JWT/JWTGenerate.py`

An interactive helper for inspecting and forging **JSON Web Tokens** during web-application authentication testing. Useful when a known or guessed signing secret allows a token to be re-signed with attacker-controlled claims.

**What it does**

- Decodes the header and payload of an existing token **without** signature verification, so you can inspect its structure.
- Re-signs a new payload (default: an `admin` claim) using a supplied `HS256` secret.
- Verifies the freshly minted token against that secret and prints a ready-to-use `Authorization: Bearer` header.

**Usage**

```bash
pip install pyjwt
python3 web/JWT/JWTGenerate.py
```

You will be prompted for the original token and the signing secret. Edit the `new_payload` dictionary in the script to control the claims you want to inject.

**Example scenario** an application signs tokens with a weak/leaked `HS256` secret. Decode the original token to learn the claim names, then re sign a payload with elevated privileges to test for broken access control.

---

## Requirements

- Python 3.x
- [`PyJWT`](https://pyjwt.readthedocs.io/) (for the JWT tool)

Install per-tool dependencies as needed:

```bash
pip install pyjwt
```

---

## Roadmap

- [ ] Add scanning / enumeration helpers
- [ ] Add privilege-escalation scripts
- [ ] Add a `requirements.txt` per tool category
- [ ] Add usage examples and sample output for each tool

---

## Contributing

This is primarily a personal lab repository, but suggestions and improvements are welcome. Open an issue or submit a pull request.

---

## License

Distributed under the [MIT License](LICENSE). © 2026 AlkhHady.
