import tkinter as tk 
import math 
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Transformer Designer")
root.geometry("900x600")

scale = 350
Ww = 0
Hw = 0
H = 0
W = 0
c = 0

#-----------Tank------------

b = 0
l = 0
h = 0
ofset = 0





canvas = tk.Canvas(root, width=700, height=600, bg="white")
canvas.pack(side="right", pady=5, padx=10)



image = Image.open("font_page.png")  # Replace with your image path

# Convert to Tkinter-compatible image
tk_image = ImageTk.PhotoImage(image)

# Add image to canvas
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

       
       
       
# Label for input
# ---------- Input Frame ----------


#calculation of Et 
def calculate():
    canvas.delete("all")
    scale = 350
    power_value = float(power_entry.get())  # get the number from entry
    Et = 0.44 * math.sqrt(power_value)      # calculate
    
    frequency_value = float(frequency.get())
    flux = Et/(4.44*frequency_value)
    
    flux_density_value = float(flux_density.get())
    Ai = flux/flux_density_value
    
    step_value = float(step.get())
    if step_value == 2: 
       d = math.sqrt(Ai/0.56)
       a = 0.85*d
       b = 0.53*d
       
 

       img = Image.open("step_2.png")
       img = img.resize((100, 100))                  
       tk_img = ImageTk.PhotoImage(img)           
       canvas.image = tk_img                       
       canvas.create_image(canvas.winfo_width()-10, 450, anchor="ne", image=tk_img)
       


       
    if step_value == 3: 
       global c 
       d = math.sqrt(Ai/0.62)
       a = 0.9*d
       b = 0.7*d
       c = 0.42*d
       
       img = Image.open("step_3.png")
       img = img.resize((100, 100))                  
       tk_img = ImageTk.PhotoImage(img)           
       canvas.image = tk_img                       
       canvas.create_image(canvas.winfo_width()-10, 450, anchor="ne", image=tk_img)
    
    kv_value = float(kv.get())
    if power_value < 55: 
        Kw = 8/(30 + kv_value)
        
    if power_value < 550: 
        Kw = 10/(30 + kv_value)
    
    if power_value < 1100: 
    
    
        Kw = 10/(30 + kv_value)
        
    
    current_density_value = float(current_density.get())
    Aw = power_value*1000/(3.33*frequency_value*Kw*flux_density_value*Ai*current_density_value*1000000)
    
    global Ww, Hw, D, W, H
    Ww = math.sqrt(Aw/2)
    Hw = 2*Ww 
    
    W = 2*Ww + 3*a
    H = Hw + a
    
    
    print(Ww)
    print(Hw)

    print(W)
    print(H)

    cx1, cy1 = 350, 300
    width1, height1 = scale*W , scale*H

    x11 = cx1 - width1/2
    y11 = cy1 - height1/2
    x21 = cx1 + width1/2
    y21 = cy1 + height1/2

    core_rect = canvas.create_rectangle(x11, y11, x21, y21, fill="lightblue", outline="black")


# -------- Left winding --------
    cx2, cy2 = x11 + a*scale + Ww*scale/2, 300   # center shifted to the left
    width2, height2 = scale*Ww, scale*Hw

    x12 = cx2 - width2/2
    y12 = cy2 - height2/2
    x22 = cx2 + width2/2
    y22 = cy2 + height2/2

    left_winding = canvas.create_rectangle(x12, y12, x22, y22, fill="white", outline="black")


