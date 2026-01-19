import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines

def draw_lego_2x3(filename):
    # Dimensions (mm)
    pitch = 8.0
    tolerance = 0.2 # Total gap tolerance (0.1 per side)

    # Brick Dimensions
    brick_len = (3 * pitch) - tolerance  # 23.8
    brick_wid = (2 * pitch) - tolerance  # 15.8
    brick_height = 9.6

    # Stud Dimensions
    stud_dia = 4.8
    stud_radius = stud_dia / 2
    stud_height = 1.8

    # Tube Dimensions
    tube_od = 6.51
    tube_id = 4.8
    tube_radius_od = tube_od / 2
    tube_radius_id = tube_id / 2

    # Wall
    wall_thick = 1.2

    # Create Figure
    fig = plt.figure(figsize=(11, 8.5)) # Landscape
    fig.suptitle("Technical Drawing: LEGO Brick 2x3 (Part 3002)", fontsize=16, weight='bold')

    # Adjust subplot layout
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.9, wspace=0.3, hspace=0.3)

    # --- TOP VIEW (Top Left) ---
    ax_top = plt.subplot(2, 2, 1)
    ax_top.set_title("TOP VIEW")
    ax_top.set_aspect('equal')
    ax_top.set_xlim(-5, 30)
    ax_top.set_ylim(-5, 20)
    ax_top.axis('off')

    # Main Body
    rect_top = patches.Rectangle((0, 0), brick_len, brick_wid, linewidth=2, edgecolor='black', facecolor='none')
    ax_top.add_patch(rect_top)

    # Studs
    # Studs are centered on the 8mm grid.
    # The brick starts at -0.1 relative to the grid (tolerance).
    # Grid centers: x = 4, 12, 20. y = 4, 12.
    # Brick starts at 0, so first stud center is at (4 - 0.1, 4 - 0.1) relative to corner?
    # Correct Math:
    # Center of brick is (brick_len/2, brick_wid/2) = (11.9, 7.9)
    # Stud offsets from center: X: +/- 8, 0. Y: +/- 4.

    center_x = brick_len / 2
    center_y = brick_wid / 2

    stud_centers_x = [center_x - pitch, center_x, center_x + pitch]
    stud_centers_y = [center_y - (pitch/2), center_y + (pitch/2)]

    for x in stud_centers_x:
        for y in stud_centers_y:
            circle = patches.Circle((x, y), stud_radius, edgecolor='black', facecolor='none')
            ax_top.add_patch(circle)
            # Center mark
            ax_top.plot(x, y, '+', color='black', markersize=3)

    # Dimensions
    # Length
    ax_top.annotate(f"{brick_len} mm", xy=(brick_len/2, -2), xycoords='data', ha='center', va='top')
    ax_top.add_line(lines.Line2D([0, brick_len], [-1, -1], color='black', lw=1))
    # Width
    ax_top.annotate(f"{brick_wid} mm", xy=(-2, brick_wid/2), xycoords='data', ha='right', va='center', rotation=90)
    ax_top.add_line(lines.Line2D([-1, -1], [0, brick_wid], color='black', lw=1))
    # Pitch
    ax_top.annotate("8.0", xy=(center_x + pitch/2, brick_wid + 2), ha='center')
    ax_top.annotate("", xy=(center_x, brick_wid+1), xytext=(center_x+pitch, brick_wid+1), arrowprops=dict(arrowstyle='<->'))


    # --- FRONT VIEW (Bottom Left) ---
    ax_front = plt.subplot(2, 2, 3)
    ax_front.set_title("FRONT ELEVATION")
    ax_front.set_aspect('equal')
    ax_front.set_xlim(-5, 30)
    ax_front.set_ylim(-5, 20)
    ax_front.axis('off')

    # Body
    rect_front = patches.Rectangle((0, 0), brick_len, brick_height, linewidth=2, edgecolor='black', facecolor='none')
    ax_front.add_patch(rect_front)

    # Studs (Side profile)
    for x in stud_centers_x:
        rect_stud = patches.Rectangle((x - stud_radius, brick_height), stud_dia, stud_height, linewidth=1.5, edgecolor='black', facecolor='none')
        ax_front.add_patch(rect_stud)

    # Hidden Wall Lines (Dashed)
    ax_front.add_line(lines.Line2D([wall_thick, wall_thick], [0, brick_height-wall_thick], linestyle='--', color='grey'))
    ax_front.add_line(lines.Line2D([brick_len-wall_thick, brick_len-wall_thick], [0, brick_height-wall_thick], linestyle='--', color='grey'))
    ax_front.add_line(lines.Line2D([wall_thick, brick_len-wall_thick], [brick_height-wall_thick, brick_height-wall_thick], linestyle='--', color='grey'))

    # Dimensions
    # Height
    ax_front.annotate(f"{brick_height}", xy=(-2, brick_height/2), ha='right')
    ax_front.add_line(lines.Line2D([-1, -1], [0, brick_height], color='black'))
    # Stud Height
    ax_front.annotate(f"{stud_height}", xy=(brick_len+2, brick_height + stud_height/2), ha='left')
    ax_front.add_line(lines.Line2D([brick_len+1, brick_len+1], [brick_height, brick_height+stud_height], color='black'))


    # --- SIDE VIEW (Bottom Right) ---
    ax_side = plt.subplot(2, 2, 4)
    ax_side.set_title("SIDE ELEVATION")
    ax_side.set_aspect('equal')
    ax_side.set_xlim(-5, 25)
    ax_side.set_ylim(-5, 20)
    ax_side.axis('off')

    # Body
    rect_side = patches.Rectangle((0, 0), brick_wid, brick_height, linewidth=2, edgecolor='black', facecolor='none')
    ax_side.add_patch(rect_side)

    # Studs
    for y_pos in stud_centers_y: # Drawing X is actually Y dimension here
        rect_stud = patches.Rectangle((y_pos - stud_radius, brick_height), stud_dia, stud_height, linewidth=1.5, edgecolor='black', facecolor='none')
        ax_side.add_patch(rect_stud)

    # Hidden Wall Lines
    ax_side.add_line(lines.Line2D([wall_thick, wall_thick], [0, brick_height-wall_thick], linestyle='--', color='grey'))
    ax_side.add_line(lines.Line2D([brick_wid-wall_thick, brick_wid-wall_thick], [0, brick_height-wall_thick], linestyle='--', color='grey'))


    # --- BOTTOM VIEW (Top Right) ---
    ax_bot = plt.subplot(2, 2, 2)
    ax_bot.set_title("BOTTOM VIEW")
    ax_bot.set_aspect('equal')
    ax_bot.set_xlim(-5, 30)
    ax_bot.set_ylim(-5, 20)
    ax_bot.axis('off')

    # Outer Shell
    rect_bot = patches.Rectangle((0, 0), brick_len, brick_wid, linewidth=2, edgecolor='black', facecolor='none')
    ax_bot.add_patch(rect_bot)

    # Inner Wall
    rect_inner = patches.Rectangle((wall_thick, wall_thick), brick_len - 2*wall_thick, brick_wid - 2*wall_thick, linewidth=1, edgecolor='black', facecolor='none')
    ax_bot.add_patch(rect_inner)

    # Tubes
    # Tubes are located between the columns of studs.
    # Stud cols at x = 4, 12, 20 (grid).
    # Tube cols at x = 8, 16 (grid).
    # Center Y at 8 (grid).

    # Adjust for brick coordinates
    # Brick center is (11.9, 7.9).
    # Tube 1 is -4mm from center X. Tube 2 is +4mm from center X.

    tube_centers_x = [center_x - (pitch/2), center_x + (pitch/2)]

    for x in tube_centers_x:
        # Outer Circle
        circ_od = patches.Circle((x, center_y), tube_radius_od, edgecolor='black', facecolor='none', linewidth=1.5)
        ax_bot.add_patch(circ_od)
        # Inner Circle
        circ_id = patches.Circle((x, center_y), tube_radius_id, edgecolor='black', facecolor='none', linewidth=1)
        ax_bot.add_patch(circ_id)
        # Center mark
        ax_bot.plot(x, center_y, '+', color='black', markersize=3)

    # Tube Dimension
    ax_bot.annotate(f"OD {tube_od}", xy=(tube_centers_x[1], center_y), xytext=(tube_centers_x[1]+5, center_y-5),
                    arrowprops=dict(facecolor='black', arrowstyle='->'))
    ax_bot.annotate(f"ID {tube_id}", xy=(tube_centers_x[0], center_y), xytext=(tube_centers_x[0]-5, center_y-5),
                    arrowprops=dict(facecolor='black', arrowstyle='->'))

    # Footer Text with Sources
    plt.figtext(0.5, 0.02,
                "SOURCES:\n1. Bartneck, C. (2019). 'LEGO Brick Dimensions and Measurements'\n2. BrickArchitect.com/parts\n3. LUGNET (lugnet.com/cad/dimensions)",
                ha="center", fontsize=8, bbox={"facecolor":"white", "alpha":0.5, "pad":5})

    plt.savefig(filename)

draw_lego_2x3("2x3_Lego_Brick_Technical_Drawing.pdf")
