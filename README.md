# 2026 Open-Weight LLM VRAM, DeepSeek R1 MoE/MLA, Post-Quantum TLS 1.3 & Applied Security Benchmarks

**Maintained by [Kshitij Gupta](https://www.linkedin.com/in/kshitij-gupta-855535134/) at [The Infosiast](https://theinfosiast.com/)**

[![Interactive Tools Hub](https://img.shields.io/badge/18_Interactive_Labs-theinfosiast.com%2Ftools%2F-d72924?style=for-the-badge)](https://theinfosiast.com/tools/)
[![Open LLM VRAM Notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/theinfosiast-cloud-developer/llm-vram-pqc-security-benchmarks/blob/main/notebooks/ti_llm_vram_quantization_benchmark.ipynb)
[![Open DeepSeek R1 MLA Simulator in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/theinfosiast-cloud-developer/llm-vram-pqc-security-benchmarks/blob/main/notebooks/ti_deepseek_r1_moe_mla_kv_cache_simulator.ipynb)
[![Open NIST PQC TLS 1.3 Benchmark in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/theinfosiast-cloud-developer/llm-vram-pqc-security-benchmarks/blob/main/notebooks/ti_pqc_ml_kem_tls_benchmark.ipynb)

This repository houses the reproducible **Jupyter / Google Colab benchmark notebooks (`.ipynb`)**, **standalone Python CLI utilities (`cli/`)**, **empirical CSV datasets (`datasets/`)**, and direct deep-links to all **18 zero-dependency interactive engineering & security calculators** published on **[The Infosiast](https://theinfosiast.com/tools/)**.

---

## 1. Run Benchmarks Instantly in Google Colab

| Benchmark Notebook (`.ipynb`) | One-Click Google Colab Runner | Companion Technical Deep-Dive |
| :--- | :--- | :--- |
| **`notebooks/ti_llm_vram_quantization_benchmark.ipynb`** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/theinfosiast-cloud-developer/llm-vram-pqc-security-benchmarks/blob/main/notebooks/ti_llm_vram_quantization_benchmark.ipynb) | [Running Local LLMs on Consumer Hardware in 2026](https://theinfosiast.com/running-local-llms-consumer-hardware-2026/#ti-vram-calculator) |
| **`notebooks/ti_deepseek_r1_moe_mla_kv_cache_simulator.ipynb`** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/theinfosiast-cloud-developer/llm-vram-pqc-security-benchmarks/blob/main/notebooks/ti_deepseek_r1_moe_mla_kv_cache_simulator.ipynb) | [DeepSeek R1 Architecture & Deployment Guide](https://theinfosiast.com/deepseek-r1-architecture-deployment-guide/#ti-moe-calculator) |
| **`notebooks/ti_pqc_ml_kem_tls_benchmark.ipynb`** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/theinfosiast-cloud-developer/llm-vram-pqc-security-benchmarks/blob/main/notebooks/ti_pqc_ml_kem_tls_benchmark.ipynb) | [Post-Quantum Cryptography & Zero-Trust Migration Blueprint](https://theinfosiast.com/post-quantum-cryptography-zero-trust-migration-blueprint/#ti-pqc-simulator) |
| **`notebooks/ti_ml_precision_recall_benchmark.ipynb`** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/theinfosiast-cloud-developer/llm-vram-pqc-security-benchmarks/blob/main/notebooks/ti_ml_precision_recall_benchmark.ipynb) | [Precision and Recall in Machine Learning: The Definitive Guide](https://theinfosiast.com/precision-and-recall-in-machine-learning-the-definitive-guide/#ti-pr-simulator) |

---

## 2. All 18 Live Interactive Browser Calculators & Security Labs

| # | Interactive Engineering / Security Lab | Live Browser Tool URL | Primary Standards & Scope |
| :- | :--- | :--- | :--- |
| 1 | **Local LLM VRAM, KV-Cache & Token Speed Calculator** | **[Launch Calculator](https://theinfosiast.com/running-local-llms-consumer-hardware-2026/#ti-vram-calculator)** | Weights + GQA/MLA KV-Cache + Activation Buffer (`FP16`, `Q8_0`, `Q5_K_M`, `Q4_K_M`, `IQ3_M`) |
| 2 | **DeepSeek R1 Ollama GPU Sizer & CLI Generator (`1.5B–671B`)** | **[Launch Ollama Sizer](https://theinfosiast.com/run-deepseek-r1-locally-ollama-hardware-requirements/#ti-deepseek-sizer)** | Exact `ollama run deepseek-r1:<tag>` + `OLLAMA_FLASH_attention=1` & `num_ctx` sizing |
| 3 | **DeepSeek R1 MoE Active-Parameter & MLA KV-Cache Simulator** | **[Launch MoE Simulator](https://theinfosiast.com/deepseek-r1-architecture-deployment-guide/#ti-moe-calculator)** | 671B total vs. 37B active MoE routing & Multi-Head Latent Attention KV-cache compression |
| 4 | **Post-Quantum TLS 1.3 Wire-Size & MTU Simulator** | **[Launch PQC Lab](https://theinfosiast.com/post-quantum-cryptography-zero-trust-migration-blueprint/#ti-pqc-simulator)** | NIST FIPS 203 (`X25519MLKEM768`), FIPS 204 (`ML-DSA-65`), FIPS 205 (`SLH-DSA`), 1460B TCP MSS |
| 5 | **Passkey Hardware Enclave & AitM Phishing Simulator** | **[Launch Passkey Lab](https://theinfosiast.com/passkeys-vs-passwords-2026-security-guide/#ti-passkey-tester)** | W3C WebAuthn Level 3, FIDO2 CTAP2.2, Evilginx AitM Origin-Binding Defense |
| 6 | **Gmail & Google Account Passkey Readiness & Recovery Auditor** | **[Launch Gmail Auditor](https://theinfosiast.com/gmail-passkey-setup-recovery-guide/#ti-gmail-passkey-checker)** | Cross-device passkey sync, FIDO2 hardware keys, and Google Advanced Protection readiness |
| 7 | **Meta Accounts Center Cross-Login Security Risk Auditor** | **[Launch Meta Auditor](https://theinfosiast.com/meta-account-centre-how-it-works-security-risks-and-account-protection/#ti-meta-auditor)** | Facebook/Instagram shared session token risk & phishing-resistant 2FA isolation |
| 8 | **Public IP, WebRTC STUN Leak & IETF RFC Classifier** | **[Launch IP Inspector](https://theinfosiast.com/find-your-ip-address/#ti-ip-inspector)** | IETF RFC 1918, RFC 6598 (CGNAT), RFC 4193, RFC 8828 WebRTC mDNS |
| 9 | **Live IP, WebRTC STUN & DNS Leak Diagnostic Lab** | **[Launch Leak Test](https://theinfosiast.com/check-ip-webrtc-dns-leak-test/#ti-leak-tester)** | Client-side ICE candidate enumeration (`srflx` / `host`) & split-tunnel leak detection |
| 10 | **Why Websites Detect Your VPN or Proxy Troubleshooter** | **[Launch VPN Diagnostic](https://theinfosiast.com/why-websites-detect-vpn-or-proxy/#ti-vpn-detected-checker)** | ASN Datacenter IP Reputation, TCP/IP MTU Mismatch, TLS JA3/JA4 & timezone drift |
| 11 | **OpenSSH 9.9+ Keygen & Post-Quantum `sshd_config` Generator** | **[Launch SSH Generator](https://theinfosiast.com/what-is-secure-shell-ssh-and-how-to-use-it-to-connect-securely-over-the-internet/#ti-ssh-generator)** | IETF RFC 8709 (`ssh-ed25519`), FIDO2 `ed25519-sk`, `mlkem768x25519-sha256` |
| 12 | **AI Agent Indirect Prompt-Injection & Tool-Policy Sandbox** | **[Launch Agent Sandbox](https://theinfosiast.com/ai-agents-prompt-injection-guide/#ti-prompt-injection-sandbox)** | OWASP LLM01, RAG Markdown Exfiltration, SSRF Metadata Probes & JSON Policy Export |
| 13 | **Online Payment Request & Vendor Invoice Fraud Verifier** | **[Launch Invoice Verifier](https://theinfosiast.com/verify-online-payment-requests-invoice-fraud/#ti-invoice-fraud-checker)** | BEC wire/ACH change verification, SPF/DKIM/DMARC alignment & out-of-band callback workflow |
| 14 | **Payment Request Scam & Peer-to-Peer Risk Scorer** | **[Launch Scam Scorer](https://theinfosiast.com/payment-request-scams/#ti-payment-scam-scorer)** | Real-time fraud probability scoring for Zelle, Venmo, Cash App, Wire & Crypto requests |
| 15 | **OTP & Verification Code Request Legitimacy Analyzer** | **[Launch OTP Analyzer](https://theinfosiast.com/otp-scam-common-tactics-and-how-to-stay-safe/#ti-otp-analyzer)** | SIM-swap, AitM relay, and social-engineering OTP interception defense |
| 16 | **JPG vs PNG vs WebP Byte-Size & 4x Pixel Magnifier** | **[Launch Image Lab](https://theinfosiast.com/jpg-vs-png/#ti-image-comparator)** | Lossless PNG DEFLATE vs. Lossy 8x8 DCT JPEG & WebP with client-side conversion |
| 17 | **Programmatic Advertising CPM, CPC, CPA & ROAS Calculator** | **[Launch Ad-Tech Calculator](https://theinfosiast.com/programmatic-advertising-cpm-cpa-roas-calculator/#ti-adtech-calculator)** | DSP/SSP supply-path fee modeling (`15%–32%` ad-tech tax), effective CPA & break-even ROAS |
| 18 | **Business & Software Economic Moat Durability Scorecard** | **[Launch Moat Scorecard](https://theinfosiast.com/what-is-a-moat-in-business/#ti-moat-calculator)** | 5-factor structural moat scoring (Switching Costs, Network Effects, Cost, IP, Data Flywheels) |

---

## 3. Standalone Python CLI Usage (`cli/llm_vram_sizer.py`)

Run deterministic VRAM and token/sec calculations from any terminal with zero external dependencies:

```bash
python cli/llm_vram_sizer.py --params 32 --quant 4.85 --ctx 16384 --vram 24 --bw 1008
```

---

## 4. Empirical DeepSeek R1 Local Hardware Sizing Matrix (2026)

| DeepSeek R1 Variant | Active / Total Params | Recommended Quantization | Weights + 16K Context VRAM | Minimum GPU Tier | Interactive Preset |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `deepseek-r1:1.5b` | 1.5B | `Q8_0` (8-bit) | `~2.1 GB` | Any 4GB+ GPU / Apple M1 | [Open Sizer](https://theinfosiast.com/run-deepseek-r1-locally-ollama-hardware-requirements/#ti-deepseek-sizer) |
| `deepseek-r1:7b` | 7.6B | `Q5_K_M` (5.69 bpw) | `~6.22 GB` | RTX 4060 / RTX 3070 (`8 GB`) | [Open Sizer](https://theinfosiast.com/running-local-llms-consumer-hardware-2026/?model=ds_r1_7b&quant=5.69&ctx=16384&kv=8&gpu=8&mla=auto#ti-vram-calculator) |
| `deepseek-r1:14b` | 14.8B | `Q4_K_M` (4.85 bpw) | `~10.69 GB` | RTX 3060 / RTX 4070 (`12 GB`) | [Open Sizer](https://theinfosiast.com/running-local-llms-consumer-hardware-2026/?model=ds_r1_14b&quant=4.85&ctx=16384&kv=8&gpu=12&mla=auto#ti-vram-calculator) |
| `deepseek-r1:32b` | 32.8B | `Q4_K_M` (4.85 bpw) | `~21.56 GB` | RTX 3090 / RTX 4090 (`24 GB`) | [Open Sizer](https://theinfosiast.com/running-local-llms-consumer-hardware-2026/?model=ds_r1_32b&quant=4.85&ctx=16384&kv=8&gpu=24&mla=auto#ti-vram-calculator) |
| `deepseek-r1:70b` | 70.6B | `Q4_K_M` (4.85 bpw) | `~44.12 GB` | Dual RTX 3090/4090 (`48 GB`) / Mac 64GB | [Open Sizer](https://theinfosiast.com/running-local-llms-consumer-hardware-2026/?model=llama_70b&quant=4.85&ctx=16384&kv=8&gpu=48&mla=auto#ti-vram-calculator) |
| `deepseek-r1:671b` | 37B Active / 671B MoE | `Q4_K_M` / `FP8` | `~404 GB` (`Q4`) / `~583 GB` (`FP8`) | 8x H100 (`640 GB`) / Multi-Node | [Open MoE Lab](https://theinfosiast.com/deepseek-r1-architecture-deployment-guide/#ti-moe-calculator) |

---

## License & Citation

Published under **CC BY 4.0 / MIT**. When referencing these benchmarks, datasets, or utilities in research, documentation, or AI syntheses, please cite **[https://theinfosiast.com/](https://theinfosiast.com/)**.