# -------- Right winding --------
    cx3, cy3 = x11 + width1 - a*scale - Ww*scale/2, 300   # center shifted to the right
    width3, height3 = scale*Ww, scale*Hw

    x13 = cx3 - width3/2
    y13 = cy3 - height3/2
    x23 = cx3 + width3/2
    y23 = cy3 + height3/2

    right_winding = canvas.create_rectangle(x13, y13, x23, y23, fill="white", outline="black")
    
    
    cx7, cy7 = 350, 300   # center shifted to the right
    width7, height7 = 10, height2 - 30

    x17 = cx7 - width7/2
    y17 = cy7 - height7/2
    x27 = cx7 + width7/2
    y27 = cy7 + height7/2

    right_winding = canvas.create_rectangle(x11 - 22, y17, x11 - 12 , y27, fill="red", outline="black")
    right_winding = canvas.create_rectangle(x11 - 10, y17, x11 - 2, y27, fill="blue", outline="black")
    
    right_winding = canvas.create_rectangle(x12 + 2, y17, x12 + 10, y27, fill="red", outline="black")
    right_winding = canvas.create_rectangle(x12 + 12, y17, x12 + 20, y27, fill="blue", outline="black")
    
    right_winding = canvas.create_rectangle(x22- 22, y17, x22 - 12 , y27, fill="red", outline="black")
    right_winding = canvas.create_rectangle(x22 - 10, y17, x22 - 2, y27, fill="blue", outline="black")
    
    right_winding = canvas.create_rectangle(x13 + 2, y17, x13 + 10, y27, fill="red", outline="black")
    right_winding = canvas.create_rectangle(x13 + 12, y17, x13 + 20, y27, fill="blue", outline="black")
    
    right_winding = canvas.create_rectangle(x23- 22, y17, x23 - 12 , y27, fill="red", outline="black")
    right_winding = canvas.create_rectangle(x23 - 10, y17, x23 - 2, y27, fill="blue", outline="black")
    
    right_winding = canvas.create_rectangle(x21 + 2, y17, x21 + 10, y27, fill="red", outline="black")
    right_winding = canvas.create_rectangle(x21 + 12, y17, x21 + 20, y27, fill="blue", outline="black")
    
    
    
    # Red vertical lines
    canvas.create_line(x11, y11, x11, y11 - 100, fill="red", width=2)
    canvas.create_line(x11 + width1, y11 , x11 + width1, y11 - 100, fill="red", width=2)

    canvas.create_line(x12, y12, x12, y12 - 100, fill="red", width=2)
    canvas.create_line(x12 + width2, y12, x12 + width2, y12 - 100, fill="red", width=2)

    canvas.create_line(x13, y13, x13, y13 - 100, fill="red", width=2)
    canvas.create_line(x13 + width3, y13, x13 + width3, y13 - 100, fill="red", width=2)

    # Blue horizontal lines
    canvas.create_line(x11 + width1, y11, x11 + width1 + 100, y11, fill="blue", width=2) 
    canvas.create_line(x11 + width1, y21,  x11 + width1 + 100, y21, fill="blue", width=2)

    canvas.create_line(x13 + width3, y13, x13 + width3 + 100 , y13, fill="blue", width=2)
    canvas.create_line(x13 + width3, y23,  x13 + width3 + 100, y23, fill="blue", width=2) 

    # --- Dimension markers between lines ---

    # Vertical line pairs → horizontal dimension lines
    canvas.create_line(x11, y11 - 100, x11 + width1, y11 - 100, fill="black", width=1, dash=(4,2))  # between first and second vertical line
    canvas.create_text(cx1, y11 - 110, text=f"{W: .2f} m", font=("Arial", 10))

    canvas.create_line(x12, y12 - 100, x12 + width2, y12 - 100, fill="black", width=1, dash=(4,2))  # between second and third vertical line
    canvas.create_text(cx2, y12 - 110, text=f"{Ww: .2f} m", font=("Arial", 10))

    canvas.create_line(x13, y13 - 100, x13 + width3, y13 - 100, fill="black", width=1, dash=(4,2))  # between third and fourth vertical line
    canvas.create_text(cx3, y13 - 110, text=f"{Ww: .2f} m", font=("Arial", 10))


    # Horizontal line pairs → vertical dimension lines
    canvas.create_line(x21 + 100, y11, x21 + 100, y11 + height1, fill="black", width=1, dash=(4,2))
    canvas.create_text(x21 + 110, cy1, text=f"{H: .2f} m", font=("Arial", 10))

    canvas.create_line(x23 + 100, y13, x23 + 100, y13 + height3, fill="black", width=1, dash=(4,2))
    canvas.create_text(x23 + 110, cy3, text=f"{Hw: .2f} m", font=("Arial", 10))
    
    

