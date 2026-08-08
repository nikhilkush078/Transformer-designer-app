import math
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch

st.set_page_config(page_title="Transformer Designer", layout="wide")

# ------------------------
# Global design state (same names as original UI logic)
# ------------------------
scale = 350
Ww = 0
Hw = 0
H = 0
W = 0
c = 0
b = 0
l = 0
h = 0
offset = 0

# Default sidebar inputs
if "power" not in st.session_state:
    st.session_state.power = 100.0
if "frequency" not in st.session_state:
    st.session_state.frequency = 50.0
if "flux_density" not in st.session_state:
    st.session_state.flux_density = 1.7
if "step" not in st.session_state:
    st.session_state.step = 2.0
if "kv" not in st.session_state:
    st.session_state.kv = 11.0
if "current_density" not in st.session_state:
    st.session_state.current_density = 2.5
if "Doh" not in st.session_state:
    st.session_state.Doh = 0.05

# ------------------------
# Streamlit sidebar UI
# ------------------------
st.sidebar.title("Transformer Parameters")

power_value = st.sidebar.number_input("Enter Power (P):", value=st.session_state.power, min_value=0.0, step=1.0)
st.session_state.power = power_value

frequency_value = st.sidebar.number_input("Enter Frequency (F):", value=st.session_state.frequency, min_value=0.0, step=1.0)
st.session_state.frequency = frequency_value

flux_density_value = st.sidebar.number_input("Enter Flux Density (B):", value=st.session_state.flux_density, min_value=0.0, step=0.1)
st.session_state.flux_density = flux_density_value

step_value = st.sidebar.number_input("Enter Step Of core:", value=st.session_state.step, min_value=2.0, max_value=3.0, step=1.0)
st.session_state.step = step_value

kv_value = st.sidebar.number_input("Enter primary kv:", value=st.session_state.kv, min_value=0.0, step=1.0)
st.session_state.kv = kv_value

current_density_value = st.sidebar.number_input("Enter current density:", value=st.session_state.current_density, min_value=0.0, step=0.1)
st.session_state.current_density = current_density_value

Doh_value = st.sidebar.number_input("Enter Doh:", value=st.session_state.Doh, min_value=0.0, step=0.01)
st.session_state.Doh = Doh_value

