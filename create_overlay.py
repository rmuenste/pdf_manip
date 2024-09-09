from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

def create_overlay(text, output_file, x, y):
    # Create a PDF canvas for overlay
    c = canvas.Canvas(output_file, pagesize=A4)
    
    # Save the current state before rotating
    c.saveState()
    
    # Translate and rotate the canvas to match the rotated original PDF
    # 90 degrees rotated around the point where the text will start
    c.translate(x * mm, y * mm)  # Move origin to (x, y)
    c.rotate(-90)  # Rotate counter-clockwise by 90 degrees

    XA = -358
    Y = 18
    PSA = -173
    Y1 = 2 
    Y2 = -16 
    XB = 95

    XB = -86
    PSB =95 

    # Draw the text at the new origin point
    c.drawString(XA, Y, "Player A")

    # Draw the text at the new origin point
    c.drawString(PSA, Y, "PassNr")

    # Draw the text at the new origin point
    c.drawString(XB, Y, "Player B")

    # Draw the text at the new origin point
    c.drawString(PSB, Y, "PassNr")
    
    # Draw the text at the new origin point
    c.drawString(XA, Y1, "Player A")

    # Draw the text at the new origin point
    c.drawString(PSA, Y1, "PassNr")

    # Draw the text at the new origin point
    c.drawString(XB, Y1, "Player B")

    # Draw the text at the new origin point
    c.drawString(PSB, Y1, "PassNr")

    # Draw the text at the new origin point
    c.drawString(XA, Y2, "Player A")

    # Draw the text at the new origin point
    c.drawString(PSA, Y2, "PassNr")

    # Draw the text at the new origin point
    c.drawString(XB, Y2, "Player B")

    # Draw the text at the new origin point
    c.drawString(PSB, Y2, "PassNr")
    
    # Restore state and save the canvas
    c.restoreState()
    c.showPage()
    c.save()

# Example usage
create_overlay("Player B", "overlay.pdf", 100, 150)  # Adjust x, y positions in mm