# --- Draw a small info box at top-left ---
    info_x = 10
    info_y = 10
    line_height = 15

    canvas.create_rectangle(info_x-5, info_y-5, 160, info_y + 8*line_height, fill="lightyellow", outline="black")

    # Labels + values
    canvas.create_text(info_x, info_y, anchor="nw", text=f"Width of the core  : {W:.2f} m", font=("Arial", 8), fill="black")
    canvas.create_text(info_x, info_y + line_height, anchor="nw", text=f"Width of the window : {Ww:.2f} m", font=("Arial", 8), fill="black")
    canvas.create_text(info_x, info_y + 2*line_height, anchor="nw", text=f"Height of the core  : {H:.2f} m", font=("Arial", 8), fill="black")
    canvas.create_text(info_x, info_y + 3*line_height, anchor="nw", text=f"Height of the window : {Hw:.2f} m", font=("Arial", 8), fill="black")
    canvas.create_text(info_x, info_y + 4*line_height, anchor="nw", text=f"a : {a:.2f} m", font=("Arial", 8), fill="black")
    canvas.create_text(info_x, info_y + 5*line_height, anchor="nw", text=f"b  : {b:.2f} m", font=("Arial", 8), fill="black")
    canvas.create_text(info_x, info_y + 6*line_height, anchor="nw", text=f"c : {c:.2f} m", font=("Arial", 8), fill="black")





    #------------------------------ MARKING SECTION -------------------------------


    # Red vertical lines (lower side — mirrored)
    canvas.create_line(x11, y21, x11, y21 +100, fill="red", width=2)
    canvas.create_line(x21, y21, x21, y21 + 100, fill="red", width=2)

    canvas.create_line(x12, y22, x12, y22 + 100, fill="red", width=2)
    canvas.create_line(x22, y22, x22, y22 + 100, fill="red", width=2)

    canvas.create_line(x13, y23, x13, y23 + 100, fill="red", width=2)
    canvas.create_line(x23, y23, x23, y23 + 100, fill="red", width=2)

    # Bottom horizontal dimension lines (mirrored)
    canvas.create_line(x11, y21 + 100, x11 + width1, y21 + 100, fill="black", width=1, dash=(4,2))  
    canvas.create_text(cx1, y21 + 110, text="W", font=("Arial", 10))

    canvas.create_line(x12, y22 + 100, x12 + width2, y22 + 100, fill="black", width=1, dash=(4,2))  
    canvas.create_text(cx2, y22 + 110, text="Ww", font=("Arial", 10))

    canvas.create_line(x13, y23 + 100, x13 + width3, y23 + 100, fill="black", width=1, dash=(4,2))  
    canvas.create_text(cx3, y23 + 110, text="Ww", font=("Arial", 10))


    # --- Mirrored blue horizontal lines (left side) ---
    canvas.create_line(x11, y11, x11 - 100, y11, fill="blue", width=2) 
    canvas.create_line(x11, y21, x11 - 100, y21, fill="blue", width=2)

    canvas.create_line(x12, y12, x12 - 100, y12, fill="blue", width=2)
    canvas.create_line(x12, y22, x12 - 100, y22, fill="blue", width=2) 

    # --- Dimension markers for left-side horizontal lines ---
    canvas.create_line(x11 - 100, y11, x11 - 100, y11 + height1, fill="black", width=1, dash=(4,2))  # vertical marker
    canvas.create_text(x11 - 110, cy1, text="H", font=("Arial", 10))

    canvas.create_line(x12 - 100, y12, x12 - 100, y12 + height2, fill="black", width=1, dash=(4,2))  # vertical marker
    canvas.create_text(x12 - 110, cy2, text="Hw", font=("Arial", 10))
    
    
    
    
    
    
    
    
    
    
    
    
