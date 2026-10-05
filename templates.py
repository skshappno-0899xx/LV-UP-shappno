# -*- coding: utf-8 -*-

_FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Orbitron:wght@500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Inter',system-ui,sans-serif;background:#000;color:#fff;min-height:100vh;-webkit-font-smoothing:antialiased}
:root{--bg:#000;--card:#08080c;--card2:#101015;--line:#1a1a22;--line2:#25252e;--txt:#fff;--mut:#8a8a95;--dim:#55555f;--green:#22c55e;--red:#ef4444;--blue:#3b82f6;--lightblue:#38bdf8;--purple:#8b5cf6;--gold:#f59e0b}
.mono{font-family:'JetBrains Mono',monospace}
.orb{font-family:'Orbitron',sans-serif}
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-track{background:#0a0a0a}
::-webkit-scrollbar-thumb{background:#262626;border-radius:4px}
::-webkit-scrollbar-thumb:hover{background:#3a3a3a}
"""

_ICONS = {
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    "fast": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 19 22 12 13 5 13 19"></polygon><polygon points="2 19 11 12 2 5 2 19"></polygon></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
    "refresh": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg>',
    "cloud": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    "list": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="6" height="4" rx="1"></rect><rect x="3" y="15" width="6" height="4" rx="1"></rect><line x1="14" y1="7" x2="21" y2="7"></line><line x1="14" y1="17" x2="21" y2="17"></line></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    "crown": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 18h20l-1.5-9-4 3-4.5-7-4.5 7-4-3z"></path></svg>',
    "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>',
    "pause": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="4" width="4" height="16" rx="1"></rect><rect x="14" y="4" width="4" height="16" rx="1"></rect></svg>',
    "play": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="6 4 20 12 6 20 6 4"></polygon></svg>',
    "trash": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"></path><path d="M10 11v6M14 11v6"></path><path d="M9 6V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"></path></svg>',
    "monitor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>',
    "gamepad": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="12" x2="10" y2="12"></line><line x1="8" y1="10" x2="8" y2="14"></line><line x1="15" y1="13" x2="15.01" y2="13"></line><line x1="18" y1="11" x2="18.01" y2="11"></line><rect x="2" y="6" width="20" height="12" rx="6"></rect></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>',
    "id": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"></rect><circle cx="9" cy="11" r="2"></circle><path d="M15 10h3M15 14h3"></path></svg>',
    "trophy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8M12 17v4M7 4h10v6a5 5 0 0 1-10 0V4z"></path><path d="M17 5h3a2 2 0 0 1 0 4h-1M7 5H4a2 2 0 0 0 0 4h1"></path></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>',
    "warn": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
    "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',
    "plus": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>',
    "arrow_right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
    "star_fill": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    "bolt_fill": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    "crown_fill": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 18h20l-1.5-9-4 3-4.5-7-4.5 7-4-3z"></path></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>',
    "copy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>',
    "restart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M3 21v-5h5"/></svg>',
}

def _icon(name, color="currentColor", size=16, stroke_extra=""):
    svg = _ICONS.get(name, "")
    if not svg:
        return ""
    svg = svg.replace('stroke="currentColor"', f'stroke="{color}"')
    svg = svg.replace('<svg ', f'<svg width="{size}" height="{size}" ', 1)
    return svg


def _icon_inline(name, color="currentColor", size=16):
    svg = _ICONS.get(name, "")
    if not svg:
        return ""
    svg = svg.replace('stroke="currentColor"', f'stroke="{color}"')
    svg = svg.replace('<svg ', f'<svg width="{size}" height="{size}" style="display:inline-block;vertical-align:middle" ', 1)
    return svg


# ==================== HOME (Landing) ====================
HOME_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>SHAPPNO LV UP - Free Fire Automation</title>
""" + _FONTS + """
<style>
""" + _CSS + """
html{scroll-behavior:smooth}
html,body{height:100%}
body{background:#050505;min-height:100vh;position:relative;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background:
  linear-gradient(rgba(255,255,255,0.015) 1px,transparent 1px),
  linear-gradient(90deg,rgba(255,255,255,0.015) 1px,transparent 1px);
  background-size:60px 60px;pointer-events:none;z-index:0;
  mask-image:radial-gradient(ellipse at 50% 40%,#000 20%,transparent 75%);
  -webkit-mask-image:radial-gradient(ellipse at 50% 40%,#000 20%,transparent 75%)}

.ann{position:relative;z-index:5;background:#38bdf8;color:#000;padding:9px 40px 9px 14px;text-align:center;font-size:12px;font-weight:600;font-family:'Inter',sans-serif}
.ann a{color:#000;text-decoration:underline;font-weight:800}
.ann .cls{position:absolute;right:12px;top:50%;transform:translateY(-50%);background:transparent;border:none;cursor:pointer;color:#000;font-size:16px;line-height:1;padding:4px}

.hdr{position:relative;z-index:5;display:flex;align-items:center;justify-content:space-between;padding:14px 18px;border-bottom:1px solid #151515}
.hlogo{display:flex;align-items:center;gap:10px}
.hshield{width:34px;height:34px;display:inline-flex;align-items:center;justify-content:center}
.hshield svg{width:34px;height:34px;stroke:#fff;fill:none;stroke-width:1.8}
.hname{font-family:'Inter',sans-serif;font-size:14px;font-weight:800;letter-spacing:2.5px;color:#fff}
.hbell{background:transparent;border:none;cursor:pointer;padding:6px;color:#fff}
.hbell svg{width:20px;height:20px;stroke:#fff;fill:none;stroke-width:1.8}

.status{position:relative;z-index:5;display:flex;justify-content:center;padding:16px 18px 0}
.spill{display:inline-flex;align-items:center;gap:8px;background:#0d0d0d;border:1px solid #1c1c1c;border-radius:24px;padding:7px 14px 7px 11px;font-family:'Inter',sans-serif;font-size:11px;font-weight:600;color:#b8b8b8}
.spill .dot{width:7px;height:7px;border-radius:50%;background:#22c55e;box-shadow:0 0 8px #22c55e;animation:pl 1.4s infinite}
.spill .mut{color:#5a5a5a;font-weight:400;margin-left:2px}
@keyframes pl{0%,100%{opacity:1}50%{opacity:0.4}}

.hero{position:relative;z-index:5;padding:50px 22px 20px;max-width:640px;margin:0 auto;text-align:center}
.hero h1{font-family:'Inter',sans-serif;font-size:26px;font-weight:800;letter-spacing:1.5px;margin-bottom:36px;
  background:linear-gradient(90deg,#38bdf8,#a78bfa,#38bdf8);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 0 24px rgba(56,189,248,0.35));}
.hero p{font-family:'Inter',sans-serif;font-size:17px;font-weight:500;line-height:1.65;color:#b8b8b8;letter-spacing:0.2px}
.hero p + p{margin-top:14px}

.ctas{position:relative;z-index:5;display:flex;gap:12px;justify-content:center;padding:24px 18px 50px;flex-wrap:wrap;max-width:440px;margin:0 auto}
.cbtn{flex:1;min-width:140px;padding:14px 20px;border-radius:10px;font-family:'Inter',sans-serif;font-size:14px;font-weight:800;letter-spacing:0.5px;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;gap:8px;border:1px solid transparent;transition:all 0.2s}
.cb-white{background:#38bdf8;color:#000}
.cb-white:hover{background:#7dd3fc}
.cb-out{background:transparent;border-color:#2a2a2a;color:#fff}
.cb-out:hover{border-color:#38bdf8;background:#0d0d0d}
.cbtn svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2.2}

.psec{position:relative;z-index:5;max-width:1200px;margin:0 auto;padding:0 18px 80px;scroll-margin-top:20px}
.ptitle{text-align:center;font-family:'Inter',sans-serif;font-size:24px;font-weight:800;letter-spacing:1px;color:#fff;margin-bottom:8px}
.psub{text-align:center;font-size:11px;color:#7a7a7a;letter-spacing:3px;text-transform:uppercase;margin-bottom:14px;font-weight:600}
.pnote{text-align:center;font-size:11px;color:#7a8ba0;max-width:560px;margin:0 auto 30px;line-height:1.6;padding:10px 16px;background:rgba(56,189,248,0.05);border:1px solid rgba(56,189,248,0.15);border-radius:10px}
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
@media(max-width:700px){.pgrid{grid-template-columns:1fr}}

.pc{background:#0b0b0e;border:1.5px solid #1f1f24;border-radius:18px;padding:32px 22px 22px;position:relative;display:flex;flex-direction:column;transition:all 0.3s}
.pc.blue{border-color:rgba(56,189,248,0.45)}
.pc.blue:hover{border-color:#38bdf8;box-shadow:0 0 40px rgba(56,189,248,0.25);transform:translateY(-4px)}
.pc.purple{border-color:rgba(139,92,246,0.5)}
.pc.purple:hover{border-color:#8b5cf6;box-shadow:0 0 40px rgba(139,92,246,0.3);transform:translateY(-4px)}
.pc.gold{border-color:rgba(245,158,11,0.5)}
.pc.gold:hover{border-color:#f59e0b;box-shadow:0 0 40px rgba(245,158,11,0.25);transform:translateY(-4px)}
.ribbon{position:absolute;top:-11px;right:20px;background:linear-gradient(135deg,#8b5cf6,#6d28d9);color:#fff;font-family:'Inter',sans-serif;font-size:9px;font-weight:800;letter-spacing:1.5px;padding:5px 12px;border-radius:20px;text-transform:uppercase;box-shadow:0 4px 20px rgba(139,92,246,0.5)}
.pi{width:64px;height:64px;margin:0 auto 20px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.pc.blue .pi{background:rgba(56,189,248,0.08);border:1.5px solid rgba(56,189,248,0.35);color:#38bdf8}
.pc.purple .pi{background:rgba(139,92,246,0.08);border:1.5px solid rgba(139,92,246,0.4);color:#a78bfa}
.pc.gold .pi{background:rgba(245,158,11,0.08);border:1.5px solid rgba(245,158,11,0.4);color:#fbbf24}
.pi svg{width:28px;height:28px}
.pn{text-align:center;font-family:'Inter',sans-serif;font-size:20px;font-weight:800;letter-spacing:5px;margin-bottom:14px;color:#fff;text-transform:uppercase}
.pl{display:flex;justify-content:center;align-items:center;gap:10px;margin-bottom:8px}
.op{font-family:'Inter',sans-serif;font-size:15px;font-weight:700;color:#4a4a4a;text-decoration:line-through}
.deal{background:#dc2626;color:#fff;font-family:'Inter',sans-serif;font-size:9px;font-weight:800;letter-spacing:1.2px;padding:3px 8px;border-radius:5px}
.pm{text-align:center;font-family:'Inter',sans-serif;font-size:48px;font-weight:900;letter-spacing:-1px;margin-bottom:26px;line-height:1;color:#fff}
.pm .cur{font-size:26px;font-weight:700;vertical-align:top;line-height:1;display:inline-block;margin-right:2px}
.feats{list-style:none;margin-bottom:22px;flex:1}
.feats li{display:flex;align-items:flex-start;gap:10px;padding:7px 0;font-size:13px;color:#d8d8dd;line-height:1.45;font-weight:500}
.feats li .ic{flex-shrink:0;width:18px;height:18px;display:flex;align-items:center;justify-content:center;margin-top:2px;color:#22c55e}
.feats li .ic svg{width:14px;height:14px}
.bb{width:100%;padding:13px;border-radius:10px;font-family:'Inter',sans-serif;font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;border:none;cursor:pointer;transition:all 0.25s;color:#fff}
.pc.blue .bb{background:linear-gradient(135deg,#38bdf8,#0284c7);box-shadow:0 6px 24px rgba(56,189,248,0.3)}
.pc.purple .bb{background:linear-gradient(135deg,#8b5cf6,#7c3aed);box-shadow:0 6px 24px rgba(139,92,246,0.35)}
.pc.gold .bb{background:linear-gradient(135deg,#f59e0b,#d97706);box-shadow:0 6px 24px rgba(245,158,11,0.3);color:#000}
.an{text-align:center;font-size:10px;color:#4a4a4a;margin-top:10px;letter-spacing:0.5px;font-weight:500}

.tg{position:fixed;right:18px;bottom:18px;width:52px;height:52px;border-radius:50%;background:#22a7e8;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 28px rgba(34,167,232,0.5);cursor:pointer;z-index:20;border:none;text-decoration:none}
.tg svg{width:26px;height:26px;fill:#fff}

.mtop{position:fixed;inset:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(8px);z-index:100;display:none;align-items:center;justify-content:center;padding:18px}
.mtop.on{display:flex}
.mbox{background:#141414;border:1px solid #262626;border-radius:18px;padding:22px;max-width:440px;width:100%;position:relative;font-family:'Inter',sans-serif}
.mh-row{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:24px}
.mh-row h3{font-size:17px;font-weight:700;color:#fff;letter-spacing:0.2px}
.mclose{width:34px;height:34px;border-radius:50%;border:1px solid #2a2a2a;background:transparent;color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.mclose:hover{background:#1e1e1e}
.mclose svg{width:16px;height:16px;stroke:#fff;fill:none;stroke-width:2}
.micon{width:56px;height:56px;margin:0 auto 18px;display:flex;align-items:center;justify-content:center}
.micon svg{width:56px;height:56px;stroke:#fff;fill:none;stroke-width:1.5}
.mtitle{text-align:center;font-size:19px;font-weight:800;color:#fff;margin-bottom:14px;letter-spacing:0.3px}
.mtext{text-align:center;font-size:13px;line-height:1.65;color:#a8a8a8;margin-bottom:22px}
.mbtn{width:100%;padding:14px;border-radius:10px;background:#fff;color:#000;border:none;font-family:'Inter',sans-serif;font-size:14px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;text-decoration:none}
.mbtn:hover{background:#e5e5e5}
</style>
</head>
<body>

<div class="ann" id="ann">
<span id="home-notif">IND server is disabled &mdash; please wait patiently!</span>
<button class="cls" onclick="document.getElementById('ann').style.display='none'">✕</button>
</div>

<div class="hdr">
<div class="hlogo">
<img src="https://files.catbox.moe/1o431f.jpg" alt="Logo" style="width:34px;height:34px;border-radius:8px;object-fit:cover;border:1.5px solid #38bdf8;box-shadow:0 0 8px rgba(56,189,248,0.6)">
<span class="hname">SHAPPNO LV UP</span>
</div>
<button class="hbell"><svg viewBox="0 0 24 24"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg></button>
</div>

<div class="status">
<span class="spill"><span class="dot"></span> System Operational <span class="mut">0ms</span></span>
</div>

<div class="hero">
<h1>SHAPPNO LV UP</h1>
<p>Fast, reliable Free Fire level-up automation built for players who want results without the grind. Simple setup, real progress.</p>
<p>Level up your account faster &mdash; stay ahead of the competition.</p>
</div>

<div class="ctas">
<a href="/login" class="cbtn cb-white">Get Started <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a>
<a href="#pricing" class="cbtn cb-out">Pricing <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></a>
</div>

<!-- Pricing -->
<div class="psec" id="pricing">
<div class="ptitle">Choose Your Plan</div>
<div class="psub">Works On All Servers</div>
<div class="pnote">All plans work globally across every Free Fire server &mdash; IND, BD, EUROPE, SG, TH, PH, VN, MY, ID, HK, TW and more. Price shown in USD.</div>
<div class="pgrid" id="pgrid"></div>

<!-- Safe & VIP Cards (BELOW the 3 big plan cards) -->
<div style="max-width:640px;margin:32px auto 0;display:grid;grid-template-columns:1fr 1fr;gap:14px">
<div style="background:linear-gradient(135deg,rgba(34,197,94,0.12),rgba(34,197,94,0.03));border:1.5px solid rgba(34,197,94,0.4);border-radius:14px;padding:16px;text-align:center">
<div style="display:inline-flex;width:40px;height:40px;border-radius:50%;background:rgba(34,197,94,0.15);color:#22c55e;align-items:center;justify-content:center;margin-bottom:8px">
<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
</div>
<div style="font-family:'Orbitron',sans-serif;font-size:14px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#fff;margin-bottom:4px">normal</div>
<div style="font-size:11px;color:#86efac;font-weight:600">7 Days ban only </div>
</div>
<div style="background:linear-gradient(135deg,rgba(245,158,11,0.15),rgba(245,158,11,0.03));border:1.5px solid rgba(245,158,11,0.5);border-radius:14px;padding:16px;text-align:center">
<div style="display:inline-flex;width:40px;height:40px;border-radius:50%;background:rgba(245,158,11,0.15);color:#f59e0b;align-items:center;justify-content:center;margin-bottom:8px">
<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 18h20l-1.5-9-4 3-4.5-7-4.5 7-4-3z"></path></svg>
</div>
<div style="font-family:'Orbitron',sans-serif;font-size:14px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#fff;margin-bottom:4px">VIP</div>
<div style="font-size:11px;color:#fcd34d;font-weight:600">no ban </div>
</div>
</div>

</div>

<a class="tg" href="https://t.me/shappno_04xx" target="_blank"><svg viewBox="0 0 24 24"><path d="M9.78 18.65l.28-4.23 7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3 3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"/></svg></a>

<div class="mtop" id="maint">
<div class="mbox">
<div class="mh-row">
<h3>Important Update</h3>
<button class="mclose" onclick="document.getElementById('maint').classList.remove('on')"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
</div>
<div class="micon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="8 12 11 15 16 9"/></svg></div>
<div class="mtitle" id="notif-title">Important Update</div>
<div class="mtext" id="notif-text">Loading...</div>
<a class="mbtn" href="https://t.me/shappno_04xx" target="_blank">Chat Now</a>
</div>
</div>

<script>
const PLANS=[
{id:'starting',name:'STARTING',style:'blue',icon:'bolt',hours:24,slots:3,price:'1',old:'2',pop:false},
{id:'basic',name:'BASIC',style:'purple',icon:'star',hours:48,slots:3,price:'2',old:'4',pop:true},
{id:'premium',name:'PREMIUM',style:'gold',icon:'crown',hours:72,slots:4,price:'2.5',old:'6',pop:false}
];
const TG='shappno_04xx';
const ICONS={
bolt:'__SVG_BOLT__',
star:'__SVG_STAR__',
crown:'__SVG_CROWN__',
check:'__SVG_CHECK__'
};

function feat(p){
const d=p.hours>=24?Math.round(p.hours/24)+' Day'+(p.hours>=48?'s':''):p.hours+' Hours';
const sp=p.id==='premium'?'Fastest Leveling Speed Available':'Fast Leveling Performance';
const off=p.id==='premium'?'Runs 24/7 — No Need To Stay Online':'Runs While You Are Offline';
return[
'Access To The Panel For '+d,
sp,
'Run Multiple Accounts At Once',
'Restart & Manage Accounts Anytime',
off,
'Telegram Payment Support & Quick Help',
p.slots+' Concurrent Account'+(p.slots>1?'s':'')
];
}

function render(){
const g=document.getElementById('pgrid');
let h='';
PLANS.forEach(p=>{
let fh='';
feat(p).forEach(t=>{fh+='<li><span class="ic">'+ICONS.check+'</span><span>'+t+'</span></li>';});
h+='<div class="pc '+p.style+'">';
if(p.pop)h+='<div class="ribbon">Most Popular</div>';
h+='<div class="pi">'+ICONS[p.icon]+'</div>';
h+='<div class="pn">'+p.name+'</div>';
h+='<div class="pl"><span class="op">$'+p.old+'</span><span class="deal">Deal</span></div>';
h+='<div class="pm"><span class="cur">$</span>'+p.price+'</div>';
h+='<ul class="feats">'+fh+'</ul>';
h+='<button class="bb" onclick="buy(\\''+p.id+'\\')">Buy '+p.name+'</button>';
h+='<div class="an">Instant Activation After Payment</div>';
h+='</div>';
});
g.innerHTML=h;
}

function buy(id){
const p=PLANS.find(x=>x.id===id);
let m='Hi, I Want To Buy The '+p.name+' Plan.\\n\\nPlan: $'+p.price+'\\nDuration: '+p.hours+' Hours\\nSlots: '+p.slots+'\\n\\nPlease Send Payment Details.';
window.open('https://t.me/'+TG+'?text='+encodeURIComponent(m),'_blank');
}
render();

document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',e=>{
    const id=a.getAttribute('href');
    if(id.length>1){
      const el=document.querySelector(id);
      if(el){
        e.preventDefault();
        el.scrollIntoView({behavior:'smooth',block:'start'});
      }
    }
  });
});

(async function loadHomeNotif(){
  try{
    const r = await fetch('/api/notification');
    const d = await r.json();
    if(d.status==='ok' && d.text){
      document.getElementById('home-notif').textContent = d.text;
      document.getElementById('notif-text').textContent = d.text;
    }
  }catch(e){}
})();

document.getElementById('maint').classList.add('on');
document.getElementById('maint').addEventListener('click',e=>{
  if(e.target.id==='maint')document.getElementById('maint').classList.remove('on');
});
</script>
</body>
</html>
"""

HOME_HTML = HOME_HTML.replace("__SVG_BOLT__", _icon("bolt_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_STAR__", _icon("star_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_CROWN__", _icon("crown_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_CHECK__", _icon("check", "#22c55e", 14).replace('"', '\\"'))


# ==================== LOGIN ====================
LOGIN_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>Login - SHAPPNO LV UP</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:#000;display:flex;align-items:center;justify-content:center;padding:20px;min-height:100vh;position:relative;overflow:hidden}
body::before{content:'';position:absolute;inset:0;background:
  linear-gradient(rgba(56,189,248,0.02) 1px,transparent 1px),
  linear-gradient(90deg,rgba(56,189,248,0.02) 1px,transparent 1px);
  background-size:60px 60px;pointer-events:none;mask-image:radial-gradient(ellipse at center,#000 20%,transparent 80%);
  -webkit-mask-image:radial-gradient(ellipse at center,#000 20%,transparent 80%)}

.wrap{width:100%;max-width:440px;position:relative;z-index:1}
.brand{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;margin-bottom:32px}

.img-logo{
  width:88px;height:88px;
  border-radius:14px;
  object-fit:cover;
  border:2px solid #38bdf8;
  box-shadow:
    0 0 15px rgba(56,189,248,0.9),
    0 0 30px rgba(56,189,248,0.6),
    0 0 60px rgba(56,189,248,0.4);
  animation:glow 1.8s ease-in-out infinite alternate;
}
@keyframes glow{
  0%{box-shadow:0 0 15px rgba(56,189,248,0.9),0 0 30px rgba(56,189,248,0.6),0 0 60px rgba(56,189,248,0.4);transform:scale(1)}
  100%{box-shadow:0 0 25px rgba(56,189,248,1),0 0 50px rgba(56,189,248,0.9),0 0 100px rgba(56,189,248,0.6);transform:scale(1.03)}
}
.brand-txt{font-family:'Orbitron',sans-serif;font-size:18px;font-weight:900;letter-spacing:3px;
  background:linear-gradient(90deg,#38bdf8,#7dd3fc,#38bdf8);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 0 12px rgba(56,189,248,0.6));}

.welcome{text-align:center;margin-bottom:28px}
.welcome h1{font-family:'Inter',sans-serif;font-size:24px;font-weight:700;letter-spacing:-0.5px;color:#fff;margin-bottom:8px}
.welcome p{font-size:13px;color:#7a7a7a;font-weight:400}

.err{background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.3);color:#ef4444;padding:11px;border-radius:10px;font-size:12px;margin-bottom:16px;display:none;text-align:center}
.err.on{display:block}

.f{margin-bottom:20px}
.f label{display:block;font-size:12px;font-weight:700;color:#b8b8b8;margin-bottom:9px;text-align:center;letter-spacing:1px;text-transform:uppercase}
.iw{position:relative}
.iw svg.lft{position:absolute;left:16px;top:50%;transform:translateY(-50%);width:18px;height:18px;stroke:#38bdf8;fill:none;stroke-width:1.8;pointer-events:none}
.iw svg.rgt{position:absolute;right:16px;top:50%;transform:translateY(-50%);width:18px;height:18px;stroke:#38bdf8;fill:none;stroke-width:1.8;cursor:pointer;transition:stroke 0.2s}
.iw svg.rgt:hover{stroke:#7dd3fc}
.f input{
  width:100%;background:transparent;
  border:1.5px solid #1e293b;border-radius:10px;
  padding:15px 46px;
  color:#fff;font-size:14px;
  font-family:'Inter',sans-serif;font-weight:500;
  outline:none;transition:all 0.2s;
}
.f input::placeholder{color:#4a4a4a;font-weight:400}
.f input:focus{border-color:#38bdf8;background:rgba(56,189,248,0.04);box-shadow:0 0 0 3px rgba(56,189,248,0.1)}

.btn{
  width:100%;padding:17px;border-radius:10px;
  background:linear-gradient(135deg,#38bdf8,#0284c7);
  color:#fff;
  border:none;cursor:pointer;
  font-family:'Inter',sans-serif;
  font-size:15px;font-weight:800;
  letter-spacing:0.5px;
  display:flex;align-items:center;justify-content:center;gap:10px;
  transition:all 0.2s;
  box-shadow:0 6px 24px rgba(56,189,248,0.3);
  margin-top:8px;
}
.btn:hover{box-shadow:0 8px 32px rgba(56,189,248,0.5);transform:translateY(-1px)}
.btn svg{width:18px;height:18px;stroke:#fff;fill:none;stroke-width:2.2}
.btn:disabled{opacity:0.6;cursor:not-allowed}

.foot{text-align:center;margin-top:24px;font-size:13px;color:#6a6a6a}
.foot a{color:#38bdf8;text-decoration:none;font-weight:700}
.foot a:hover{text-decoration:underline}
</style>
</head>
<body>
<div class="wrap">

<div class="brand">
<img class="img-logo" src="https://files.catbox.moe/1o431f.jpg" alt="Logo">
<span class="brand-txt">SHAPPNO LV UP</span>
</div>

<div class="welcome">
<h1>Welcome Back</h1>
<p>Enter your password to continue</p>
</div>

<div class="err" id="err"></div>

<form id="f">
<div class="f">
<label>Password</label>
<div class="iw">
<svg class="lft" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
<svg class="rgt" id="eye" viewBox="0 0 24 24"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
<input type="password" id="p" placeholder="Enter your password" autocomplete="current-password" required>
</div>
</div>

<button type="submit" class="btn" id="sb">
Login
<svg viewBox="0 0 24 24"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><polyline points="10 17 15 12 10 7"/><line x1="15" y1="12" x2="3" y2="12"/></svg>
</button>
</form>

<div class="foot">New here? <a href="/plans">Create account</a></div>
</div>

<script>
const eye=document.getElementById('eye');
const pw=document.getElementById('p');
eye.addEventListener('click',()=>{
const t=pw.type==='password'?'text':'password';
pw.type=t;
eye.style.stroke=t==='text'?'#7dd3fc':'#38bdf8';
});

document.getElementById('f').addEventListener('submit',async(e)=>{
e.preventDefault();
const err=document.getElementById('err');
const btn=document.getElementById('sb');
err.classList.remove('on');
btn.disabled=true;btn.firstChild.textContent='Signing in...';
const p=document.getElementById('p').value;
try{
const r=await fetch('/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:p})});
const d=await r.json();
if(d.status==='ok')window.location.href=d.redirect||'/dashboard';
else{err.textContent=d.error||'Login Failed';err.classList.add('on')}
}catch(ex){err.textContent='Network Error';err.classList.add('on')}
btn.disabled=false;btn.firstChild.textContent='Login';
});
</script>
</body>
</html>
"""



# ==================== PLANS ====================
PLANS_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Pricing - SHAPPNO LV UP</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:radial-gradient(ellipse at top,#0a1020 0%,#000 55%);padding-bottom:60px}
.head{display:flex;align-items:center;justify-content:space-between;padding:18px 22px;border-bottom:1px solid var(--line);max-width:1400px;margin:0 auto}
.logo{display:flex;align-items:center;gap:10px;font-family:'Orbitron',sans-serif;font-size:14px;font-weight:700;letter-spacing:2px}
.logo .lm{width:36px;height:36px;background:linear-gradient(135deg,#38bdf8,#0284c7);border-radius:10px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:16px;box-shadow:0 0 20px rgba(56,189,248,0.5)}
.wrap{max-width:1200px;margin:0 auto;padding:44px 22px 0}
.t{text-align:center;font-family:'Orbitron',sans-serif;font-size:30px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:10px}
.sub{text-align:center;font-size:11px;color:var(--mut);letter-spacing:4px;text-transform:uppercase;margin-bottom:14px;font-weight:600}
.note{text-align:center;font-size:12px;color:#7a8ba0;max-width:640px;margin:0 auto 40px;line-height:1.6;padding:12px 18px;background:rgba(56,189,248,0.05);border:1px solid rgba(56,189,248,0.15);border-radius:10px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:20px}
@media(max-width:700px){.grid{grid-template-columns:1fr}}

.pc{background:var(--card);border:1.5px solid var(--line2);border-radius:20px;padding:36px 24px 24px;position:relative;transition:all 0.3s;display:flex;flex-direction:column}
.pc.blue{border-color:rgba(56,189,248,0.45)}
.pc.blue:hover{border-color:#38bdf8;box-shadow:0 0 40px rgba(56,189,248,0.25);transform:translateY(-4px)}
.pc.purple{border-color:rgba(139,92,246,0.5)}
.pc.purple:hover{border-color:#8b5cf6;box-shadow:0 0 40px rgba(139,92,246,0.3);transform:translateY(-4px)}
.pc.gold{border-color:rgba(245,158,11,0.5)}
.pc.gold:hover{border-color:#f59e0b;box-shadow:0 0 40px rgba(245,158,11,0.25);transform:translateY(-4px)}
.ribbon{position:absolute;top:-12px;right:22px;background:linear-gradient(135deg,#8b5cf6,#6d28d9);color:#fff;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.5px;padding:6px 14px;border-radius:20px;text-transform:uppercase;box-shadow:0 4px 20px rgba(139,92,246,0.5)}
.pi{width:70px;height:70px;margin:0 auto 22px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.pc.blue .pi{background:rgba(56,189,248,0.08);border:1.5px solid rgba(56,189,248,0.35);color:#38bdf8}
.pc.purple .pi{background:rgba(139,92,246,0.08);border:1.5px solid rgba(139,92,246,0.4);color:#a78bfa}
.pc.gold .pi{background:rgba(245,158,11,0.08);border:1.5px solid rgba(245,158,11,0.4);color:#fbbf24}
.pi svg{width:30px;height:30px}
.pn{text-align:center;font-family:'Orbitron',sans-serif;font-size:24px;font-weight:700;letter-spacing:6px;margin-bottom:16px;color:#fff}
.pl{display:flex;justify-content:center;align-items:center;gap:12px;margin-bottom:8px}
.op{font-family:'Inter',sans-serif;font-size:16px;font-weight:700;color:var(--dim);text-decoration:line-through}
.deal{background:#dc2626;color:#fff;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.5px;padding:3px 9px;border-radius:5px}
.pm{text-align:center;font-family:'Orbitron',sans-serif;font-size:52px;font-weight:900;letter-spacing:-1px;margin-bottom:30px;line-height:1;color:#fff}
.pm .cur{font-size:30px;font-weight:700;vertical-align:top;line-height:1;display:inline-block;margin-right:2px}
.feats{list-style:none;margin-bottom:26px;flex:1}
.feats li{display:flex;align-items:flex-start;gap:12px;padding:8px 0;font-size:14px;color:#d8d8dd;line-height:1.45;font-weight:500}
.feats li .ic{flex-shrink:0;width:18px;height:18px;display:flex;align-items:center;justify-content:center;margin-top:2px;color:#22c55e}
.feats li .ic svg{width:15px;height:15px}
.bb{width:100%;padding:15px;border-radius:12px;font-family:'Orbitron',sans-serif;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;border:none;cursor:pointer;transition:all 0.25s;color:#fff}
.pc.blue .bb{background:linear-gradient(135deg,#38bdf8,#0284c7);box-shadow:0 6px 24px rgba(56,189,248,0.3)}
.pc.purple .bb{background:linear-gradient(135deg,#8b5cf6,#7c3aed);box-shadow:0 6px 24px rgba(139,92,246,0.35)}
.pc.gold .bb{background:linear-gradient(135deg,#f59e0b,#d97706);box-shadow:0 6px 24px rgba(245,158,11,0.3);color:#000}
.an{text-align:center;font-size:11px;color:var(--dim);margin-top:12px;letter-spacing:0.5px;font-weight:500}
.flink{text-align:center;margin-top:36px;font-size:13px;color:var(--mut)}
.flink a{color:#38bdf8;text-decoration:none;font-weight:700}
</style>
</head>
<body>
<div class="head">
<div class="logo"><span class="lm">S</span><span>SHAPPNO LV UP</span></div>
<a href="/login" style="color:#fff;text-decoration:none;font-size:13px;font-weight:700">Login →</a>
</div>
<div class="wrap">
<div class="t">Choose Your Plan</div>
<div class="sub">Works On All Servers</div>
<div class="note">All plans work globally across every Free Fire server &mdash; IND, BD, EUROPE, SG, TH, PH, VN, MY, ID, HK, TW and more. Price shown in USD.</div>
<div class="grid" id="grid"></div>
<div class="flink">Already Have An Account? <a href="/login">Sign In</a></div>
</div>
<script>
const SVG={
check:'__SVG_CHECK__',
bolt:'__SVG_BOLT__',
star:'__SVG_STAR__',
crown:'__SVG_CROWN__'
};
const PLANS=[
{id:'starting',name:'STARTING',style:'blue',icon:'bolt',hours:24,slots:3,price:'1',old:'2',pop:false},
{id:'basic',name:'BASIC',style:'purple',icon:'star',hours:48,slots:3,price:'2',old:'4',pop:true},
{id:'premium',name:'PREMIUM',style:'gold',icon:'crown',hours:72,slots:4,price:'2.5',old:'6',pop:false}
];
const TG='shappno_04xx';

function feat(p){
const d=p.hours>=24?Math.round(p.hours/24)+' Day'+(p.hours>=48?'s':''):p.hours+' Hours';
const sp=p.id==='premium'?'Fastest Leveling Speed Available':'Fast Leveling Performance';
const off=p.id==='premium'?'Runs 24/7 &mdash; No Need To Stay Online':'Runs While You Are Offline';
return[
{ic:'check',txt:'Access To The Panel For '+d},
{ic:'check',txt:sp},
{ic:'check',txt:'Run Multiple Accounts At Once'},
{ic:'check',txt:'Restart & Manage Accounts Anytime'},
{ic:'check',txt:off},
{ic:'check',txt:'Telegram Payment Support & Quick Help'},
{ic:'check',txt:p.slots+' Concurrent Account'+(p.slots>1?'s':'')}
];
}

function render(){
const g=document.getElementById('grid');
let h='';
PLANS.forEach(p=>{
let fh='';
feat(p).forEach(f=>{
fh+='<li><span class="ic">'+SVG.check+'</span><span>'+f.txt+'</span></li>';
});
h+='<div class="pc '+p.style+'">';
if(p.pop)h+='<div class="ribbon">Most Popular</div>';
h+='<div class="pi">'+SVG[p.icon]+'</div>';
h+='<div class="pn">'+p.name+'</div>';
h+='<div class="pl"><span class="op">$'+p.old+'</span><span class="deal">Deal</span></div>';
h+='<div class="pm"><span class="cur">$</span>'+p.price+'</div>';
h+='<ul class="feats">'+fh+'</ul>';
h+='<button class="bb" onclick="buy(\\''+p.id+'\\')">Buy '+p.name+'</button>';
h+='<div class="an">Instant Activation After Payment</div>';
h+='</div>';
});
g.innerHTML=h;
}

function buy(id){
const p=PLANS.find(x=>x.id===id);
let m='Hi, I Want To Buy The '+p.name+' Plan.\\n\\nPlan: $'+p.price+'\\nDuration: '+p.hours+' Hours\\nSlots: '+p.slots+'\\n\\nPlease Send Payment Details.';
window.open('https://t.me/'+TG+'?text='+encodeURIComponent(m),'_blank');
}
render();
</script>
</body>
</html>
"""

PLANS_HTML = PLANS_HTML.replace("__SVG_CHECK__", _icon("check", "#22c55e", 15).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_BOLT__", _icon("bolt_fill", "currentColor", 30).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_STAR__", _icon("star_fill", "currentColor", 30).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_CROWN__", _icon("crown_fill", "currentColor", 30).replace('"', '\\"'))



# ==================== EXPIRED ====================
EXPIRED_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Plan Expired - SHAPPNO LV UP</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{display:flex;align-items:center;justify-content:center;padding:24px;background:radial-gradient(ellipse at top,#200a0a 0%,#000 60%)}
.wrap{width:100%;max-width:460px;text-align:center}
.ic{width:84px;height:84px;border-radius:50%;background:rgba(239,68,68,0.08);border:1.5px solid var(--red);display:inline-flex;align-items:center;justify-content:center;margin-bottom:24px;color:var(--red)}
h1{font-family:'Orbitron',sans-serif;font-size:26px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px}
p{font-size:14px;color:var(--mut);line-height:1.7;margin-bottom:30px}
.br{display:flex;flex-direction:column;gap:10px;max-width:300px;margin:0 auto}
.b{display:block;padding:14px;border-radius:10px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;text-decoration:none;text-align:center;transition:all 0.2s;border:none;cursor:pointer}
.b1{background:linear-gradient(135deg,#38bdf8,#0284c7);color:#fff}
.b1:hover{box-shadow:0 8px 28px rgba(56,189,248,0.5)}
.b2{background:transparent;border:1px solid var(--line2);color:var(--mut)}
.b2:hover{border-color:var(--red);color:var(--red)}
</style>
</head>
<body>
<div class="wrap">
<div class="ic">""" + _icon("warn", "currentColor", 40) + """</div>
<h1>Plan Expired</h1>
<p>Your Plan Has Ended And All Bots Have Been Stopped.<br>To Renew, Contact @shappno_04xx On Telegram.</p>
<div class="br">
<a class="b b1" href="/plans">Renew Plan</a>
<a class="b b2" href="/logout">Logout</a>
</div>
</div>
</body>
</html>
"""


# ==================== DASHBOARD (Part A: CSS) ====================
DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>Dashboard - SHAPPNO LV UP</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:radial-gradient(ellipse at top,#0a1020 0%,#000 55%);padding-bottom:80px;overflow-x:hidden}
*{-webkit-tap-highlight-color:transparent}

.top{position:sticky;top:0;z-index:50;background:rgba(0,0,0,0.9);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.top-in{max-width:1200px;margin:0 auto;padding:12px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}
.logo{display:flex;align-items:center;gap:10px;font-family:'Orbitron',sans-serif;font-size:12px;font-weight:800;letter-spacing:2px;color:#fff}
.logo img{
  width:36px;height:36px;border-radius:50%;
  object-fit:cover;
  border:2px solid #38bdf8;
  box-shadow:0 0 12px rgba(56,189,248,0.7), 0 0 24px rgba(56,189,248,0.4);
  animation:dglow 2s ease-in-out infinite alternate;
}
@keyframes dglow{
  0%{box-shadow:0 0 12px rgba(56,189,248,0.7),0 0 24px rgba(56,189,248,0.4)}
  100%{box-shadow:0 0 20px rgba(56,189,248,1),0 0 40px rgba(56,189,248,0.7)}
}

.meta{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.mi{display:flex;flex-direction:column;gap:1px;padding:3px 9px;border-left:2px solid #38bdf8}
.mi .l{font-size:8px;color:var(--mut);letter-spacing:1.2px;text-transform:uppercase;font-weight:800;font-family:'Orbitron',sans-serif}
.mi .v{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;white-space:nowrap}
.act{display:flex;gap:5px}
.bs{padding:8px 12px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;border-radius:8px;cursor:pointer;text-decoration:none;border:1px solid transparent;display:inline-flex;align-items:center;justify-content:center;gap:4px;transition:all 0.2s;white-space:nowrap}
.bw{background:#38bdf8;color:#000}
.bw:hover{opacity:0.88}
.bg{background:transparent;border-color:var(--line2);color:var(--mut)}
.bg:hover{border-color:var(--red);color:var(--red)}

.main{max-width:1200px;margin:0 auto;padding:18px 14px 80px}
.grid{display:grid;grid-template-columns:1fr;gap:14px}

.cc{
  position:relative;
  background:linear-gradient(145deg,#0b1220 0%,#080c14 100%);
  border:1px solid #1a2740;
  border-radius:16px;
  overflow:hidden;
  transition:border-color 0.25s, box-shadow 0.25s;
}
.cc:hover{border-color:#1e3a5f;box-shadow:0 0 0 1px rgba(56,189,248,0.08), 0 8px 32px rgba(0,0,0,0.5)}

.tagline{padding:14px 16px 10px;display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.pill{
  display:inline-flex;align-items:center;gap:6px;
  background:rgba(255,255,255,0.03);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:20px;
  padding:5px 12px;
  font-family:'Orbitron',sans-serif;
  font-size:9px;font-weight:700;
  letter-spacing:1.2px;
  text-transform:uppercase;
  color:#d0d5dd;
}
.pill.uid{font-family:'JetBrains Mono',monospace;letter-spacing:0.4px;font-size:10px}
.pill svg{width:11px;height:11px;opacity:0.75}
.pill.mode-br{background:rgba(56,189,248,0.1);border-color:rgba(56,189,248,0.4);color:#38bdf8}
.pill.mode-lw{background:rgba(139,92,246,0.1);border-color:rgba(139,92,246,0.4);color:#a78bfa}

.status-top{
  display:inline-flex;align-items:center;gap:5px;
  background:rgba(34,197,94,0.12);
  border:1px solid rgba(34,197,94,0.5);
  border-radius:20px;
  padding:5px 12px;
  font-family:'Orbitron',sans-serif;
  font-size:9px;font-weight:800;
  letter-spacing:1.2px;
  text-transform:uppercase;
  color:#22c55e;
  white-space:nowrap;
  margin-left:auto;
}
.status-top .dot{width:6px;height:6px;border-radius:50%;background:#22c55e;box-shadow:0 0 6px #22c55e;animation:pl 1.4s infinite}
.status-top.paused{background:rgba(138,138,149,0.12);border-color:rgba(138,138,149,0.4);color:#8a8a95}
.status-top.paused .dot{background:#8a8a95;box-shadow:none;animation:none}
.status-top.match{background:rgba(245,158,11,0.12);border-color:rgba(245,158,11,0.5);color:#f59e0b}
.status-top.match .dot{background:#f59e0b;box-shadow:0 0 6px #f59e0b}
.status-top.online{background:rgba(56,189,248,0.12);border-color:rgba(56,189,248,0.5);color:#38bdf8}
.status-top.online .dot{background:#38bdf8;box-shadow:0 0 6px #38bdf8}

.acc-head{
  display:flex;align-items:center;gap:12px;
  padding:14px 16px;
  background:linear-gradient(135deg,rgba(56,189,248,0.08),rgba(56,189,248,0.02));
  border-top:1px solid rgba(56,189,248,0.1);
  border-bottom:1px solid rgba(56,189,248,0.1);
}
.avatar{
  width:48px;height:48px;border-radius:11px;
  background:linear-gradient(135deg,#1e3a5f,#0f1e33);
  border:1px solid rgba(56,189,248,0.3);
  display:flex;align-items:center;justify-content:center;
  font-family:'Orbitron',sans-serif;
  font-weight:900;font-size:19px;color:#fff;
  flex-shrink:0;
  box-shadow:inset 0 0 16px rgba(56,189,248,0.1);
}
.hinfo{flex:1;min-width:0}
.hinfo h3{
  font-family:'Orbitron',sans-serif;
  font-size:14px;font-weight:800;
  letter-spacing:0.3px;
  color:#fff;
  margin-bottom:3px;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}
.hinfo p{
  font-family:'JetBrains Mono',monospace;
  font-size:10px;color:#7c869a;
  letter-spacing:0.3px;
  display:flex;align-items:center;gap:5px;
}
.uid-copy{
  background:rgba(56,189,248,0.1);
  border:1px solid rgba(56,189,248,0.3);
  border-radius:5px;
  padding:2px 5px;
  cursor:pointer;
  display:inline-flex;align-items:center;justify-content:center;
  transition:all 0.2s;
}
.uid-copy:hover{background:rgba(56,189,248,0.2);border-color:#38bdf8}
.uid-copy svg{width:10px;height:10px;stroke:#38bdf8}
.lvl-badge{
  background:rgba(56,189,248,0.12);
  border:1px solid rgba(56,189,248,0.45);
  border-radius:8px;
  padding:6px 11px;
  font-family:'Orbitron',sans-serif;
  font-size:11px;font-weight:800;
  letter-spacing:0.8px;
  color:#38bdf8;
  white-space:nowrap;
  flex-shrink:0;
}

.cd{padding:12px 16px;border-bottom:1px solid rgba(255,255,255,0.05);display:grid;grid-template-columns:1fr 1fr;gap:8px 22px}
@media(max-width:560px){.cd{grid-template-columns:1fr}}
.row{display:flex;align-items:center;gap:7px;font-size:12px;min-width:0}
.row .k{color:var(--mut);font-size:9px;font-weight:800;letter-spacing:1.3px;text-transform:uppercase;min-width:76px;font-family:'Orbitron',sans-serif}
.row .v{color:#fff;font-weight:700;font-family:'JetBrains Mono',monospace;font-size:11px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}

.timerow{padding:9px 16px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;align-items:center;gap:7px;font-size:10px;color:var(--mut);font-family:'JetBrains Mono',monospace}
.td{width:4px;height:4px;border-radius:50%;background:#fff;opacity:0.5}

/* PROGRESS BAR */
.progress-box{
  padding:14px 16px;
  border-bottom:1px solid rgba(255,255,255,0.05);
  background:rgba(0,0,0,0.2);
}
.progress-head{
  display:flex;justify-content:space-between;align-items:center;
  margin-bottom:10px;font-size:11px;font-weight:800;
  font-family:'Orbitron',sans-serif;letter-spacing:1px;text-transform:uppercase;
}
.progress-head .l{color:#fff}
.progress-head .r{color:#38bdf8;font-family:'JetBrains Mono',monospace;font-size:12px}
.progress-track{
  width:100%;height:14px;
  background:#0a0a0a;
  border-radius:8px;
  overflow:hidden;
  position:relative;
  border:1px solid #1a2740;
}
.progress-fill{
  height:100%;
  background:linear-gradient(90deg,#38bdf8,#7dd3fc,#38bdf8);
  border-radius:8px;
  transition:width 0.6s ease;
  box-shadow:0 0 12px rgba(56,189,248,0.6);
  position:relative;
  overflow:hidden;
}
.progress-fill::after{
  content:'';
  position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.4),transparent);
  animation:shine 2s infinite;
}
@keyframes shine{0%{transform:translateX(-100%)}100%{transform:translateX(100%)}}
.progress-nums{
  display:flex;justify-content:space-between;
  margin-top:7px;font-size:10px;
  color:#7c869a;font-family:'JetBrains Mono',monospace;font-weight:600;
}
.progress-nums .need{color:#f59e0b}

.statrow{display:grid;grid-template-columns:1fr 1fr 1fr;border-bottom:1px solid rgba(255,255,255,0.05);background:rgba(0,0,0,0.25)}
.sc{padding:12px 6px;text-align:center;border-right:1px solid rgba(255,255,255,0.05)}
.sc:last-child{border-right:none}
.sc .l{font-size:8px;color:var(--mut);letter-spacing:1.3px;text-transform:uppercase;font-weight:800;margin-bottom:5px;font-family:'Orbitron',sans-serif}
.sc .v{font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:800;color:#fff;word-break:break-all}
.sc .v.g{color:#22c55e}
@media(max-width:400px){.sc .v{font-size:12px}}

/* 4 BUTTONS IN ONE ROW */
.acc-actions{
  display:grid;
  grid-template-columns:1fr 1fr 1fr 1fr;
  gap:8px;
  padding:12px 14px 14px;
}
.acc-actions button{
  padding:11px 6px;
  background:#1c1c1e;
  border:1px solid #2a2a2e;
  border-radius:10px;
  color:#fff;
  font-family:'Orbitron',sans-serif;
  font-size:9px;
  font-weight:800;
  letter-spacing:0.8px;
  text-transform:uppercase;
  cursor:pointer;
  transition:all 0.18s;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  gap:4px;
  min-width:0;
}
.acc-actions button:hover{background:#242428;border-color:#3a3a40}
.acc-actions button svg{width:14px;height:14px;flex-shrink:0}
.acc-actions button:disabled{opacity:0.5;cursor:not-allowed}
.btn-pause{color:#f59e0b}
.btn-pause:hover{border-color:#f59e0b!important;background:rgba(245,158,11,0.08)!important}
.btn-pause svg{stroke:#f59e0b}
.btn-restart{color:#38bdf8}
.btn-restart:hover{border-color:#38bdf8!important;background:rgba(56,189,248,0.08)!important}
.btn-restart svg{stroke:#38bdf8}
.btn-refresh{color:#22c55e}
.btn-refresh:hover{border-color:#22c55e!important;background:rgba(34,197,94,0.08)!important}
.btn-refresh svg{stroke:#22c55e}
.btn-delete{color:#ef4444;border-color:rgba(239,68,68,0.4)!important;background:rgba(239,68,68,0.05)!important}
.btn-delete:hover{border-color:#ef4444!important;background:rgba(239,68,68,0.12)!important}
.btn-delete svg{stroke:#ef4444}
@media(max-width:400px){
  .acc-actions{gap:5px;padding:10px 10px 12px}
  .acc-actions button{padding:9px 3px;font-size:8px;gap:3px}
  .acc-actions button svg{width:12px;height:12px}
}

.empty{text-align:center;padding:60px 20px;color:var(--mut)}
.empty .big{display:flex;justify-content:center;margin-bottom:12px;opacity:0.25}
.empty .big svg{width:44px;height:44px}

.conf{position:fixed;inset:0;background:rgba(0,0,0,0.88);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;z-index:200;padding:18px}
.conf.on{display:flex}
.conf-box{background:#141414;border:1px solid #262626;border-radius:16px;padding:22px;max-width:400px;width:100%;font-family:'Inter',sans-serif}
.conf-head{font-size:16px;font-weight:700;color:#fff;margin-bottom:14px;text-align:center}
.conf-msg{font-size:13px;line-height:1.65;color:#a8a8a8;text-align:center;margin-bottom:22px}
.conf-msg b{color:#38bdf8;font-weight:800}
.conf-btns{display:flex;gap:10px}
.conf-btns button{flex:1;padding:13px 10px;border-radius:10px;font-family:'Inter',sans-serif;font-size:13px;font-weight:700;cursor:pointer;border:none;transition:all 0.2s}
.conf-yes{background:#38bdf8;color:#000}
.conf-yes:hover{background:#7dd3fc}
.conf-no{background:#1c1c1e;color:#fff;border:1px solid #2a2a2e!important}
.conf-no:hover{background:#242428}

.mtop{position:fixed;inset:0;background:rgba(0,0,0,0.88);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;z-index:300;padding:18px}
.mtop.on{display:flex}
.mbox{background:#141414;border:1px solid #262626;border-radius:18px;padding:22px;max-width:440px;width:100%;position:relative;font-family:'Inter',sans-serif}
.mh-row{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:22px}
.mh-row h3{font-size:17px;font-weight:700;color:#fff;letter-spacing:0.2px}
.mclose{width:34px;height:34px;border-radius:50%;border:1px solid #2a2a2a;background:transparent;color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.mclose:hover{background:#1e1e1e}
.mclose svg{width:16px;height:16px;stroke:#fff;fill:none;stroke-width:2}
.micon{width:56px;height:56px;margin:0 auto 16px;display:flex;align-items:center;justify-content:center}
.micon svg{width:56px;height:56px;stroke:#fff;fill:none;stroke-width:1.5}
.mtitle{text-align:center;font-size:19px;font-weight:800;color:#fff;margin-bottom:12px;letter-spacing:0.3px}
.mtext{text-align:center;font-size:13px;line-height:1.65;color:#a8a8a8;margin-bottom:20px}
.mbtn{width:100%;padding:14px;border-radius:10px;background:#fff;color:#000;border:none;font-family:'Inter',sans-serif;font-size:14px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;text-decoration:none}
.mbtn:hover{background:#e5e5e5}
</style>
</head>


<body>

<div class="top">
<div class="top-in">
<div class="logo">
<img src="https://files.catbox.moe/1o431f.jpg" alt="Logo">
<span>SHAPPNO LV UP</span>
</div>
<div class="meta">
<div class="mi"><span class="l">User</span><span class="v" id="ui-u">{{USERNAME}}</span></div>
<div class="mi"><span class="l">Time</span><span class="v" id="ui-t">--</span></div>
<div class="mi"><span class="l">Slots</span><span class="v" id="ui-s">0/0</span></div>
</div>
<div class="act">
<a class="bs bw" href="/add-new-job">+ Add New Job</a>
<a class="bs bg" href="/logout">Logout</a>
</div>
</div>
</div>

<div class="main">
<div class="grid" id="grid"></div>
</div>

<div class="conf" id="cm">
<div class="conf-box">
<div class="conf-head" id="cm-t">Confirm</div>
<div class="conf-msg" id="cm-m">Are You Sure?</div>
<div class="conf-btns">
<button class="conf-yes" id="cm-y">Yes</button>
<button class="conf-no" id="cm-n">No</button>
</div>
</div>
</div>

<div class="mtop" id="maint">
<div class="mbox">
<div class="mh-row">
<h3>Important Update</h3>
<button class="mclose" onclick="document.getElementById('maint').classList.remove('on')"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
</div>
<div class="micon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="8 12 11 15 16 9"/></svg></div>
<div class="mtitle" id="notif-title">Important Update</div>
<div class="mtext" id="notif-text">Loading...</div>
<a class="mbtn" href="https://t.me/shappno_04xx" target="_blank">Chat Now</a>
</div>
</div>

<script>
const SVG={
pause:'__SVG_PAUSE__',
play:'__SVG_PLAY__',
trash:'__SVG_TRASH__',
refresh:'__SVG_REFRESH__',
restart:'__SVG_RESTART__',
globe:'__SVG_GLOBE__',
id:'__SVG_ID__',
warn:'__SVG_WARN__',
bolt:'__SVG_BOLT__',
copy:'__SVG_COPY__',
crown:'__SVG_CROWN__'
};

const LEVELS = {
    1: 0, 2: 48, 3: 202, 4: 544, 5: 1012, 6: 1844, 7: 2792, 8: 3800,
    9: 4870, 10: 6004, 11: 7192, 12: 8448, 13: 9776, 14: 11140, 15: 12566,
    16: 14060, 17: 15610, 18: 17224, 19: 18902, 20: 20632, 21: 22424,
    22: 24728, 23: 26192, 24: 28166, 25: 30200, 26: 32294, 27: 34448,
    28: 37804, 29: 41174, 30: 44870, 31: 48852, 32: 53334, 33: 58566,
    34: 64096, 35: 69994, 36: 76460, 37: 83108, 38: 91128, 39: 99322,
    40: 108092, 41: 120144, 42: 133266, 43: 147472, 44: 162760, 45: 179126,
    46: 196572, 47: 215368, 48: 235516, 49: 257010, 50: 279860, 51: 304056,
    52: 348318, 53: 394982, 54: 444044, 55: 495508, 56: 549364, 57: 633756,
    58: 721744, 59: 813336, 60: 908522, 61: 1041438, 62: 1180352, 63: 1325256,
    64: 1476184, 65: 1634300, 66: 1840946, 67: 2056594, 68: 2281242, 69: 2514880,
    70: 2757530, 71: 3059506, 72: 3372284, 73: 3699456, 74: 4041030, 75: 4397020,
    76: 4829104, 77: 5282204, 78: 5756304, 79: 6251404, 80: 6767504, 81: 7381324,
    82: 8043154, 83: 8752952, 84: 9510808, 85: 10316638, 86: 11277190, 87: 12360748,
    88: 13360304, 89: 14482858, 90: 15659418, 91: 17026708, 92: 18453688, 93: 19941280,
    94: 21488570, 95: 23095858, 96: 24763138, 97: 26490138, 98: 28277708, 99: 30124996,
    100: 32032284,
};

function showConfirm(title,msg,yesText,noText){
return new Promise(resolve=>{
document.getElementById('cm-t').textContent=title;
document.getElementById('cm-m').innerHTML=msg;
document.getElementById('cm-y').textContent=yesText||'Yes';
document.getElementById('cm-n').textContent=noText||'No';
document.getElementById('cm-n').style.display='';
document.getElementById('cm').classList.add('on');
const clean=()=>{
document.getElementById('cm').classList.remove('on');
document.getElementById('cm-y').onclick=null;
document.getElementById('cm-n').onclick=null;
};
document.getElementById('cm-y').onclick=()=>{clean();resolve(true)};
document.getElementById('cm-n').onclick=()=>{clean();resolve(false)};
});
}

async function delAcc(uid){
const ok=await showConfirm('Delete Account','Please Confirm That You Are Deleting Your Account.','Yes, Delete','No, Cancel');
if(!ok)return;
try{
  const r = await fetch('/api/account/delete',{
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({uid, keep_in_file:false})
  });
  const d = await r.json();
  // Force dashboard refresh after short delay (allow server to clean up)
  setTimeout(()=>{ fetchS(); }, 800);
  setTimeout(()=>{ fetchS(); }, 2000);
}catch(e){
  try{ await fetchS(); }catch(_){}
}
}

async function pauseAcc(uid){
try{await fetch('/api/account/pause',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid})});fetchS()}catch(e){}
}
async function resumeAcc(uid){
try{await fetch('/api/account/resume',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid})});fetchS()}catch(e){}
}

/* RESTART with 2 min countdown */
const restartCooldowns = {};
async function restartAcc(uid,btn){
const now = Date.now();
const cd = restartCooldowns[uid] || 0;
if(now < cd) return;
restartCooldowns[uid] = now + 120000;
if(btn){
  btn.disabled = true;
  let remain = 120;
  const orig = btn.innerHTML;
  const tick = setInterval(()=>{
    remain--;
    if(remain <= 0){
      clearInterval(tick);
      btn.disabled = false;
      btn.innerHTML = orig;
      restartCooldowns[uid] = 0;
      return;
    }
    const m = Math.floor(remain/60);
    const s = remain % 60;
    btn.innerHTML = SVG.restart + ' ' + m + ':' + String(s).padStart(2,'0');
  },1000);
}
try{
  await fetch('/api/account/delete',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid, keep_in_file:true})});
  await new Promise(r=>setTimeout(r,1500));
  await fetch('/api/account/restart',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid})});
  await fetchS();
}catch(e){}
}

/* REFRESH — pull fresh data from API immediately, 3s cooldown */
const refreshCooldowns = {};
async function refreshAcc(uid,btn){
const now = Date.now();
const cd = refreshCooldowns[uid] || 0;
if(now < cd) return;
refreshCooldowns[uid] = now + 3000;
if(btn){
  btn.disabled = true;
  const orig = btn.innerHTML;
  btn.innerHTML = SVG.refresh + ' ...';
  setTimeout(()=>{
    btn.disabled = false;
    btn.innerHTML = orig;
    refreshCooldowns[uid] = 0;
  }, 2500);
}
try{
  await fetch('/api/account/resume',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid})});
  await fetchS();
}catch(e){
  try{ await fetchS(); }catch(_){}
}
}

function esc(s){if(s==null)return'';return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}
function ago(ts){
if(!ts)return'--';
const s=Math.floor(Date.now()/1000-ts);
if(s<5)return'Just Now';
if(s<60)return s+'s Ago';
if(s<3600)return Math.floor(s/60)+'m Ago';
if(s<86400)return Math.floor(s/3600)+'h Ago';
return Math.floor(s/86400)+'d Ago'
}

/* Timer in 2h 20m format (hours + minutes) */
function fmtLeft(s){
if(s<=0)return'Expired';
const d=Math.floor(s/86400);
const h=Math.floor((s%86400)/3600);
const m=Math.floor((s%3600)/60);
if(d>0)return d+'d '+h+'h '+m+'m';
if(h>0)return h+'h '+m+'m';
return m+'m';
}

let liveSecondsLeft = 0;
setInterval(()=>{
if(liveSecondsLeft > 0){
  liveSecondsLeft--;
  document.getElementById('ui-t').textContent = fmtLeft(liveSecondsLeft);
}
},1000);

/* UID copy — fixed for all browsers */
function copyUID(uid,el){
  const doCopy = (text) => {
    if(navigator.clipboard && window.isSecureContext){
      return navigator.clipboard.writeText(text);
    } else {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.left = '-9999px';
      document.body.appendChild(ta);
      ta.select();
      try{document.execCommand('copy')}catch(e){}
      document.body.removeChild(ta);
      return Promise.resolve();
    }
  };
  doCopy(uid).then(()=>{
    const orig = el.innerHTML;
    el.innerHTML = '<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>';
    setTimeout(()=>{el.innerHTML = orig}, 1000);
  }).catch(()=>{});
}


function render(data){
const g=document.getElementById('grid');
const a=data.accounts||[];
const slots=data.slots||0;
if(data.expired){window.location.href='/expired';return}

let h='';

a.forEach(acc=>{
const gained=acc.gained_exp||0;
const isPaused=acc.status==='PAUSED';
const isMatch=acc.status==='IN_MATCH';
const nickname=esc(acc.nickname||'Player');
const initial=nickname.charAt(0).toUpperCase()||'P';
const uid=esc(acc.uid);
const region=esc(acc.region||'IND');
const mode=(acc.mode||'LW').toUpperCase();
const modeCls=mode==='BR'?'pill mode-br':'pill mode-lw';
const modeLabel=mode==='BR'?'BATTLE ROYALE':'LONE WOLF';
const currentExp = acc.current_exp || 0;
const level = acc.level || 1;
const nextLevel = level + 1;
const baseExp = LEVELS[level] || 0;
const nextExp = LEVELS[nextLevel] || (baseExp + 10000);
const needExp = nextExp - baseExp;
const haveExp = currentExp - baseExp;
const pct = Math.min(100, Math.max(0, (haveExp / needExp) * 100));
const remainExp = Math.max(0, nextExp - currentExp);

let statusLabel, statusCls;
if(isPaused){statusLabel='PAUSED';statusCls='status-top paused'}
else if(isMatch){statusLabel='IN MATCH';statusCls='status-top match'}
else if(acc.status==='ONLINE'){statusLabel='ONLINE';statusCls='status-top online'}
else {statusLabel='LIVE';statusCls='status-top'}

h+='<div class="cc">';

h+='<div class="tagline">';
h+='<span class="'+modeCls+'">'+SVG.bolt+' '+modeLabel+'</span>';
h+='<span class="'+statusCls+'"><span class="dot"></span>'+statusLabel+'</span>';
h+='</div>';

h+='<div class="acc-head">';
h+='<div class="avatar">'+initial+'</div>';
h+='<div class="hinfo"><h3>'+nickname+'</h3><p>UID: '+uid+' <span class="uid-copy" onclick="copyUID(\\''+uid+'\\',this)" title="Copy UID">'+SVG.copy+'</span></p></div>';
h+='<div class="lvl-badge">Lv.'+level+'</div>';
h+='</div>';

h+='<div class="cd">';
h+='<div class="row"><span class="k">Created</span><span class="v">'+ago(acc.created_at)+'</span></div>';
h+='<div class="row"><span class="k">Nickname</span><span class="v">'+nickname+'</span></div>';
h+='<div class="row"><span class="k">Region</span><span class="v">'+region+'</span></div>';
h+='<div class="row"><span class="k">Updated</span><span class="v">'+ago(acc.last_update)+'</span></div>';
h+='</div>';

// Progress Bar
h+='<div class="progress-box">';
h+='<div class="progress-head">';
h+='<span class="l">Level '+level+' &rarr; L'+(level+1)+'</span>';
h+='<span class="r">'+pct.toFixed(1)+'%</span>';
h+='</div>';
h+='<div class="progress-track"><div class="progress-fill" style="width:'+pct+'%"></div></div>';
h+='<div class="progress-nums">';
h+='<span>'+haveExp+' / '+needExp+' EXP</span>';
h+='<span class="need">'+remainExp+' EXP needed</span>';
h+='</div>';
h+='</div>';

h+='<div class="statrow">';
h+='<div class="sc"><div class="l">EXP</div><div class="v">'+(acc.current_exp||0).toLocaleString()+'</div></div>';
h+='<div class="sc"><div class="l">Initial</div><div class="v">'+(acc.initial_exp||0).toLocaleString()+'</div></div>';
h+='<div class="sc"><div class="l">Gained</div><div class="v g">+'+gained.toLocaleString()+'</div></div>';
h+='</div>';

// 4 buttons in one row
h+='<div class="acc-actions">';
if(isPaused){
  h+='<button class="btn-pause" onclick="resumeAcc(\\''+uid+'\\')">'+SVG.play+' ON</button>';
} else {
  h+='<button class="btn-pause" onclick="pauseAcc(\\''+uid+'\\')">'+SVG.pause+' PAUSE</button>';
}
h+='<button class="btn-restart" onclick="restartAcc(\\''+uid+'\\',this)">'+SVG.restart+' RESTART</button>';
h+='<button class="btn-refresh" onclick="refreshAcc(\\''+uid+'\\',this)">'+SVG.refresh+' REFRESH</button>';
h+='<button class="btn-delete" onclick="delAcc(\\''+uid+'\\')">'+SVG.trash+' DELETE</button>';
h+='</div>';

h+='</div>';
});

if(a.length===0){
h='<div class="empty"><div class="big">'+SVG.warn+'</div><p>No Accounts Yet. Click <b>+ Add New Job</b> To Start.</p></div>'
}

g.innerHTML=h;
document.getElementById('ui-u').textContent=data.username||'{{USERNAME}}';
liveSecondsLeft = data.seconds_left || 0;
document.getElementById('ui-t').textContent=fmtLeft(liveSecondsLeft);
document.getElementById('ui-s').textContent=a.length+'/'+slots
}

async function fetchS(){
try{
const r=await fetch('/api/stats');
if(r.status===401){window.location.href='/login';return}
const d=await r.json();
render(d)
}catch(e){}
}

async function loadNotif(){
  try{
    const r = await fetch('/api/notification');
    const d = await r.json();
    if(d.status==='ok' && d.text){
      document.getElementById('notif-text').textContent = d.text;
      document.getElementById('notif-title').textContent = 'Important Update';
    }
  }catch(e){}
}

document.getElementById('maint').classList.add('on');
document.getElementById('maint').addEventListener('click',e=>{
if(e.target.id==='maint')document.getElementById('maint').classList.remove('on');
});

loadNotif();
fetchS();
setInterval(fetchS, 240000);
</script>
</body>
</html>
"""

DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_PAUSE__", _icon("pause", "currentColor", 14).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_PLAY__", _icon("play", "currentColor", 14).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_TRASH__", _icon("trash", "currentColor", 14).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_REFRESH__", _icon("refresh", "currentColor", 14).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_RESTART__", _icon("restart", "currentColor", 14).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_GLOBE__", _icon("globe", "currentColor", 11).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_ID__", _icon("id", "currentColor", 11).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_WARN__", _icon("warn", "currentColor", 44).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_BOLT__", _icon("bolt", "currentColor", 11).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_COPY__", _icon("copy", "currentColor", 10).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_CROWN__", _icon("crown_fill", "#f59e0b", 16).replace('"', '\\"'))


# ==================== ADD NEW JOB ====================
ADD_NEW_JOB_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Add New Job - SHAPPNO LV UP</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',system-ui,sans-serif;background:#000;color:#fff;min-height:100vh;-webkit-font-smoothing:antialiased}
.wrap{max-width:720px;margin:0 auto;padding:0 18px 80px}
.top{position:sticky;top:0;z-index:50;background:rgba(0,0,0,0.95);backdrop-filter:blur(14px);border-bottom:1px solid #1a1a1a;padding:14px 0;margin-bottom:28px}
.top-in{max-width:720px;margin:0 auto;padding:0 18px;display:flex;align-items:center;gap:12px}
.back{background:transparent;border:1px solid #2a2a2a;color:#fff;width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none;transition:all 0.2s;flex-shrink:0}
.back:hover{border-color:#38bdf8;background:#0c1a24}
.back svg{width:18px;height:18px;stroke:#fff;fill:none;stroke-width:2.5}
.ttl h1{font-size:17px;font-weight:800;letter-spacing:1px;margin:0 0 2px;text-transform:uppercase}
.ttl p{font-size:10px;color:#666;letter-spacing:2px;text-transform:uppercase;margin:0;font-weight:600}
.note{background:#0a0a0a;border:1px solid #1a1a1a;border-radius:10px;padding:14px 16px;font-size:12px;color:#888;line-height:1.6;margin-bottom:24px}
.note strong{color:#fff}
.sec{margin-bottom:28px}
.sec-title{font-size:10px;color:#666;letter-spacing:2px;text-transform:uppercase;font-weight:800;margin-bottom:12px;display:flex;align-items:center;gap:8px}
.sec-title::before{content:'';width:3px;height:12px;background:#38bdf8;border-radius:2px}
.modes{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:520px){.modes{grid-template-columns:1fr}}
.mode{border:1.5px solid #1e1e1e;background:#0a0a0a;border-radius:14px;padding:20px 18px;cursor:pointer;transition:all 0.2s;position:relative;overflow:hidden}
.mode:hover{border-color:#3a3a3a;background:#111}
.mode.on{border-color:#38bdf8;background:#0c1a24}
.mode .icn{width:44px;height:44px;border-radius:11px;border:1.5px solid #2a2a2a;display:flex;align-items:center;justify-content:center;margin-bottom:14px;transition:all 0.2s}
.mode.on .icn{border-color:#38bdf8;background:#38bdf8}
.mode.on .icn svg{stroke:#000}
.mode .icn svg{width:22px;height:22px;stroke:#fff;fill:none;stroke-width:2;transition:all 0.2s}
.mode h3{font-size:15px;font-weight:800;letter-spacing:0.5px;margin:0 0 6px}
.mode p{font-size:12px;color:#888;line-height:1.5;margin:0}
.mode .tag{position:absolute;top:14px;right:14px;font-size:9px;font-weight:800;letter-spacing:1.2px;padding:4px 8px;border-radius:6px;text-transform:uppercase;border:1px solid #2a2a2a;color:#666;font-family:'JetBrains Mono',monospace}
.mode.on .tag{border-color:#38bdf8;color:#38bdf8}
.tabs{display:flex;gap:4px;background:#0a0a0a;padding:4px;border-radius:12px;margin-bottom:18px;border:1px solid #1a1a1a;flex-wrap:wrap}
.tb{flex:1;min-width:100px;padding:11px;text-align:center;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;border-radius:9px;cursor:pointer;color:#666;border:none;background:transparent;transition:all 0.2s;font-family:'Inter',sans-serif}
.tb.on{background:#38bdf8;color:#000}
.field{margin-bottom:18px}
.field label{display:block;font-size:10px;color:#666;letter-spacing:1.5px;text-transform:uppercase;font-weight:800;margin-bottom:8px}
.field input,.field textarea{width:100%;background:#0a0a0a;border:1.5px solid #1e1e1e;border-radius:12px;padding:15px 16px;color:#fff;font-size:14px;font-family:'JetBrains Mono',monospace;outline:none;transition:all 0.2s;letter-spacing:0.3px;resize:none}
.field input:focus,.field textarea:focus{border-color:#38bdf8;background:#0c1a24}
.field input::placeholder,.field textarea::placeholder{color:#3a3a3a;font-family:'Inter',sans-serif}
.err{background:#1a0a0a;border:1px solid #4a1a1a;color:#ff4444;padding:12px 14px;border-radius:10px;font-size:13px;margin-bottom:16px;display:none;line-height:1.5}
.err.on{display:block}
.err strong{color:#ff6666}
.info{background:#0a1a2a;border:1px solid #1a3a5a;color:#38bdf8;padding:12px 14px;border-radius:10px;font-size:13px;margin-bottom:16px;display:none;line-height:1.5}
.info.on{display:block}
.submit{width:100%;padding:16px;border-radius:12px;background:#38bdf8;color:#000;border:none;font-family:'Inter',sans-serif;font-size:13px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer;transition:all 0.2s;margin-top:8px}
.submit:hover{background:#7dd3fc}
.submit:disabled{opacity:0.5;cursor:not-allowed}
.result{background:#0a1a0a;border:1px solid #1a4a1a;border-radius:12px;padding:18px;margin-bottom:24px;display:none}
.result.on{display:block}
.result h3{color:#4ade80;font-size:13px;font-weight:800;letter-spacing:1px;text-transform:uppercase;margin:0 0 14px;display:flex;align-items:center;gap:8px}
.result .row{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #142a14;font-size:12px}
.result .row:last-child{border:none}
.result .k{color:#666;font-weight:600;font-size:11px;letter-spacing:1px;text-transform:uppercase}
.result .v{color:#fff;font-family:'JetBrains Mono',monospace;font-weight:700}
.hide{display:none!important}
.badge{display:inline-block;padding:3px 8px;border-radius:5px;font-size:9px;font-weight:800;letter-spacing:1px;text-transform:uppercase;font-family:'JetBrains Mono',monospace}
.badge.br{background:rgba(56,189,248,0.15);color:#38bdf8;border:1px solid rgba(56,189,248,0.3)}
.badge.lw{background:rgba(139,92,246,0.15);color:#a78bfa;border:1px solid rgba(139,92,246,0.3)}
.status-row{display:flex;align-items:center;gap:8px;padding:10px 14px;background:#0a0a0a;border:1px solid #1a1a1a;border-radius:10px;margin-bottom:16px;font-size:12px;color:#888}
.status-row .dot{width:8px;height:8px;border-radius:50%;background:#555;flex-shrink:0}
.status-row .dot.on{background:#22c55e;box-shadow:0 0 8px #22c55e}
.status-row .dot.err{background:#ef4444;box-shadow:0 0 8px #ef4444}
.status-row .dot.wait{background:#f59e0b;box-shadow:0 0 8px #f59e0b}
.bulk-info{background:#0a0a0a;border:1px solid #1a1a1a;border-radius:10px;padding:14px 16px;font-size:12px;color:#a8a8a8;line-height:1.7;margin-bottom:14px}
.bulk-info strong{color:#f59e0b;font-weight:800;letter-spacing:1px;text-transform:uppercase;font-size:11px;font-family:'Orbitron',sans-serif}
.bulk-info span{font-family:'JetBrains Mono',monospace;color:#7dd3fc;font-size:11px}
.bulk-preview{margin-top:14px;padding:14px 16px;background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.3);border-radius:10px}
.bulk-preview-title{font-family:'Orbitron',sans-serif;font-size:10px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:#22c55e;margin-bottom:6px}
.bulk-preview-count{font-family:'JetBrains Mono',monospace;font-size:14px;color:#fff;font-weight:700}
</style>
</head>
<body>
<div class="top">
<div class="top-in">
<a href="/dashboard" class="back">
<svg viewBox="0 0 24 24"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
</a>
<div class="ttl">
<h1>Add New Job</h1>
<p>Configure &amp; Start Bot</p>
</div>
</div>
</div>
<div class="wrap">
<div class="note">
<strong>Auto Mode Switch:</strong> Battle Royale accounts that reach Level 3 will switch to Lone Wolf automatically. Lone Wolf accounts that drop below Level 3 will switch to Battle Royale.
</div>

<div class="status-row">
<span class="dot" id="api-dot"></span>
<span id="api-status">Checking BR API status...</span>
</div>

<div id="result" class="result"></div>
<div id="err" class="err"></div>
<div id="info" class="info"></div>

<form id="form">
<div class="sec">
<div class="sec-title">Select Mode</div>
<div class="modes">
<div class="mode" data-mode="BR" id="m-br">
<div class="icn"><svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>
<h3>Battle Royale</h3>
<p>Level 1-2 accounts only. Farm EXP fast to unlock Lone Wolf.</p>
<div class="tag">Lvl 1-2</div>
</div>
<div class="mode" data-mode="LW" id="m-lw">
<div class="icn"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/><line x1="2" y1="12" x2="22" y2="12"/></svg></div>
<h3>Lone Wolf</h3>
<p>Level 3+ accounts only. Long-session high EXP farming.</p>
<div class="tag">Lvl 3+</div>
</div>
</div>
</div>

<div class="sec">
<div class="sec-title">Account Credentials</div>
<div class="tabs">
<button type="button" class="tb on" data-t="guest" onclick="sw('guest')">UID + Password</button>
<button type="button" class="tb" data-t="token" onclick="sw('token')">Access Token</button>
<button type="button" class="tb" data-t="bulk" onclick="sw('bulk')" id="tabBulk" style="display:none">VIP Bulk Upload</button>
</div>
<div id="fg">
<div class="field">
<label>Free Fire UID</label>
<input type="text" id="uid" placeholder="Enter your numeric UID" autocomplete="off" inputmode="numeric">
</div>
<div class="field">
<label>Password</label>
<input type="text" id="password" placeholder="Enter your account password" autocomplete="off">
</div>
</div>
<div id="ft" class="hide">
<div class="field">
<label>Access Token</label>
<textarea id="token" rows="4" placeholder="Paste your access token here"></textarea>
</div>
</div>
<div id="fb" class="hide">
<div class="bulk-info">
<strong>Upload .txt or .json file</strong><br>
<span>.txt format: uid:password per line</span><br>
<span>.json format: [{"uid":"...","password":"..."}]</span>
</div>
<input type="file" id="bulkFile" accept=".txt,.json" style="width:100%;padding:14px;background:#0a0a0a;border:1.5px dashed rgba(245,158,11,0.5);border-radius:12px;color:#fff;cursor:pointer;font-family:'Inter',sans-serif;font-size:13px">
<div class="bulk-preview" id="bulkPreview" style="display:none">
<div class="bulk-preview-title">Preview</div>
<div class="bulk-preview-count" id="bulkCount">0 accounts found</div>
</div>
</div>
</div>

<button type="submit" class="submit" id="btn">Start Job</button>
</form>
</div>


<script>
var MODE = null;
var TAB = 'guest';
var BULK_ACCOUNTS = [];

function sw(t){
    TAB = t;
    document.querySelectorAll('.tb').forEach(function(el){el.classList.toggle('on', el.dataset.t === t);});
    document.getElementById('fg').classList.toggle('hide', t !== 'guest');
    document.getElementById('ft').classList.toggle('hide', t !== 'token');
    document.getElementById('fb').classList.toggle('hide', t !== 'bulk');
}

(async function checkVip(){
    try{
        const r = await fetch('/api/stats');
        const d = await r.json();
        if(d.is_vip){
            document.getElementById('tabBulk').style.display = '';
        }
    }catch(e){}
})();

document.getElementById('bulkFile')?.addEventListener('change', async function(e){
    const f = e.target.files[0];
    if(!f){BULK_ACCOUNTS=[];document.getElementById('bulkPreview').style.display='none';return}
    const text = await f.text();
    BULK_ACCOUNTS = [];
    try{
        const j = JSON.parse(text);
        if(Array.isArray(j)){
            BULK_ACCOUNTS = j.map(x=>{
                if(typeof x === 'string') return {uid: x.split(':')[0], password: x.split(':')[1]};
                return {uid: String(x.uid||x.UID||''), password: String(x.password||x.pass||'')};
            }).filter(x=>x.uid && x.password);
        } else if(typeof j === 'object'){
            BULK_ACCOUNTS = Object.entries(j).map(([k,v])=>({uid:k, password:v}));
        }
    }catch(ex){
        BULK_ACCOUNTS = text.split(/\\r?\\n/).map(l=>l.trim()).filter(l=>l && !l.startsWith('#')).map(l=>{
            const parts = l.split(':');
            return {uid: parts[0]?.trim(), password: parts[1]?.trim()};
        }).filter(x=>x.uid && x.password);
    }
    document.getElementById('bulkCount').textContent = BULK_ACCOUNTS.length + ' accounts found';
    document.getElementById('bulkPreview').style.display = BULK_ACCOUNTS.length > 0 ? 'block' : 'none';
});

document.querySelectorAll('.mode').forEach(function(el){
    el.addEventListener('click', function(){
        document.querySelectorAll('.mode').forEach(function(x){x.classList.remove('on');});
        el.classList.add('on');
        MODE = el.dataset.mode;
    });
});

function setApi(status, text, cls){
    var dot = document.getElementById('api-dot');
    dot.className = 'dot' + (cls ? ' ' + cls : '');
    document.getElementById('api-status').textContent = text;
}

async function checkApiStatus(){
    try{
        var r = await fetch('/api/br-status');
        var d = await r.json();
        if(d.ok){
            setApi('ok', 'BR API Online (' + d.latency + 'ms)', 'on');
        } else {
            setApi('err', 'BR API Offline', 'err');
        }
    }catch(e){
        setApi('err', 'BR API Unreachable', 'err');
    }
}

checkApiStatus();
setInterval(checkApiStatus, 30000);

function showErr(msg){
    var el = document.getElementById('err');
    el.innerHTML = '<strong>Error:</strong> ' + msg;
    el.classList.add('on');
    document.getElementById('info').classList.remove('on');
}

function clearMsgs(){
    document.getElementById('err').classList.remove('on');
    document.getElementById('info').classList.remove('on');
}

document.getElementById('form').addEventListener('submit', async function(e){
    e.preventDefault();
    clearMsgs();
    var resEl = document.getElementById('result');
    var btn = document.getElementById('btn');
    resEl.classList.remove('on');

    if(!MODE){
        showErr('Select a mode: Choose Battle Royale or Lone Wolf.');
        return;
    }

    if(TAB === 'bulk'){
        if(BULK_ACCOUNTS.length === 0){
            showErr('Please upload a file with accounts first.');
            return;
        }
        btn.disabled = true;
        btn.textContent = 'Adding ' + BULK_ACCOUNTS.length + ' accounts...';
        try{
            var r = await fetch('/api/account/bulk-add', {
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body: JSON.stringify({accounts: BULK_ACCOUNTS, mode: MODE})
            });
            var d = await r.json();
            if(d.status === 'ok'){
                resEl.innerHTML =
                    '<h3>Bulk Upload Done</h3>' +
                    '<div class="row"><span class="k">Added</span><span class="v">' + d.added + '</span></div>' +
                    '<div class="row"><span class="k">Failed</span><span class="v">' + d.failed + '</span></div>';
                resEl.classList.add('on');
                BULK_ACCOUNTS = [];
                document.getElementById('bulkFile').value = '';
                document.getElementById('bulkPreview').style.display = 'none';
                setTimeout(function(){ window.location.href = '/dashboard'; }, 2500);
            } else {
                showErr(d.error || 'Bulk add failed');
            }
        }catch(ex){
            showErr('Network error: ' + ex.message);
        }
        btn.disabled = false;
        btn.textContent = 'Start Job';
        return;
    }

    var uid = '', pw = '', token = '';
    if(TAB === 'guest'){
        uid = document.getElementById('uid').value.trim();
        pw = document.getElementById('password').value.trim();
        if(!uid || !pw){ showErr('UID and Password are required.'); return; }
    } else {
        token = document.getElementById('token').value.trim();
        if(!token){ showErr('Access Token is required.'); return; }
    }

    btn.disabled = true;
    btn.textContent = 'Validating...';

    try{
        var payload = {mode: MODE};
        if(TAB === 'guest'){ payload.uid = uid; payload.password = pw; }
        else { payload.token = token; }

        var r = await fetch('/api/account/add-job', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });
        var d = await r.json();

        if(d.status === 'ok'){
            var badge = d.mode === 'BR' ? '<span class="badge br">BR</span>' : '<span class="badge lw">LW</span>';
            resEl.innerHTML =
                '<h3>Job Started</h3>' +
                '<div class="row"><span class="k">Mode</span><span class="v">' + badge + '</span></div>' +
                '<div class="row"><span class="k">Nickname</span><span class="v">' + (d.nickname || '?') + '</span></div>' +
                '<div class="row"><span class="k">Level</span><span class="v">' + (d.level || 1) + '</span></div>' +
                '<div class="row"><span class="k">Region</span><span class="v">' + (d.region || '?') + '</span></div>' +
                '<div class="row"><span class="k">Account ID</span><span class="v">' + (d.account_id || '?') + '</span></div>';
            resEl.classList.add('on');

            if(TAB === 'guest'){
                document.getElementById('uid').value = '';
                document.getElementById('password').value = '';
            } else {
                document.getElementById('token').value = '';
            }
            document.querySelectorAll('.mode').forEach(function(x){x.classList.remove('on');});
            MODE = null;

            setTimeout(function(){ window.location.href = '/dashboard'; }, 2500);
        } else {
            showErr(d.error || 'Unknown error');
        }
    }catch(ex){
        showErr('Network error: ' + ex.message);
    }

    btn.disabled = false;
    btn.textContent = 'Start Job';
});
</script>
</body>
</html>
"""


# ==================== ADMIN LOGIN ====================
ADMIN_LOGIN_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Admin Access</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{display:flex;align-items:center;justify-content:center;padding:24px;background:radial-gradient(ellipse at top,#1a0a1a 0%,#000 60%)}
.wrap{width:100%;max-width:380px}
.badge{text-align:center;margin-bottom:30px}
.badge .ic{display:inline-flex;width:60px;height:60px;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.4);border-radius:14px;align-items:center;justify-content:center;margin-bottom:16px;color:var(--red)}
.badge .ic svg{width:26px;height:26px}
.badge h2{font-family:'Orbitron',sans-serif;font-size:17px;font-weight:800;letter-spacing:2px;text-transform:uppercase}
.badge p{font-size:10px;color:var(--red);margin-top:8px;letter-spacing:3px;text-transform:uppercase;opacity:0.8;font-weight:700}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:28px}
.f{margin-bottom:16px}
.f label{display:block;font-size:10px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:7px}
.f input{width:100%;background:var(--card2);border:1px solid var(--line2);border-radius:10px;padding:12px 14px;color:#fff;font-size:15px;font-family:'Inter',sans-serif;outline:none;transition:border 0.2s}
.f input:focus{border-color:var(--red);box-shadow:0 0 0 3px rgba(239,68,68,0.15)}
.btn{width:100%;background:linear-gradient(135deg,#ef4444,#dc2626);color:#fff;border:none;border-radius:10px;padding:14px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;transition:all 0.2s}
.btn:hover{box-shadow:0 8px 28px rgba(239,68,68,0.45)}
.err{background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);color:var(--red);padding:12px;border-radius:10px;font-size:13px;margin-bottom:16px;display:none}
.err.on{display:block}
</style>
</head>
<body>
<div class="wrap">
<div class="badge">
<div class="ic">""" + _icon("warn", "currentColor", 26) + """</div>
<h2>Admin Access</h2>
<p>Restricted Area</p>
</div>
<div class="card">
<div id="err" class="err"></div>
<form id="f">
<div class="f"><label>Admin Username</label><input type="text" id="u" autocomplete="off" required></div>
<div class="f"><label>Admin Password</label><input type="password" id="p" autocomplete="off" required></div>
<button type="submit" class="btn">Access Panel</button>
</form>
</div>
</div>
<script>
document.getElementById('f').addEventListener('submit',async(e)=>{
e.preventDefault();
const err=document.getElementById('err');
err.classList.remove('on');
const u=document.getElementById('u').value.trim();
const p=document.getElementById('p').value;
try{
const r=await fetch(window.location.pathname,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p})});
const d=await r.json();
if(d.status==='ok')window.location.href=d.redirect;
else{err.textContent=d.error||'Access Denied';err.classList.add('on')}
}catch(ex){err.textContent='Network Error';err.classList.add('on')}
});
</script>
</body>
</html>
"""


# ==================== ADMIN PANEL ====================
ADMIN_PANEL_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Admin Panel - SHAPPNO LV UP</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:#000}
.top{background:rgba(0,0,0,0.95);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:50}
.top-in{max-width:1400px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between}
.logo{display:flex;align-items:center;gap:10px;font-family:'Orbitron',sans-serif;font-size:12px;font-weight:700;letter-spacing:2px}
.lm{width:30px;height:30px;background:linear-gradient(135deg,#ef4444,#b91c1c);color:#fff;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:14px}
.out{background:transparent;border:1px solid var(--line2);color:var(--mut);padding:8px 14px;border-radius:8px;font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;transition:all 0.2s}
.out:hover{border-color:var(--red);color:var(--red)}
.main{max-width:1400px;margin:0 auto;padding:28px 24px 80px}
.st{font-family:'Orbitron',sans-serif;font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:14px;display:flex;align-items:center;gap:10px}
.st::before{content:'';width:3px;height:16px;background:#38bdf8;border-radius:2px}
.panel{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:28px}
.grid4{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px;margin-bottom:18px}
@media(max-width:900px){.grid4{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.grid4{grid-template-columns:1fr}}
.f label{display:block;font-size:10px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px}
.f input,.f select,.f textarea{width:100%;background:var(--card2);border:1px solid var(--line2);border-radius:10px;padding:11px 14px;color:#fff;font-size:14px;font-family:'Inter',sans-serif;outline:none;transition:border 0.2s}
.f input:focus,.f select:focus,.f textarea:focus{border-color:#38bdf8}
.f textarea{resize:vertical;min-height:60px}
.vip-opt{display:flex;align-items:center;gap:10px;padding:12px 14px;background:var(--card2);border:1px solid var(--line2);border-radius:10px;cursor:pointer;user-select:none;transition:all 0.2s}
.vip-opt:hover{border-color:#f59e0b}
.vip-opt input{width:auto;cursor:pointer;accent-color:#f59e0b;width:18px;height:18px;flex-shrink:0}
.vip-opt span{font-size:12px;font-weight:700;color:#f59e0b;letter-spacing:1px;text-transform:uppercase}
.btn{background:linear-gradient(135deg,#38bdf8,#0284c7);color:#fff;border:none;padding:12px 26px;border-radius:10px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;transition:all 0.2s}
.btn:hover{box-shadow:0 8px 24px rgba(56,189,248,0.4)}
.hint{font-size:11px;color:var(--mut);margin-top:10px}
.tw{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;padding:14px 16px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;color:var(--mut);letter-spacing:1.5px;text-transform:uppercase;border-bottom:1px solid var(--line2);background:var(--card2)}
td{padding:14px 16px;border-bottom:1px solid var(--line);vertical-align:middle;color:#fff}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover{background:rgba(255,255,255,0.02)}
.mono{font-family:'JetBrains Mono',monospace;font-size:12px}
.muted{color:var(--mut)}
.badge{display:inline-block;padding:4px 10px;border-radius:6px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1px}
.ba{background:rgba(34,197,94,0.15);color:var(--green);border:1px solid rgba(34,197,94,0.3)}
.be{background:rgba(239,68,68,0.15);color:var(--red);border:1px solid rgba(239,68,68,0.3)}
.bv{background:rgba(245,158,11,0.15);color:#f59e0b;border:1px solid rgba(245,158,11,0.4)}
.acts{display:flex;gap:6px;flex-wrap:wrap}
.mini{background:var(--card2);border:1px solid var(--line2);color:var(--mut);padding:7px 11px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1px;border-radius:6px;cursor:pointer;transition:all 0.15s}
.mini:hover{border-color:#38bdf8;color:#38bdf8}
.mini.danger:hover{border-color:var(--red);color:var(--red)}
.empty{text-align:center;padding:60px 20px;color:var(--mut);font-size:14px}
.toast{position:fixed;bottom:24px;right:24px;background:var(--card2);border:1px solid #38bdf8;color:#fff;padding:14px 20px;border-radius:10px;font-size:13px;font-weight:700;box-shadow:0 8px 32px rgba(0,0,0,0.6);opacity:0;transform:translateY(20px);transition:all 0.3s;pointer-events:none;z-index:200;max-width:360px}
.toast.on{opacity:1;transform:translateY(0)}
.toast.err{border-color:var(--red)}
</style>
</head>
<body>
<div class="top">
<div class="top-in">
<div class="logo"><span class="lm">A</span><span>SHAPPNO LV UP &mdash; ADMIN</span></div>
<a class="out" href="/admin-shappno/logout">Logout</a>
</div>
</div>
<div class="main">


<!-- Notification Settings -->
<div class="st">Website Notification</div>
<div class="panel">
<div class="f" style="margin-bottom:14px">
<label>Notification Text (shown on Home &amp; Dashboard)</label>
<textarea id="notifText" placeholder="Enter notification text...">IND server is disabled — please wait patiently!</textarea>
</div>
<button class="btn" onclick="saveNotif()">Save Notification</button>
<div class="hint">This text will appear on the Home page announcement bar and Dashboard popup.</div>
</div>

<!-- Create User -->
<div class="st">Create User</div>
<div class="panel">
<div class="grid4">
<div class="f"><label>Username</label><input type="text" id="nu" autocomplete="off"></div>
<div class="f"><label>Password</label><input type="text" id="np" autocomplete="off"></div>
<div class="f"><label>Slots (Max 1000)</label><input type="number" id="ns" value="3" min="1" max="1000"></div>
<div class="f"><label>Duration (Hours)</label><input type="number" id="nh" value="24" min="1" max="8760"></div>
</div>
<div class="vip-opt" style="margin-bottom:14px">
<input type="checkbox" id="nvip">
<span>VIP Account (Enables Bulk File Upload)</span>
</div>
<button class="btn" onclick="createU()">Create User</button>
<div class="hint">Timer Starts Immediately Upon Creation.</div>
</div>

<div class="st">All Users</div>
<div class="tw" id="tbl"><div class="empty">Loading...</div></div>
</div>
<div class="toast" id="toast"></div>
<script>
function esc(s){if(s==null)return'';return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}
function toast(msg,err){const t=document.getElementById('toast');t.textContent=msg;t.classList.toggle('err',!!err);t.classList.add('on');setTimeout(()=>t.classList.remove('on'),2600)}
function fmtLeft(exp){const now=Math.floor(Date.now()/1000);const s=exp-now;if(s<=0)return{t:'Expired',e:true};const d=Math.floor(s/86400);const h=Math.floor((s%86400)/3600);const m=Math.floor((s%3600)/60);const sec=Math.floor(s%60);const pad=n=>String(n).padStart(2,'0');let str='';if(d>0)str+=d+'d ';str+=pad(h)+':'+pad(m)+':'+pad(sec);return{t:str,e:false}}
function fmtDate(ts){return new Date(ts*1000).toLocaleString()}
async function saveNotif(){
try{
const t=document.getElementById('notifText').value;
const r=await fetch('/api/admin/set-notification',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:t})});
const d=await r.json();
if(d.status==='ok'){toast('Notification Saved')}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function createU(){
const u=document.getElementById('nu').value.trim();
const p=document.getElementById('np').value.trim();
const s=parseInt(document.getElementById('ns').value);
const h=parseInt(document.getElementById('nh').value);
const vip=document.getElementById('nvip').checked;
if(!u||!p){toast('Username And Password Required',true);return}
if(s<1||s>1000){toast('Slots Must Be 1-1000',true);return}
if(h<1||h>8760){toast('Hours Must Be 1-8760',true);return}
try{
const r=await fetch('/api/admin/create-user',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p,slots:s,hours:h,vip:vip})});
const d=await r.json();
if(d.status==='ok'){toast('User Created: '+u+(vip?' (VIP)':''));document.getElementById('nu').value='';document.getElementById('np').value='';document.getElementById('nvip').checked=false;loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function loadU(){
try{
const r=await fetch('/api/admin/list-users');
const d=await r.json();
if(d.status!=='ok')return;
const users=d.users||[];
const w=document.getElementById('tbl');
if(users.length===0){w.innerHTML='<div class="empty">No Users Yet</div>';return}
let h='<table><thead><tr>';
h+='<th>Username</th><th>Type</th><th>Slots</th><th>Used</th><th>Expires</th><th>Created</th><th>Actions</th>';
h+='</tr></thead><tbody>';
users.forEach(u=>{
const e=fmtLeft(u.expires_at);
const b=e.e?'<span class="badge be">Expired</span>':'<span class="badge ba">'+e.t+'</span>';
const vb=u.is_vip?'<span class="badge bv">VIP</span>':'<span class="badge" style="background:#1a1a22;color:#666;border:1px solid #2a2a2e">Normal</span>';
h+='<tr>';
h+='<td class="mono">'+esc(u.username)+'</td>';
h+='<td>'+vb+'</td>';
h+='<td class="mono">'+u.slots+'</td>';
h+='<td class="mono muted">'+(u.used_slots||0)+'</td>';
h+='<td>'+b+'</td>';
h+='<td class="muted">'+fmtDate(u.created_at)+'</td>';
h+='<td><div class="acts">';
h+='<button class="mini" onclick="ext(\\''+esc(u.username)+'\\',24)">+24H</button>';
h+='<button class="mini" onclick="slot(\\''+esc(u.username)+'\\',10)">+10 Slots</button>';
h+='<button class="mini" onclick="toggleVip(\\''+esc(u.username)+'\\')">'+(u.is_vip?'Remove VIP':'Make VIP')+'</button>';
h+='<button class="mini danger" onclick="delU(\\''+esc(u.username)+'\\')">Delete</button>';
h+='</div></td>';
h+='</tr>'
});
h+='</tbody></table>';
w.innerHTML=h
}catch(e){}
}
async function ext(u,h){
try{
const r=await fetch('/api/admin/extend-time',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,hours:h})});
const d=await r.json();
if(d.status==='ok'){toast('Extended '+u+' By '+h+'h');loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function slot(u,c){
try{
const r=await fetch('/api/admin/add-slot',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,count:c})});
const d=await r.json();
if(d.status==='ok'){toast('Added '+c+' Slot To '+u);loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function toggleVip(u){
try{
const r=await fetch('/api/admin/toggle-vip',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u})});
const d=await r.json();
if(d.status==='ok'){toast('VIP Updated For '+u);loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function delU(u){
if(!confirm('Delete User '+u+'? This Wipes All Their Data.'))return;
try{
const r=await fetch('/api/admin/delete-user',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u})});
const d=await r.json();
if(d.status==='ok'){toast('Deleted '+u);loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function loadNotif(){
try{
const r=await fetch('/api/admin/get-notification');
const d=await r.json();
if(d.status==='ok'){document.getElementById('notifText').value=d.text||''}
}catch(e){}
}
loadNotif();
loadU();
setInterval(loadU,5000);
</script>
</body>
</html>
"""


ALL_TEMPLATES = {
    "home": HOME_HTML,
    "login": LOGIN_HTML,
    "plans": PLANS_HTML,
    "dashboard": DASHBOARD_HTML,
    "expired": EXPIRED_HTML,
    "admin_login": ADMIN_LOGIN_HTML,
    "admin_panel": ADMIN_PANEL_HTML,
}