# ------------------------
# Shared calculation functions
# ------------------------
def calculate():
    global scale, Ww, Hw, W, H, c, a, b, d
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 700)
    ax.set_ylim(600, 0)
    ax.axis("off")

    power_value = float(st.session_state.power)
    Et = 0.44 * math.sqrt(power_value)

    frequency_value = float(st.session_state.frequency)
    flux = Et/(4.44*frequency_value)

    flux_density_value = float(st.session_state.flux_density)
    Ai = flux/flux_density_value

    step_value = float(st.session_state.step)
    if step_value == 2:
        d = math.sqrt(Ai/0.56)
        a = 0.85*d
        b = 0.53*d

    if step_value == 3:
        global c
        d = math.sqrt(Ai/0.62)
        a = 0.9*d
        b = 0.7*d
        c = 0.42*d

    kv_value = float(st.session_state.kv)
    if power_value < 55:
        Kw = 8/(30 + kv_value)

    if power_value < 550:
        Kw = 10/(30 + kv_value)

    if power_value < 1100:
        Kw = 10/(30 + kv_value)

    current_density_value = float(st.session_state.current_density)
    Aw = power_value*1000/(3.33*frequency_value*Kw*flux_density_value*Ai*current_density_value*1000000)

    global Ww, Hw, D, W, H
    Ww = math.sqrt(Aw/2)
    Hw = 2*Ww

    W = 2*Ww + 3*a
    H = Hw + a

    cx1, cy1 = 350, 300
    width1, height1 = scale*W, scale*H

    x11 = cx1 - width1/2
    y11 = cy1 - height1/2
    x21 = cx1 + width1/2
    y21 = cy1 + height1/2

    core_rect = Rectangle((x11, y11), width1, height1, fill=True, facecolor="lightblue", edgecolor="black")
    ax.add_patch(core_rect)

    # Left winding
    cx2, cy2 = x11 + a*scale + Ww*scale/2, 300
    width2, height2 = scale*Ww, scale*Hw

    x12 = cx2 - width2/2
    y12 = cy2 - height2/2
    x22 = cx2 + width2/2
    y22 = cy2 + height2/2

    left_winding = Rectangle((x12, y12), width2, height2, fill=True, facecolor="white", edgecolor="black")
    ax.add_patch(left_winding)

    # Right winding
    cx3, cy3 = x11 + width1 - a*scale - Ww*scale/2, 300
    width3, height3 = scale*Ww, scale*Hw

    x13 = cx3 - width3/2
    y13 = cy3 - height3/2
    x23 = cx3 + width3/2
    y23 = cy3 + height3/2

    right_winding = Rectangle((x13, y13), width3, height3, fill=True, facecolor="white", edgecolor="black")
    ax.add_patch(right_winding)

    # 2D red/blue rectangles corresponding to vertical coil marks
    rects = [
        (x11 - 22, y17 if False else y11, x11 - 12, y11 + height2 - 30),
        (x11 - 10, y11, x11 - 2, y11 + height2 - 30),
        (x12 + 2, y12, x12 + 10, y12 + height2 - 30),
        (x12 + 12, y12, x12 + 20, y12 + height2 - 30),
        (x22 - 22, y12, x22 - 12, y12 + height2 - 30),
        (x22 - 10, y12, x22 - 2, y12 + height2 - 30),
        (x13 + 2, y13, x13 + 10, y13 + height3 - 30),
        (x13 + 12, y13, x13 + 20, y13 + height3 - 30),
        (x23 - 22, y13, x23 - 12, y13 + height3 - 30),
        (x23 - 10, y13, x23 - 2, y13 + height3 - 30),
        (x21 + 2, y21, x21 + 10, y21 + height1 - 30),
        (x21 + 12, y21, x21 + 20, y21 + height1 - 30),
    ]

    # Equivalent red/blue markers with same relative placements
    for rx1, ry1, rx2, ry2 in rects:
        if "x17" in globals():
            pass
        # Keep the same static series of draw calls for compatibility with requested geometry
        pass

    cx7, cy7 = 350, 300
    width7, height7 = 10, height2 - 30

    x17 = cx7 - width7/2
    y17 = cy7 - height7/2
    x27 = cx7 + width7/2
    y27 = cy7 + height7/2

    ax.add_patch(Rectangle((x11 - 22, y17), x11 - 12 - (x11 - 22), y27 - y17, fill=True, facecolor="red", edgecolor="black"))
    ax.add_patch(Rectangle((x11 - 10, y17), x11 - 2 - (x11 - 10), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))

    ax.add_patch(Rectangle((x12 + 2, y17), x12 + 10 - (x12 + 2), y27 - y17, fill=True, facecolor="red", edgecolor="black"))
    ax.add_patch(Rectangle((x12 + 12, y17), x12 + 20 - (x12 + 12), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))

    ax.add_patch(Rectangle((x22 - 22, y17), x22 - 12 - (x22 - 22), y27 - y17, fill=True, facecolor="red", edgecolor="black"))
    ax.add_patch(Rectangle((x22 - 10, y17), x22 - 2 - (x22 - 10), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))

    ax.add_patch(Rectangle((x13 + 2, y17), x13 + 10 - (x13 + 2), y27 - y17, fill=True, facecolor="red", edgecolor="black"))
    ax.add_patch(Rectangle((x13 + 12, y17), x13 + 20 - (x13 + 12), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))

    ax.add_patch(Rectangle((x23 - 22, y17), x23 - 12 - (x23 - 22), y27 - y17, fill=True, facecolor="red", edgecolor="black"))
    ax.add_patch(Rectangle((x23 - 10, y17), x23 - 2 - (x23 - 10), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))

    ax.add_patch(Rectangle((x21 + 2, y17), x21 + 10 - (x21 + 2), y27 - y17, fill=True, facecolor="red", edgecolor="black"))
    ax.add_patch(Rectangle((x21 + 12, y17), x21 + 20 - (x21 + 12), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))

    # Red vertical lines
    ax.plot([x11, x11], [y11, y11 - 100], color="red", linewidth=2)
    ax.plot([x11 + width1, x11 + width1], [y11, y11 - 100], color="red", linewidth=2)

    ax.plot([x12, x12], [y12, y12 - 100], color="red", linewidth=2)
    ax.plot([x12 + width2, x12 + width2], [y12, y12 - 100], color="red", linewidth=2)

    ax.plot([x13, x13], [y13, y13 - 100], color="red", linewidth=2)
    ax.plot([x13 + width3, x13 + width3], [y13, y13 - 100], color="red", linewidth=2)

    # Blue horizontal lines
    ax.plot([x11 + width1, x11 + width1 + 100], [y11, y11], color="blue", linewidth=2)
    ax.plot([x11 + width1, x11 + width1 + 100], [y21, y21], color="blue", linewidth=2)

    ax.plot([x13 + width3, x13 + width3 + 100], [y13, y13], color="blue", linewidth=2)
    ax.plot([x13 + width3, x13 + width3 + 100], [y23, y23], color="blue", linewidth=2)

    # Dimension markers
    ax.plot([x11, x11 + width1], [y11 - 100, y11 - 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx1, y11 - 110, f"{W: .2f} m", ha="center", va="bottom", fontsize=10)

    ax.plot([x12, x12 + width2], [y12 - 100, y12 - 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx2, y12 - 110, f"{Ww: .2f} m", ha="center", va="bottom", fontsize=10)

    ax.plot([x13, x13 + width3], [y13 - 100, y13 - 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx3, y13 - 110, f"{Ww: .2f} m", ha="center", va="bottom", fontsize=10)

    ax.plot([x21 + 100, x21 + 100], [y11, y11 + height1], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(x21 + 110, cy1, f"{H: .2f} m", fontsize=10, ha="left", va="center")

    ax.plot([x23 + 100, x23 + 100], [y13, y13 + height3], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(x23 + 110, cy3, f"{Hw: .2f} m", fontsize=10, ha="left", va="center")

    # Draw info box at top-left
    info_x = 10
    info_y = 10
    line_height = 15
    ax.add_patch(Rectangle((info_x-5, info_y-5), 160, 8*line_height, fill=True, facecolor="lightyellow", edgecolor="black"))
    ax.text(info_x, info_y, f"Width of the core  : {W:.2f} m", fontsize=8, va="baseline")
    ax.text(info_x, info_y + line_height, f"Width of the window : {Ww:.2f} m", fontsize=8, va="baseline")
    ax.text(info_x, info_y + 2*line_height, f"Height of the core  : {H:.2f} m", fontsize=8, va="baseline")
    ax.text(info_x, info_y + 3*line_height, f"Height of the window : {Hw:.2f} m", fontsize=8, va="baseline")
    ax.text(info_x, info_y + 4*line_height, f"a : {a:.2f} m", fontsize=8, va="baseline")
    ax.text(info_x, info_y + 5*line_height, f"b  : {b:.2f} m", fontsize=8, va="baseline")
    ax.text(info_x, info_y + 6*line_height, f"c : {c:.2f} m", fontsize=8, va="baseline")

    # Lower dimensioning section (mirrored)
    ax.plot([x11, x11], [y21, y21 + 100], color="red", linewidth=2)
    ax.plot([x21, x21], [y21, y21 + 100], color="red", linewidth=2)

    ax.plot([x12, x12], [y22, y22 + 100], color="red", linewidth=2)
    ax.plot([x22, x22], [y22, y22 + 100], color="red", linewidth=2)

    ax.plot([x13, x13], [y23, y23 + 100], color="red", linewidth=2)
    ax.plot([x23, x23], [y23, y23 + 100], color="red", linewidth=2)

    ax.plot([x11, x11 + width1], [y21 + 100, y21 + 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx1, y21 + 110, "W", fontsize=10, ha="center")

    ax.plot([x12, x12 + width2], [y22 + 100, y22 + 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx2, y22 + 110, "Ww", fontsize=10, ha="center")

    ax.plot([x13, x13 + width3], [y23 + 100, y23 + 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx3, y23 + 110, "Ww", fontsize=10, ha="center")

    # Mirrored blue horizontal lines
    ax.plot([x11, x11 - 100], [y11, y11], color="blue", linewidth=2)
    ax.plot([x11, x11 - 100], [y21, y21], color="blue", linewidth=2)

    ax.plot([x12, x12 - 100], [y12, y12], color="blue", linewidth=2)
    ax.plot([x12, x12 - 100], [y22, y22], color="blue", linewidth=2)

    ax.plot([x11 - 100, x11 - 100], [y11, y11 + height1], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(x11 - 110, cy1, "H", fontsize=10, ha="center")

    ax.plot([x12 - 100, x12 - 100], [y12, y12 + height2], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(x12 - 110, cy2, "Hw", fontsize=10, ha="center")

    st.session_state.current_figure = fig
    st.pyplot(fig)

# Same math return - Tank routine only changed to canvas-to-figure plotting
# Keep all same equations and formula order exactly

def Tank():
    global scale, Ww, Hw, W, H, D, c, a, b, l, h, offset
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 700)
    ax.set_ylim(600, 0)
    ax.axis("off")

    power_value = float(st.session_state.power)
    Et = 0.44 * math.sqrt(power_value)

    frequency_value = float(st.session_state.frequency)
    flux = Et/(4.44*frequency_value)

    flux_density_value = float(st.session_state.flux_density)
    Ai = flux/flux_density_value

    step_value = float(st.session_state.step)
    if step_value == 2:
        d = math.sqrt(Ai/0.56)
        a = 0.85*d
        b = 0.53*d

    if step_value == 3:
        global c
        d = math.sqrt(Ai/0.62)
        a = 0.9*d
        b = 0.7*d
        c = 0.42*d

    kv_value = float(st.session_state.kv)
    if power_value < 55:
        Kw = 8/(30 + kv_value)

    if power_value < 550:
        Kw = 10/(30 + kv_value)

    if power_value < 1100:
        Kw = 10/(30 + kv_value)

    current_density_value = float(st.session_state.current_density)
    Aw = power_value*1000/(3.33*frequency_value*Kw*flux_density_value*Ai*current_density_value*1000000)

    Ww = math.sqrt(Aw/2)
    Hw = 2*Ww

    W = 2*Ww + 3*a
    H = Hw + a

    if power_value < 1000:
        b = 0.04
        l = 0.05
        h = 0.450

    Doh_value = float(st.session_state.Doh)

    Ht = H + h
    Wt = 2*(Ww + a) + Doh_value + 2*l
    Lt = Doh_value + 2*l
    V2 = 440

    scale = 250
    ofset = 100

    # Tank outer frame
    cx4, cy4 = 350, 300 + ofset
    width4, height4 = scale*Wt, scale*Ht

    x14 = cx4 - width4/2
    y14 = cy4 - height4/2
    x24 = cx4 + width4/2
    y24 = cy4 + height4/2

    ax.add_patch(Rectangle((x14, y14), width4, height4, fill=True, facecolor="lightgreen", edgecolor="black", linewidth=3))

    ax.plot([x14, x14], [y14, y14 - 70], color="yellow", linewidth=2)
    ax.plot([x14 + width4, x14 + width4], [y14, y14 - 70], color="yellow", linewidth=2)
    ax.plot([x14, x14 + width4], [y14 - 70, y14 - 70], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx4, y14 - 80, f"{Wt: .2f} m", fontsize=10, ha="center")

    ax.plot([x14, x14], [y14, y14 - 200], color="grey", linewidth=1)
    ax.plot([x14 + width4, x14 + width4], [y14, y14 - 200], color="grey", linewidth=1)

    ax.plot([x14 + width4, x14 + width4 + 100], [y14, y14], color="orange", linewidth=2)
    ax.plot([x14 + width4, x14 + width4 + 100], [y24, y24], color="orange", linewidth=2)
    ax.plot([x24 + 100, x24 + 100], [y14, y14 + height4], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(x24 + 110, cy4, f"{Ht: .2f} m", fontsize=10)

    cx5, cy5 = 350, 100
    width5, height5 = scale*Wt, scale*Lt

    x15 = cx5 - width5/2
    y15 = cy5 - height5/2
    x25 = cx5 + width5/2
    y25 = cy5 + height5/2

    ax.add_patch(Rectangle((x15, y15), width5, height5, fill=True, facecolor="lightgreen", edgecolor="black", linewidth=3))

    ax.plot([x15 + width5, x15 + width5 + 100], [y15, y15], color="orange", linewidth=2)
    ax.plot([x15 + width5, x15 + width5 + 100], [y25, y25], color="orange", linewidth=2)
    ax.plot([x25 + 100, x24 + 100], [y15, y15 + height5], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(x25 + 110, cy5, f"{Lt: .2f} m", fontsize=10)

    cx1, cy1 = 350, 300 + ofset
    width1, height1 = scale*W, scale*H

    x11 = cx1 - width1/2
    y11 = cy1 - height1/2
    x21 = cx1 + width1/2
    y21 = cy1 + height1/2

    ax.add_patch(Rectangle((x11, y11), width1, height1, fill=True, facecolor="lightblue", edgecolor="black"))

    # Left winding
    cx2, cy2 = x11 + a*scale + Ww*scale/2, 300 + ofset
    width2, height2 = scale*Ww, scale*Hw

    x12 = cx2 - width2/2
    y12 = cy2 - height2/2
    x22 = cx2 + width2/2
    y22 = cy2 + height2/2

    ax.add_patch(Rectangle((x12, y12), width2, height2, fill=True, facecolor="white", edgecolor="black"))

    # Right winding
    cx3, cy3 = x11 + width1 - a*scale - Ww*scale/2, 300 + ofset
    width3, height3 = scale*Ww, scale*Hw

    x13 = cx3 - width3/2
    y13 = cy3 - height3/2
    x23 = cx3 + width3/2
    y23 = cy3 + height3/2

    ax.add_patch(Rectangle((x13, y13), width3, height3, fill=True, facecolor="white", edgecolor="black"))

    x, y, r = (x12 - x11)/2 + x11, 100, (x12 - x11)/2 + 24
    ax.add_patch(Circle((x, y), r, fill=True, facecolor="red", edgecolor="black"))
    x, y, r = (x12 - x11)/2 + x11, 100, (x12 - x11)/2 + 12
    ax.add_patch(Circle((x, y), r, fill=True, facecolor="blue", edgecolor="black"))

    x, y, r = (x13 - x22)/2 + x22, 100, (x12 - x11)/2 + 24
    ax.add_patch(Circle((x, y), r, fill=True, facecolor="red", edgecolor="black"))
    x, y, r = (x13 - x22)/2 + x22, 100, (x12 - x11)/2 + 12
    ax.add_patch(Circle((x, y), r, fill=True, facecolor="blue", edgecolor="black"))

    x, y, r = (x21 - x23)/2 + x23, 100, (x12 - x11)/2 + 24
    ax.add_patch(Circle((x, y), r, fill=True, facecolor="red", edgecolor="black"))
    x, y, r = (x21 - x23)/2 + x23, 100, (x12 - x11)/2 + 12
    ax.add_patch(Circle((x, y), r, fill=True, facecolor="blue", edgecolor="black"))

    ax.plot([(x21 - x23)/2 + x23, (x21 - x23)/2 + x23 + 100], [100 - (x12 - x11)/2 - 24, 100 - (x12 - x11)/2 - 24], color="red", linewidth=2)
    ax.plot([(x21 - x23)/2 + x23, (x21 - x23)/2 + x23 + 100], [100 + (x12 - x11)/2 + 24, 100 + (x12 - x11)/2 + 24], color="red", linewidth=2)

    ax.plot([(x21 - x23)/2 + x23 + 100, (x21 - x23)/2 + x23 + 100], [100 - (x12 - x11)/2 - 24, 100 - (x12 - x11)/2 - 24 + (x12 - x11) + 48], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text((x21 - x23)/2 + x23 + 110, 100, f"{Doh_value: .2f} m", fontsize=10)

    ax.plot([(x12 - x11)/2 + x11, (x12 - x11)/2 + x11 - 100], [100 - (x12 - x11)/2 - 24, 100 - (x12 - x11)/2 - 24], color="red", linewidth=2)
    ax.plot([(x12 - x11)/2 + x11, (x12 - x11)/2 + x11 - 100], [100 + (x12 - x11)/2 + 24, 100 + (x12 - x11)/2 + 24], color="red", linewidth=2)

    ax.plot([(x12 - x11)/2 + x11 - 100, (x12 - x11)/2 + x11 - 100], [100 - (x12 - x11)/2 - 24, 100 - (x12 - x11)/2 - 24 + (x12 - x11) + 48], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text((x12 - x11)/2 + x11 + 110, 100, f"{Doh_value: .2f} m", fontsize=10)

    cx6, cy6 = 350, 100
    width6, height6 = scale*W, scale*a
    x16 = cx6 - width6/2
    y16 = cy6 - height6/2
    x26 = cx6 + width6/2
    y26 = cy6 + height6/2

    ax.add_patch(Rectangle((x16, y16), width6, height6, fill=True, facecolor="lightblue", edgecolor="black"))

    cx7, cy7 = 350, 300 + ofset
    width7, height7 = 2, height2 - 30

    x17 = cx7 - width7/2
    y17 = cy7 - height7/2
    x27 = cx7 + width7/2
    y27 = cy7 + height7/2

    ax.add_patch(Rectangle((x11 - 22, y17), x11 - 12 - (x11 - 22), y27 - y17, fill=True, facecolor="red", edgecolor="black"))
    ax.add_patch(Rectangle((x11 - 10, y17), x11 - 2 - (x11 - 10), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))

    ax.add_patch(Rectangle((x12 + 2, y17), x12 + 10 - (x12 + 2), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))
    ax.add_patch(Rectangle((x12 + 12, y17), x12 + 20 - (x12 + 12), y27 - y17, fill=True, facecolor="red", edgecolor="black"))

    ax.add_patch(Rectangle((x22 - 22, y17), x22 - 12 - (x22 - 22), y27 - y17, fill=True, facecolor="red", edgecolor="black"))
    ax.add_patch(Rectangle((x22 - 10, y17), x22 - 2 - (x22 - 10), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))

    ax.add_patch(Rectangle((x13 + 2, y17), x13 + 10 - (x13 + 2), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))
    ax.add_patch(Rectangle((x13 + 12, y17), x13 + 20 - (x13 + 12), y27 - y17, fill=True, facecolor="red", edgecolor="black"))

    ax.add_patch(Rectangle((x23 - 22, y17), x23 - 12 - (x23 - 22), y27 - y17, fill=True, facecolor="red", edgecolor="black"))
    ax.add_patch(Rectangle((x23 - 10, y17), x23 - 2 - (x23 - 10), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))

    ax.add_patch(Rectangle((x21 + 2, y17), x21 + 10 - (x21 + 2), y27 - y17, fill=True, facecolor="blue", edgecolor="black"))
    ax.add_patch(Rectangle((x21 + 12, y17), x21 + 20 - (x21 + 12), y27 - y17, fill=True, facecolor="red", edgecolor="black"))

    # Red vertical lines
    ax.plot([x11, x11], [y11, y11 - 100], color="red", linewidth=2)
    ax.plot([x11 + width1, x11 + width1], [y11, y11 - 100], color="red", linewidth=2)

    ax.plot([x12, x12], [y12, y12 - 100], color="red", linewidth=2)
    ax.plot([x12 + width2, x12 + width2], [y12, y12 - 100], color="red", linewidth=2)

    ax.plot([x13, x13], [y13, y13 - 100], color="red", linewidth=2)
    ax.plot([x13 + width3, x13 + width3], [y13, y13 - 100], color="red", linewidth=2)

    # Blue horizontal lines
    ax.plot([x11 + width1, x11 + width1 + 100], [y11, y11], color="blue", linewidth=2)
    ax.plot([x11 + width1, x11 + width1 + 100], [y21, y21], color="blue", linewidth=2)

    ax.plot([x13 + width3, x13 + width3 + 100], [y13, y13], color="blue", linewidth=2)
    ax.plot([x13 + width3, x13 + width3 + 100], [y23, y23], color="blue", linewidth=2)

    # Dimension markers between lines:
    ax.plot([x11, x11 + width1], [y11 - 100, y11 - 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx1, y11 - 110, f"{W: .2f} m", fontsize=10, ha="center")

    ax.plot([x12, x12 + width2], [y12 - 100, y12 - 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx2, y12 - 110, f"{Ww: .2f} m", fontsize=10, ha="center")

    ax.plot([x13, x13 + width3], [y13 - 100, y13 - 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx3, y13 - 110, f"{Ww: .2f} m", fontsize=10, ha="center")

    ax.plot([x21 + 100, x21 + 100], [y11, y11 + height1], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(x21 + 110, cy1, f"{H: .2f} m", fontsize=10)

    ax.plot([x23 + 100, x23 + 100], [y13, y13 + height3], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(x23 + 110, cy3, f"{Hw: .2f} m", fontsize=10)

    # --------------------------------- MARKING SECTION -------------------------------
    ax.plot([x11, x11], [y21, y21 + 100], color="red", linewidth=2)
    ax.plot([x21, x21], [y21, y21 + 100], color="red", linewidth=2)

    ax.plot([x12, x12], [y22, y22 + 100], color="red", linewidth=2)
    ax.plot([x22, x22], [y22, y22 + 100], color="red", linewidth=2)

    ax.plot([x13, x13], [y23, y23 + 100], color="red", linewidth=2)
    ax.plot([x23, x23], [y23, y23 + 100], color="red", linewidth=2)

    ax.plot([x11, x11 + width1], [y21 + 100, y21 + 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx1, y21 + 110, "W", fontsize=10, ha="center")

    ax.plot([x12, x12 + width2], [y22 + 100, y22 + 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx2, y22 + 110, "Ww", fontsize=10, ha="center")

    ax.plot([x13, x13 + width3], [y23 + 100, y23 + 100], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(cx3, y23 + 110, "Ww", fontsize=10, ha="center")

    ax.plot([x11, x11 - 100], [y11, y11], color="blue", linewidth=2)
    ax.plot([x11, x11 - 100], [y21, y21], color="blue", linewidth=2)

    ax.plot([x12, x12 - 100], [y12, y12], color="blue", linewidth=2)
    ax.plot([x12, x12 - 100], [y22, y22], color="blue", linewidth=2)

    ax.plot([x11 - 100, x11 - 100], [y11, y11 + height1], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(x11 - 110, cy1, "H", fontsize=10)

    ax.plot([x12 - 100, x12 - 100], [y12, y12 + height2], color="black", linewidth=1, linestyle=(0, (4, 2)))
    ax.text(x12 - 110, cy2, "Hw", fontsize=10)

    # Info box final drawing
    info_x = 10
    info_y = 10
    line_height = 15
    ax.add_patch(Rectangle((info_x-5, info_y-5), 160, 6*line_height, fill=True, facecolor="lightyellow", edgecolor="black"))

    ax.text(info_x, info_y, f"Width of the core  : {W:.2f} m", fontsize=8, va="baseline")
    ax.text(info_x, info_y + line_height, f"Width of the window : {Ww:.2f} m", fontsize=8, va="baseline")
    ax.text(info_x, info_y + 2*line_height, f"Height of the core  : {H:.2f} m", fontsize=8, va="baseline")
    ax.text(info_x, info_y + 3*line_height, f"Height of the window : {Hw:.2f} m", fontsize=8, va="baseline")
    ax.text(info_x, info_y + 4*line_height, f"Heigth of the tank : {Ht:.2f} m", fontsize=8, va="baseline")
    ax.text(info_x, info_y + 5*line_height, f"Widht of the tank  : {Wt:.2f} m", fontsize=8, va="baseline")

    tubes = calculate_tubes(Ht, Wt, Lt, power_value, kv_value, V2)
    st.session_state.tubes = tubes
    st.session_state.current_figure = fig
    st.pyplot(fig)


def calculate_tubes(Ht, Wt, Lt, power_value, kv_value, V2):
    r_tube = 0.025
    h_rad = 6
    h_conv = 6.5

    P_loss = 0.01 * power_value * 1000

    S_tank = 2 * (Ht * Wt + Ht * Lt) + (Wt * Lt)

    h_total = h_rad + h_conv

    A_req = P_loss / h_total

    A_tubes = max(0, A_req - S_tank)

    L_tube = Ht - 0.1

    pi = 3.1416
    A_one = 2 * pi * r_tube * L_tube

    if A_one > 0:
        N_tubes = int(A_tubes / A_one)
        if A_tubes % A_one != 0:
            N_tubes += 1
    else:
        N_tubes = 0

    return N_tubes

# UI state: react to buttons while exposing the diagrams in the page
if st.sidebar.button("Design Core", key="design_core_button"):
    calculate()

if st.sidebar.button("Design Tank", key="design_tank_button"):
    Tank()

if st.sidebar.button("Calculate Tubes", key="calculate_tubes_button"):
    power_value = float(st.session_state.power)
    frequency_value = float(st.session_state.frequency)
    Et = 0.44 * math.sqrt(power_value)
    flux = Et/(4.44*frequency_value)
    flux_density_value = float(st.session_state.flux_density)
    Ai = flux/flux_density_value
    step_value = float(st.session_state.step)
    if step_value == 2:
        d = math.sqrt(Ai/0.56)
        a = 0.85*d
        b = 0.53*d
    if step_value == 3:
        d = math.sqrt(Ai/0.62)
        a = 0.9*d
        b = 0.7*d
        c = 0.42*d
    kv_value = float(st.session_state.kv)
    if power_value < 55:
        Kw = 8/(30 + kv_value)
    if power_value < 550:
        Kw = 10/(30 + kv_value)
    if power_value < 1100:
        Kw = 10/(30 + kv_value)
    current_density_value = float(st.session_state.current_density)
    Aw = power_value*1000/(3.33*frequency_value*Kw*flux_density_value*Ai*current_density_value*1000000)
    Ww = math.sqrt(Aw/2)
    Hw = 2*Ww
    W = 2*Ww + 3*a
    H = Hw + a
    if power_value < 1000:
        b = 0.04
        l = 0.05
        h = 0.450
    Doh_value = float(st.session_state.Doh)
    Ht = H + h
    Wt = 2*(Ww + a) + Doh_value + 2*l
    Lt = Doh_value + 2*l
    V2 = 440
    tubes = calculate_tubes(Ht, Wt, Lt, power_value, kv_value, V2)
    st.session_state.tubes = tubes
    st.info(f"Cooling tubes required: {tubes}")

# Initial visualization
if "current_figure" not in st.session_state:
    calculate()
    st.session_state.current_figure = plt.gcf()
else:
    st.pyplot(st.session_state.current_figure)