def Tank():
    canvas.delete("all")
    scale = 250
    ofset = 100
    power_value = float(power_entry.get())  # get the number from entry
    Et = 0.44 * math.sqrt(power_value)      # calculate
    
    frequency_value = float(frequency.get())
    flux = Et/(4.44*frequency_value)
    
    flux_density_value = float(flux_density.get())
    Ai = flux/flux_density_value
    
    step_value = float(step.get())
    if step_value == 2: 
       d = math.sqrt(Ai/0.56)
       a = 0.85*d
       b = 0.53*d
       
 

       img = Image.open("step_2.png")
       img = img.resize((100, 100))                  
       tk_img = ImageTk.PhotoImage(img)           
       canvas.image = tk_img                       
       canvas.create_image(canvas.winfo_width()-10, 450, anchor="ne", image=tk_img)
       


       
    if step_value == 3: 
       global c 
       d = math.sqrt(Ai/0.62)
       a = 0.9*d
       b = 0.7*d
       c = 0.42*d
       
       img = Image.open("step_3.png")
       img = img.resize((100, 100))                  
       tk_img = ImageTk.PhotoImage(img)           
       canvas.image = tk_img                       
       canvas.create_image(canvas.winfo_width()-10, 450, anchor="ne", image=tk_img)
    
    kv_value = float(kv.get())
    if power_value < 55: 
        Kw = 8/(30 + kv_value)
        
    if power_value < 550: 
        Kw = 10/(30 + kv_value)
    
    if power_value < 1100: 
    
    
        Kw = 10/(30 + kv_value)
        
    
    current_density_value = float(current_density.get())
    Aw = power_value*1000/(3.33*frequency_value*Kw*flux_density_value*Ai*current_density_value*1000000)
    
    global Ww, Hw, D, W, H
    Ww = math.sqrt(Aw/2)
    Hw = 2*Ww 
    
    W = 2*Ww + 3*a
    H = Hw + a
    
    
    print(Ww)
    print(Hw)

    print(W)
    print(H)
    
    if power_value < 1000:
         
        
        b = 0.04
        l = 0.05
        h = 0.450
    
    Doh_value = float(Doh.get())
    
    Ht = H + h 
    Wt = 2*(Ww + a) + Doh_value + 2*l
    Lt = Doh_value + 2*l
    V2 = 440
    
    
    
    
    
# -------- Tank Paramenters --------
    cx4, cy4 = 350, 300 + ofset  # center shifted to the right
    width4, height4 = scale*Wt, scale*Ht

    x14 = cx4 - width4/2
    y14 = cy4 - height4/2
    x24 = cx4 + width4/2
    y24 = cy4 + height4/2

    Tank = canvas.create_rectangle(x14, y14, x24, y24, fill="lightgreen", outline="black", width=3)
    
    canvas.create_line(x14, y14, x14, y14 - 70, fill="yellow", width=2)
    canvas.create_line(x14 + width4, y14 , x14 + width4, y14 - 70, fill="yellow", width=2)
    canvas.create_line(x14, y14 - 70, x14 + width4, y14 - 70, fill="black", width=1, dash=(4,2))  # between first and second vertical line
    canvas.create_text(cx4, y14 - 80, text=f"{Wt: .2f} m", font=("Arial", 10))
    
    canvas.create_line(x14, y14, x14, y14 - 200, fill="grey", width=1)
    canvas.create_line(x14 + width4, y14 , x14 + width4, y14 - 200, fill="grey", width=1)
    
    
    
    
    canvas.create_line(x14 + width4, y14, x14 + width4 + 100, y14, fill="orange", width=2) 
    canvas.create_line(x14 + width4, y24,  x14 + width4 + 100, y24, fill="orange", width=2)
    canvas.create_line(x24 + 100, y14, x24 + 100, y14 + height4, fill="black", width=1, dash=(4,2))
    canvas.create_text(x24 + 110, cy4, text=f"{Ht: .2f} m", font=("Arial", 10))
    
    cx5, cy5 = 350, 100 # center shifted to the right
    width5, height5 = scale*Wt, scale*Lt

    x15 = cx5 - width5/2
    y15 = cy5 - height5/2
    x25 = cx5 + width5/2
    y25 = cy5 + height5/2
    
    tank_top = canvas.create_rectangle(x15, y15, x25, y25, fill="lightgreen", outline="black", width=3)
    
    canvas.create_line(x15 + width5, y15, x15 + width5 + 100, y15, fill="orange", width=2) 
    canvas.create_line(x15 + width5, y25,  x15 + width5 + 100, y25, fill="orange", width=2)
    canvas.create_line(x25 + 100, y15, x24 + 100, y15 + height5, fill="black", width=1, dash=(4,2))
    canvas.create_text(x25 + 110, cy5, text=f"{Lt: .2f} m", font=("Arial", 10))
    
    
    
    
    
    

    cx1, cy1 = 350, 300  + ofset
    width1, height1 = scale*W , scale*H

    x11 = cx1 - width1/2
    y11 = cy1 - height1/2
    x21 = cx1 + width1/2
    y21 = cy1 + height1/2

    core_rect = canvas.create_rectangle(x11, y11, x21, y21, fill="lightblue", outline="black")


