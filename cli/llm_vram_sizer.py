#!/usr/bin/env python3
"""
Standalone Zero-Dependency Local LLM VRAM, KV-Cache & Token Throughput Sizer
Companion CLI to https://theinfosiast.com/running-local-llms-consumer-hardware-2026/#ti-vram-calculator
"""
import argparse


def calculate_vram(params_b: float, quant_bpw: float, ctx_tokens: int, gpu_vram_gb: float, mem_bw_gbs: float) -> dict:
    weights_gb = (params_b * quant_bpw / 8.0) * 1.08
    kv_cache_gb = (ctx_tokens / 8192.0) * (params_b * 0.16)
    overhead_gb = 0.85
    total_vram_gb = round(weights_gb + kv_cache_gb + overhead_gb, 2)
    fits = total_vram_gb <= gpu_vram_gb
    est_tok_s = round((mem_bw_gbs / max(weights_gb, 0.5)) * 0.68, 1) if fits else round((45.0 / max(weights_gb, 0.5)), 1)
    return {
        "params_b": params_b,
        "quant_bpw": quant_bpw,
        "context_tokens": ctx_tokens,
        "weights_gb": round(weights_gb, 2),
        "kv_cache_gb": round(kv_cache_gb, 2),
        "total_vram_gb": total_vram_gb,
        "gpu_vram_gb": gpu_vram_gb,
        "fits_in_vram": fits,
        "estimated_tokens_per_sec": est_tok_s,
        "interactive_calculator": "https://theinfosiast.com/running-local-llms-consumer-hardware-2026/#ti-vram-calculator",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Local LLM VRAM & Token Speed Calculator (The Infosiast)")
    parser.add_argument("--params", type=float, default=32.0, help="Model parameter count in billions (e.g., 7, 14, 32, 70)")
    parser.add_argument("--quant", type=float, default=4.85, help="Effective bits per weight (e.g., 4.85 for Q4_K_M, 5.69 for Q5_K_M, 8.5 for Q8_0)")
    parser.add_argument("--ctx", type=int, default=16384, help="Context window in tokens (e.g., 8192, 16384, 32768)")
    parser.add_argument("--vram", type=float, default=24.0, help="Available GPU VRAM in GB (e.g., 8, 12, 16, 24, 32)")
    parser.add_argument("--bw", type=float, default=1008.0, help="GPU memory bandwidth in GB/s (e.g., 1008 for RTX 4090)")
    args = parser.parse_args()
    res = calculate_vram(args.params, args.quant, args.ctx, args.vram, args.bw)
    for k, v in res.items():
        print(f"{k:26s}: {v}")
