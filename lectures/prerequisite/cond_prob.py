import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def visualize_conditional_probability():
    # Sample space: outcomes of a die roll
    outcomes = [1, 2, 3, 4, 5, 6]
    
    # Event A: Number is even
    A = [2, 4, 6]
    
    # Event B: Number is greater than 3
    B = [4, 5, 6]
    
    # A ∩ B: Numbers that are both even AND > 3
    A_and_B = [4, 6]
    
    # Calculate probabilities
    P_B = len(B)/len(outcomes)
    P_A_and_B = len(A_and_B)/len(outcomes)
    P_A_given_B = P_A_and_B / P_B
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Title
    plt.title('Conditional Probability: P(Even |X>3) = P(Even ∩ X>3) / P(X>3)', 
              fontsize=14, pad=20)
    
    # Draw the complete sample space
    ax.text(1, 5.5, 'Sample Space (S):', fontsize=12, weight='bold')
    for i, num in enumerate(outcomes):
        ax.add_patch(Rectangle((1 + i*0.8, 4.5), 0.7, 0.7, 
                              facecolor='lightgray', edgecolor='black'))
        ax.text(1.35 + i*0.8, 4.85, str(num), fontsize=12, ha='center')
    
    # Draw event B (>3)
    ax.text(1, 3.8, 'Event B: X>3', fontsize=12, weight='bold')
    for i, num in enumerate(B):
        ax.add_patch(Rectangle((4.2 + i*0.8, 3.5), 0.7, 0.7, 
                     facecolor='lightblue', edgecolor='black'))
        ax.text(4.55 + i*0.8, 3.85, str(num), fontsize=12, ha='center')
    
    # Draw event A (even numbers) in B
    ax.text(1, 2.8, 'Event A∩B: Even AND >3', fontsize=12, weight='bold')
    for i, num in enumerate(A_and_B):
        ax.add_patch(Rectangle((4.2 + i*1.6, 2.5), 0.7, 0.7, 
                     facecolor='lightgreen', edgecolor='black'))
        ax.text(4.55 + i*1.6, 2.85, str(num), fontsize=12, ha='center')
    
    # Draw probability calculations
    ax.text(1, 1.5, 'Calculations:', fontsize=12, weight='bold')
    ax.text(1, 1.0, f'P(B) = {len(B)}/{len(outcomes)} = {P_B:.2f}', fontsize=12)
    ax.text(1, 0.5, f'P(A∩B) = {len(A_and_B)}/{len(outcomes)} = {P_A_and_B:.2f}', fontsize=12)
    ax.text(5, 1.0, f'P(A|B) = P(A∩B)/P(B) = {P_A_and_B:.2f}/{P_B:.2f} = {P_A_given_B:.2f}', 
            fontsize=12, weight='bold', color='red')
    
    # Add arrows to show the relationship
    ax.annotate('', xy=(7.5, 3.8), xytext=(7.5, 2.2),
                arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.text(7.7, 3.0, 'Conditioning on B', rotation=90, va='center')
    
    plt.tight_layout()
    plt.show()

# Run the visualization