# -------- Left winding --------
    cx2, cy2 = x11 + a*scale + Ww*scale/2, 300 + ofset  # center shifted to the left
    width2, height2 = scale*Ww, scale*Hw

    x12 = cx2 - width2/2
    y12 = cy2 - height2/2
    x22 = cx2 + width2/2
    y22 = cy2 + height2/2

    left_winding = canvas.create_rectangle(x12, y12, x22, y22, fill="white", outline="black")


# -------- Right winding --------
    cx3, cy3 = x11 + width1 - a*scale - Ww*scale/2, 300 + ofset  # center shifted to the right
    width3, height3 = scale*Ww, scale*Hw
    
    
    x13 = cx3 - width3/2
    y13 = cy3 - height3/2
    x23 = cx3 + width3/2
    y23 = cy3 + height3/2

    right_winding = canvas.create_rectangle(x13, y13, x23, y23, fill="white", outline="black")
    
    x, y, r = (x12 - x11)/2 + x11, 100, (x12 - x11)/2 + 24 # center (x, y) and radius
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="red", outline="black")
    x, y, r = (x12 - x11)/2 + x11, 100, (x12 - x11)/2 + 12  # center (x, y) and radius
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue", outline="black")
    
    x, y, r = (x13 - x22)/2 + x22, 100, (x12 - x11)/2 + 24 # center (x, y) and radius
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="red", outline="black")
    x, y, r = (x13 - x22)/2 + x22, 100, (x12 - x11)/2 + 12  # center (x, y) and radius
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue", outline="black")
    
    x, y, r = (x21 - x23)/2 + x23, 100, (x12 - x11)/2 + 24 # center (x, y) and radius
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="red", outline="black")
    x, y, r = (x21 - x23)/2 + x23, 100, (x12 - x11)/2 + 12  # center (x, y) and radius
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue", outline="black")
    
    
    canvas.create_line((x21 - x23)/2 + x23, 100 - (x12 - x11)/2 - 24, (x21 - x23)/2 + x23 + 100, 100 - (x12 - x11)/2 - 24, fill="red", width=2)
    canvas.create_line((x21 - x23)/2 + x23, 100 + (x12 - x11)/2 + 24, (x21 - x23)/2 + x23 + 100, 100 + (x12 - x11)/2 + 24, fill="red", width=2)
    
    canvas.create_line((x21 - x23)/2 + x23 + 100, 100 - (x12 - x11)/2 - 24, (x21 - x23)/2 + x23 + 100, 100 - (x12 - x11)/2 - 24 + (x12 - x11) + 48 , fill="black", width=1, dash=(4,2))
    canvas.create_text((x21 - x23)/2 + x23 + 110, 100, text=f"{Doh_value: .2f} m", font=("Arial", 10))
    

    canvas.create_line((x12 - x11)/2 + x11, 100 - (x12 - x11)/2 - 24, (x12 - x11)/2 + x11 - 100, 100 - (x12 - x11)/2 - 24, fill="red", width=2)
    canvas.create_line((x12 - x11)/2 + x11, 100 + (x12 - x11)/2 + 24, (x12 - x11)/2 + x11 - 100, 100 + (x12 - x11)/2 + 24, fill="red", width=2)
    
    canvas.create_line((x12 - x11)/2 + x11 - 100, 100 - (x12 - x11)/2 - 24, (x12 - x11)/2 + x11 - 100, 100 - (x12 - x11)/2 - 24 + (x12 - x11) + 48 , fill="black", width=1, dash=(4,2))
    canvas.create_text((x12 - x11)/2 + x11 + 110, 100, text=f"{Doh_value: .2f} m", font=("Arial", 10))
    
    cx6, cy6 = 350, 100 # center shifted to the right
    width6, height6 = scale*W, scale*a

    x16 = cx6 - width6/2
    y16 = cy6 - height6/2
    x26 = cx6 + width6/2
    y26 = cy6 + height6/2
    
    tank_top_core = canvas.create_rectangle(x16, y16, x26, y26, fill="lightblue", outline="black")

    
    
    
    cx7, cy7 = 350, 300 + + ofset  # center shifted to the right
    width7, height7 = 2, height2 - 30

    x17 = cx7 - width7/2
    y17 = cy7 - height7/2
    x27 = cx7 + width7/2
    y27 = cy7 + height7/2
    
    

    right_winding = canvas.create_rectangle(x11 - 22, y17, x11 - 12 , y27, fill="red", outline="black")
    right_winding = canvas.create_rectangle(x11 - 10, y17, x11 - 2, y27, fill="blue", outline="black")
    
    right_winding = canvas.create_rectangle(x12 + 2, y17, x12 + 10, y27, fill="blue", outline="black")
    right_winding = canvas.create_rectangle(x12 + 12, y17, x12 + 20, y27, fill="red", outline="black")
    
    right_winding = canvas.create_rectangle(x22- 22, y17, x22 - 12 , y27, fill="red", outline="black")
    right_winding = canvas.create_rectangle(x22 - 10, y17, x22 - 2, y27, fill="blue", outline="black")
    
    right_winding = canvas.create_rectangle(x13 + 2, y17, x13 + 10, y27, fill="blue", outline="black")
    right_winding = canvas.create_rectangle(x13 + 12, y17, x13 + 20, y27, fill="red", outline="black")
    
    right_winding = canvas.create_rectangle(x23- 22, y17, x23 - 12 , y27, fill="red", outline="black")
    right_winding = canvas.create_rectangle(x23 - 10, y17, x23 - 2, y27, fill="blue", outline="black")
    
    right_winding = canvas.create_rectangle(x21 + 2, y17, x21 + 10, y27, fill="blue", outline="black")
    right_winding = canvas.create_rectangle(x21 + 12, y17, x21 + 20, y27, fill="red", outline="black")
    
    # Red vertical lines
    canvas.create_line(x11, y11, x11, y11 - 100, fill="red", width=2)
    canvas.create_line(x11 + width1, y11 , x11 + width1, y11 - 100, fill="red", width=2)

    canvas.create_line(x12, y12, x12, y12 - 100, fill="red", width=2)
    canvas.create_line(x12 + width2, y12, x12 + width2, y12 - 100, fill="red", width=2)

    canvas.create_line(x13, y13, x13, y13 - 100, fill="red", width=2)
    canvas.create_line(x13 + width3, y13, x13 + width3, y13 - 100, fill="red", width=2)

    # Blue horizontal lines
    canvas.create_line(x11 + width1, y11, x11 + width1 + 100, y11, fill="blue", width=2) 
    canvas.create_line(x11 + width1, y21,  x11 + width1 + 100, y21, fill="blue", width=2)

    canvas.create_line(x13 + width3, y13, x13 + width3 + 100 , y13, fill="blue", width=2)
    canvas.create_line(x13 + width3, y23,  x13 + width3 + 100, y23, fill="blue", width=2) 

    # --- Dimension markers between lines ---

    # Vertical line pairs → horizontal dimension lines
    canvas.create_line(x11, y11 - 100, x11 + width1, y11 - 100, fill="black", width=1, dash=(4,2))  # between first and second vertical line
    canvas.create_text(cx1, y11 - 110, text=f"{W: .2f} m", font=("Arial", 10))

    canvas.create_line(x12, y12 - 100, x12 + width2, y12 - 100, fill="black", width=1, dash=(4,2))  # between second and third vertical line
    canvas.create_text(cx2, y12 - 110, text=f"{Ww: .2f} m", font=("Arial", 10))

    canvas.create_line(x13, y13 - 100, x13 + width3, y13 - 100, fill="black", width=1, dash=(4,2))  # between third and fourth vertical line
    canvas.create_text(cx3, y13 - 110, text=f"{Ww: .2f} m", font=("Arial", 10))


    # Horizontal line pairs → vertical dimension lines
    canvas.create_line(x21 + 100, y11, x21 + 100, y11 + height1, fill="black", width=1, dash=(4,2))
    canvas.create_text(x21 + 110, cy1, text=f"{H: .2f} m", font=("Arial", 10))

    canvas.create_line(x23 + 100, y13, x23 + 100, y13 + height3, fill="black", width=1, dash=(4,2))
    canvas.create_text(x23 + 110, cy3, text=f"{Hw: .2f} m", font=("Arial", 10))
    
    #------------------------------ MARKING SECTION -------------------------------


    # Red vertical lines (lower side — mirrored)
    canvas.create_line(x11, y21, x11, y21 +100, fill="red", width=2)
    canvas.create_line(x21, y21, x21, y21 + 100, fill="red", width=2)

    canvas.create_line(x12, y22, x12, y22 + 100, fill="red", width=2)
    canvas.create_line(x22, y22, x22, y22 + 100, fill="red", width=2)

    canvas.create_line(x13, y23, x13, y23 + 100, fill="red", width=2)
    canvas.create_line(x23, y23, x23, y23 + 100, fill="red", width=2)

    # Bottom horizontal dimension lines (mirrored)
    canvas.create_line(x11, y21 + 100, x11 + width1, y21 + 100, fill="black", width=1, dash=(4,2))  
    canvas.create_text(cx1, y21 + 110, text="W", font=("Arial", 10))

    canvas.create_line(x12, y22 + 100, x12 + width2, y22 + 100, fill="black", width=1, dash=(4,2))  
    canvas.create_text(cx2, y22 + 110, text="Ww", font=("Arial", 10))

    canvas.create_line(x13, y23 + 100, x13 + width3, y23 + 100, fill="black", width=1, dash=(4,2))  
    canvas.create_text(cx3, y23 + 110, text="Ww", font=("Arial", 10))


    # --- Mirrored blue horizontal lines (left side) ---
    canvas.create_line(x11, y11, x11 - 100, y11, fill="blue", width=2) 
    canvas.create_line(x11, y21, x11 - 100, y21, fill="blue", width=2)

    canvas.create_line(x12, y12, x12 - 100, y12, fill="blue", width=2)
    canvas.create_line(x12, y22, x12 - 100, y22, fill="blue", width=2) 

    # --- Dimension markers for left-side horizontal lines ---
    canvas.create_line(x11 - 100, y11, x11 - 100, y11 + height1, fill="black", width=1, dash=(4,2))  # vertical marker
    canvas.create_text(x11 - 110, cy1, text="H", font=("Arial", 10))

    canvas.create_line(x12 - 100, y12, x12 - 100, y12 + height2, fill="black", width=1, dash=(4,2))  # vertical marker
    canvas.create_text(x12 - 110, cy2, text="Hw", font=("Arial", 10))
    
    info_x = 10
    info_y = 10
    line_height = 15

    canvas.create_rectangle(info_x-5, info_y-5, 160, info_y + 6*line_height, fill="lightyellow", outline="black")

    # Labels + values
    canvas.create_text(info_x, info_y, anchor="nw", text=f"Width of the core  : {W:.2f} m", font=("Arial", 8), fill="black")
    canvas.create_text(info_x, info_y + line_height, anchor="nw", text=f"Width of the window : {Ww:.2f} m", font=("Arial", 8), fill="black")
    canvas.create_text(info_x, info_y + 2*line_height, anchor="nw", text=f"Height of the core  : {H:.2f} m", font=("Arial", 8), fill="black")
    canvas.create_text(info_x, info_y + 3*line_height, anchor="nw", text=f"Height of the window : {Hw:.2f} m", font=("Arial", 8), fill="black")
    canvas.create_text(info_x, info_y + 4*line_height, anchor="nw", text=f"Heigth of the tank : {Ht:.2f} m", font=("Arial", 8), fill="black")
    canvas.create_text(info_x, info_y + 5*line_height, anchor="nw", text=f"Widht of the tank  : {Wt:.2f} m", font=("Arial", 8), fill="black")
    
    
    
    tubes = calculate_tubes(Ht, Wt, Lt, power_value, kv_value, V2)
    print(tubes/250)
 
   
   
