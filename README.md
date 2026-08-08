# ⚡ Transformer Designer 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Library-Tkinter-blue)
![Status](https://img.shields.io/badge/Status-Development-orange)

> [!IMPORTANT]
> **Transformer Designer** is a desktop application built for Electrical Engineers to automate the complex calculations and physical drafting of power transformers, including core geometry, tank dimensions, and cooling systems.

---

## 🚀 Key Features

*   **📐 Core Design:** Automatically calculates $E_t$ (Voltage per turn), Flux, and Net Iron Area ($A_i$). Supports 2-step and 3-step core geometries with real-time visualization.
*   **🔋 Parameter Optimization:** Inputs for Power (kVA), Frequency, Flux Density, and Current Density to determine the window area ($A_w$) and core dimensions.
*   **📦 Tank Drafting:** Generates the physical layout of the transformer tank based on clearance requirements ($D_{oh}$) and winding dimensions.
*   **🌡️ Cooling Analysis:** Includes a dedicated module to calculate the required number of cooling tubes based on radiation and convection dissipation constants.
*   **🖼️ Dynamic Scaling:** Uses a custom coordinate system to render technical drawings directly onto a Tkinter Canvas with precise dimension markers.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.x |
| **GUI Framework** | Tkinter |
| **Graphics/UI** | PIL (Pillow) |
| **Mathematics** | Math library (Trigonometry & Square roots) |

---

## ⚙️ How It Works

> [!TIP]
> The application follows standard design procedures where the window height ($H_w$) is typically twice the window width ($W_w$), ensuring an optimal balance between copper and iron losses.

1.  **Core Calculation:** Based on the input power, the system uses the formula $E_t = 0.44 \cdot \sqrt{P}$ to initiate the design.
2.  **Step Logic:** It calculates the stack dimensions ($a, b, c$) depending on whether a 2-step or 3-step core is selected.
3.  **Visual Output:** The Canvas draws the Core (Blue), Windings (White), and specific markers for the primary and secondary coils (Red/Blue).
4.  **Cooling Logic:** The `calculate_tubes` function assumes a 1% loss and determines how many 0.025m tubes are needed to maintain safe operating temperatures.

---

## 📺 Project Walkthrough & Demo
I have recorded a detailed technical session explaining the code logic, the mathematical formulas used, and a live demo of the design process.

> [!NOTE]
> **Watch the full engineering breakdown here:**
> ### 🔗 [Transformer Designer: Implementation & Demo on YouTube](https://youtu.be/m-p4YI1Xa8o?si=5umyoavobU65kmyO)

---

## 🚦 Getting Started

### 1. Prerequisites
Ensure you have Python and the Pillow library installed:
```bash
pip install Pillow
