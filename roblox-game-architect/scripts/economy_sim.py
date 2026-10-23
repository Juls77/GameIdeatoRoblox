#!/usr/bin/env python3
"""Progressions-Check für Roblox-Economy-Kurven.

Simuliert einen aktiven Spieler, der jedes Upgrade kauft, sobald er es sich leisten kann,
und prüft, ob Upgrade-Kosten, Einkommen und Zeitziele zusammenpassen (z. B. "erster
Rebirth nach 60–90 Min", "Upgrade alle 15–60 Sek in den ersten 10 Min").

Beispiel (Tycoon: Kosten 50 * 1.12^(n-1), Einkommen +0.8/s pro Stufe, 50 Stufen):
  python3 economy_sim.py --base 50 --growth 1.12 --levels 50 --income-start 2 --income-per-level 0.8

Optionen:
  --income-mult  Multiplikator auf das Einkommen (z. B. 2 für 2x-Pass, 1.5 für seltene Bewohner)
  --checkpoints  Stufen, die in der Tabelle erscheinen (Standard: 1,5,10,25,40,Max)
"""
import argparse


def simulate(base, growth, levels, income_start, income_per_level, income_mult, offset):
    t = 0.0
    rows = []
    for n in range(1, levels + 1):
        cost = base * growth ** (n - 1 + offset)
        income = (income_start + income_per_level * (n - 1)) * income_mult
        wait = cost / income
        t += wait
        rows.append((n, cost, income, wait, t))
    return rows


def fmt_time(s):
    if s < 120:
        return f"{s:.0f} s"
    if s < 7200:
        return f"{s / 60:.1f} min"
    return f"{s / 3600:.1f} h"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", type=float, required=True, help="Kosten der ersten Stufe")
    p.add_argument("--growth", type=float, required=True, help="Faktor r pro Stufe, z. B. 1.12")
    p.add_argument("--levels", type=int, required=True)
    p.add_argument("--income-start", type=float, required=True, help="Einkommen/Sek vor Stufe 1")
    p.add_argument("--income-per-level", type=float, required=True, help="Einkommenszuwachs/Sek pro Stufe")
    p.add_argument("--income-mult", type=float, default=1.0)
    p.add_argument("--offset", type=int, default=0, help="Exponent-Offset (0 = Kosten(1) = base)")
    p.add_argument("--checkpoints", type=str, default="")
    a = p.parse_args()

    rows = simulate(a.base, a.growth, a.levels, a.income_start, a.income_per_level, a.income_mult, a.offset)
    cps = {int(x) for x in a.checkpoints.split(",") if x} or {1, 5, 10, 25, 40, a.levels}
    print(f"{'Stufe':>5} | {'Kosten':>12} | {'Eink./s':>8} | {'Wartezeit':>10} | {'kumuliert':>10}")
    print("-" * 58)
    for n, cost, inc, wait, t in rows:
        if n in cps:
            print(f"{n:>5} | {cost:>12,.0f} | {inc:>8.1f} | {fmt_time(wait):>10} | {fmt_time(t):>10}")
    total_cost = sum(r[1] for r in rows)
    print("-" * 58)
    print(f"Summe Kosten: {total_cost:,.0f} | Zeit bis Stufe {a.levels}: {fmt_time(rows[-1][4])}")
    ten = max((r[0] for r in rows if r[4] <= 600), default=0)
    print(f"Stufen in den ersten 10 Min (nur Upgrades, ohne FTUE-Pausen): {ten}")
    slow = [r[0] for r in rows if r[4] <= 600 and r[3] > 60]
    if slow:
        print(f"WARNUNG: Wartezeit > 60 s schon in den ersten 10 Min bei Stufe {slow[0]}")


if __name__ == "__main__":
    main()