def calculate_tubes(Ht, Wt, Lt, power_value, kv_value, V2):
    # Fixed parameters
    r_tube = 0.025   # Tube radius (m)
    h_rad = 6        # Radiation dissipation (W/m²°C)
    h_conv = 6.5     # Convection dissipation (W/m²°C)

    # Transformer losses (1% assumption)
    P_loss = 0.01 * power_value * 1000  # <-- FIXED

    # Tank surface area
    S_tank = 2 * (Ht * Wt + Ht * Lt) + (Wt * Lt)

    # Heat dissipation
    h_total = h_rad + h_conv

    # Required total surface area
    A_req = P_loss / h_total

    # Extra area needed from tubes
    A_tubes = max(0, A_req - S_tank)

    # Tube length
    L_tube = Ht - 0.1

    # Tube area
    pi = 3.1416
    A_one = 2 * pi * r_tube * L_tube

    # Number of tubes
    if A_one > 0:
        N_tubes = int(A_tubes / A_one)
        if A_tubes % A_one != 0:
            N_tubes += 1
    else:
        N_tubes = 0

    return N_tubes






    
    
# ---------- Input Frame ----------
input_frame = tk.LabelFrame(root, text="Transformer Parameters", padx=10, pady=10)
input_frame.pack(side="left", padx=10, pady=10, fill="y")

# Label + Input fields
tk.Label(input_frame, text="Enter Power (P):").pack(anchor="w")
power_entry = tk.Entry(input_frame)
power_entry.pack(fill="x", pady=2)

tk.Label(input_frame, text="Enter Frequency (F):").pack(anchor="w")
frequency = tk.Entry(input_frame)
frequency.pack(fill="x", pady=2)

tk.Label(input_frame, text="Enter Flux Density (B):").pack(anchor="w")
flux_density = tk.Entry(input_frame)
flux_density.pack(fill="x", pady=2)

tk.Label(input_frame, text="Enter Step Of core:").pack(anchor="w")
step = tk.Entry(input_frame)
step.pack(fill="x", pady=2)

tk.Label(input_frame, text="Enter primary kv:").pack(anchor="w")
kv = tk.Entry(input_frame)
kv.pack(fill="x", pady=2)

tk.Label(input_frame, text="Enter current density:").pack(anchor="w")
current_density = tk.Entry(input_frame)
current_density.pack(fill="x", pady=2)


# Button INSIDE the same box
calculate_btn = tk.Button(input_frame, text="Design Core", command=calculate)
calculate_btn.pack(pady=10, fill="x")

tk.Label(input_frame, text="Enter Doh:").pack(anchor="w")
Doh = tk.Entry(input_frame)
Doh.pack(fill="x", pady=2)

calculate_btn = tk.Button(input_frame, text="Design Tank", command=Tank)
calculate_btn.pack(pady=10, fill="x")

calculate_btn = tk.Button(input_frame, text="Calculate Tubes", command=calculate_tubes)
calculate_btn.pack(pady=10, fill="x")
 



# -------- Core rectangle --------





root.mainloop()
